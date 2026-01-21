# Email Configuration Guide

## Gmail Setup (Recommended)

### Step 1: Enable 2-Factor Authentication
1. Go to [Google Account Security](https://myaccount.google.com/security)
2. Click "2-Step Verification"
3. Follow the steps to enable 2FA

### Step 2: Generate App-Specific Password
1. Go to [App Passwords](https://myaccount.google.com/apppasswords)
2. Select **Mail** and **Windows** (or your device)
3. Google will generate a 16-character password
4. Copy this password

### Step 3: Update .env File
Open `.env` in the `web_service` directory and update:

```
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=xxxx xxxx xxxx xxxx
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

**Important:** Use the 16-character app password, NOT your regular Gmail password!

---

## Troubleshooting

### Error: "Email authentication failed"
- ✓ Make sure you're using the App-Specific Password, not regular password
- ✓ Check that 2-Factor Authentication is enabled
- ✓ Verify email address is correct (no typos)

### Error: "Email not configured"
- ✓ Check `.env` file exists in `web_service/` directory
- ✓ Verify `SENDER_EMAIL` and `SENDER_PASSWORD` are filled in
- ✓ Restart the Flask app after updating `.env`

### Error: "Connection refused"
- ✓ Check internet connection
- ✓ Verify SMTP_SERVER (smtp.gmail.com) and SMTP_PORT (587)
- ✓ Try adding `@gmail.com` to email if using Gmail

### Email Not Arriving
- ✓ Check spam folder
- ✓ Verify recipient email is correct
- ✓ Check console output for detailed error messages

---

## Other Email Providers

### Outlook/Office 365
```
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
SENDER_EMAIL=your-email@outlook.com
SENDER_PASSWORD=your-password
```

### Yahoo Mail
```
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
SENDER_EMAIL=your-email@yahoo.com
SENDER_PASSWORD=your-16-character-app-password
```

### Custom/Corporate Email
Ask your IT department for:
- SMTP Server address
- SMTP Port (usually 587 or 465)
- Your email credentials

---

## Testing Email Configuration

To test if email is working:

1. Open terminal in `web_service/` directory
2. Run:
```python
python
from app import send_email
success, msg = send_email("test@example.com", "Test Subject", "<h1>Test Body</h1>")
print(success, msg)
```

3. Check the output for detailed error messages

---

## How to Get App-Specific Password (Step-by-Step with Screenshots)

### For Gmail:
1. Open https://myaccount.google.com
2. Click **Security** on the left menu
3. Scroll down to find **2-Step Verification** (enable if not done)
4. Below that, find **App passwords**
5. Select **Mail** from first dropdown
6. Select **Windows** (or your OS) from second dropdown
7. Click **Generate**
8. Copy the 16-character password shown
9. Paste it in `.env` file

---

## Email Features

After setting up email:
- ✅ Results sent automatically after analysis
- ✅ Includes analysis summary
- ✅ CSV file attached
- ✅ Professional formatted email

---

**Still having issues?** 
1. Check the console output when running the web service for [EMAIL] logs
2. Verify all settings in `.env` file
3. Test with a simple email first before uploading data files
