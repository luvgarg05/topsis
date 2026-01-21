# TOPSIS - Deployment Guide

## Production Deployment

This guide covers deploying the TOPSIS application to production environments.

---

## Option 1: Heroku Deployment

### Prerequisites
- Heroku CLI installed
- Git repository initialized
- Free Heroku account

### Setup

1. **Create Heroku app:**
```bash
heroku create your-app-name
```

2. **Set environment variables:**
```bash
heroku config:set SENDER_EMAIL=your-email@gmail.com
heroku config:set SENDER_PASSWORD=your-app-password
heroku config:set SMTP_SERVER=smtp.gmail.com
heroku config:set SMTP_PORT=587
```

3. **Add Procfile:**
```
web: cd web_service && gunicorn app:app
```

4. **Deploy:**
```bash
git push heroku main
```

---

## Option 2: AWS Deployment

### Using Elastic Beanstalk

1. **Install EB CLI:**
```bash
pip install awsebcli
```

2. **Initialize:**
```bash
eb init -p python-3.9 topsis-app
```

3. **Create environment:**
```bash
eb create topsis-env
```

4. **Set environment variables:**
```bash
eb setenv SENDER_EMAIL=your-email@gmail.com SENDER_PASSWORD=your-password
```

5. **Deploy:**
```bash
eb deploy
```

---

## Option 3: Docker Deployment

### Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "web_service/app.py"]
```

### Build and Run

```bash
docker build -t topsis-app .
docker run -p 5000:5000 \
  -e SENDER_EMAIL=your-email@gmail.com \
  -e SENDER_PASSWORD=your-password \
  topsis-app
```

---

## Option 4: Traditional Server (AWS EC2, DigitalOcean, etc.)

### Setup

1. **SSH into server:**
```bash
ssh ubuntu@your-server-ip
```

2. **Install dependencies:**
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-venv
```

3. **Clone repository:**
```bash
git clone your-repo-url
cd topsis-lavanya-102313066
```

4. **Create virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate
```

5. **Install packages:**
```bash
pip install -r web_service/requirements.txt
pip install gunicorn
```

6. **Set environment variables:**
```bash
export SENDER_EMAIL=your-email@gmail.com
export SENDER_PASSWORD=your-password
```

7. **Run with Gunicorn:**
```bash
gunicorn --bind 0.0.0.0:5000 --chdir web_service app:app
```

### Using Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Systemd Service

Create `/etc/systemd/system/topsis.service`:

```ini
[Unit]
Description=TOPSIS Web Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/topsis-lavanya-102313066
Environment="PATH=/home/ubuntu/topsis-lavanya-102313066/venv/bin"
EnvironmentFile=/home/ubuntu/.topsis.env
ExecStart=/home/ubuntu/topsis-lavanya-102313066/venv/bin/gunicorn --bind 0.0.0.0:5000 --chdir web_service app:app
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable topsis
sudo systemctl start topsis
```

---

## Environment Configuration

### Production .env Example

```
SENDER_EMAIL=noreply@topsis-app.com
SENDER_PASSWORD=secure-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FLASK_ENV=production
MAX_FILE_SIZE=52428800
```

### Security Considerations

1. Use strong, randomly generated passwords
2. Store secrets in environment variables (not in code)
3. Use HTTPS in production
4. Enable CORS only for trusted domains
5. Rate limit API endpoints
6. Monitor logs for suspicious activity

---

## SSL/TLS Certificate

### Let's Encrypt (Free)

```bash
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d your-domain.com
```

Update Nginx to use certificate:

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    # ... rest of config
}
```

---

## Performance Optimization

### 1. Enable Caching

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/api/download/<filename>')
@cache.cached(timeout=300)
def download(filename):
    # ...
```

### 2. Use Async Tasks

```python
from celery import Celery

celery = Celery(app.name, broker='redis://localhost:6379')

@celery.task
def analyze_async(email, weights, impacts):
    # Long-running analysis
    pass
```

### 3. Database Connection Pooling

Use connection pooling for databases if storing results.

---

## Monitoring and Logging

### Application Logging

```python
import logging

logging.basicConfig(
    filename='topsis.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Monitoring Tools

1. **Sentry:** Error tracking
2. **New Relic:** Performance monitoring
3. **ELK Stack:** Centralized logging
4. **Prometheus:** Metrics collection

### Setup Sentry

```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    "your-sentry-dsn",
    integrations=[FlaskIntegration()]
)
```

---

## Backup and Recovery

### Backup Strategy

1. **Database backups:** Daily automated backups
2. **Code repository:** Git with multiple remotes
3. **Configuration:** Store .env securely (e.g., AWS Secrets Manager)

### Recovery Plan

1. Restore from latest backup
2. Verify data integrity
3. Test critical functions
4. Monitor for issues

---

## Scaling

### Horizontal Scaling

1. Deploy multiple application instances
2. Use load balancer (AWS ELB, Nginx)
3. Scale database separately

### Vertical Scaling

1. Increase server resources (CPU, RAM)
2. Optimize code and queries
3. Enable caching

### Database Optimization

- Index frequently queried columns
- Archive old data
- Use connection pooling
- Consider read replicas

---

## Maintenance

### Regular Tasks

- Monitor disk space usage
- Update dependencies monthly
- Review and rotate logs
- Check SSL certificate expiration
- Monitor error rates
- Update OS security patches

### Rollback Procedure

```bash
# Revert to previous version
git rollback previous-tag
git push heroku main

# Or for traditional servers
cd /var/www/topsis
git checkout v1.0.0
systemctl restart topsis
```

---

## CI/CD Pipeline

### GitHub Actions Example

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: python test_all.py

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        run: |
          git push https://heroku:${{ secrets.HEROKU_API_KEY }}@git.heroku.com/${{ secrets.HEROKU_APP_NAME }}.git main
```

---

## Support and Issues

For deployment issues:
1. Check application logs
2. Verify environment variables
3. Test connectivity (email, file storage)
4. Review security group/firewall rules
5. Contact support with error logs

---

## Checklist for Production

- ✅ Environment variables configured
- ✅ SSL/TLS certificate installed
- ✅ Database backups automated
- ✅ Logging and monitoring enabled
- ✅ Error handling tested
- ✅ Load testing completed
- ✅ Security audit completed
- ✅ Documentation updated
- ✅ Rollback plan documented
- ✅ Team trained on deployment

