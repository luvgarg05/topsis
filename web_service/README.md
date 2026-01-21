# TOPSIS Web Service Documentation

## Overview

This is a Flask-based web service for TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) analysis. It provides an interactive interface for multi-criteria decision-making with file upload support and email delivery.

## Features

- ✅ Web-based user interface
- ✅ Multi-file format support (CSV, Excel, JSON)
- ✅ Real-time input validation
- ✅ Email result delivery
- ✅ CSV download functionality
- ✅ Responsive design

## Setup

### Requirements

- Python 3.7+
- Flask 2.3.3
- pandas 2.0.3
- numpy 2.2.6
- openpyxl 3.1.5
- python-dotenv 1.0.0

### Installation

```bash
cd web_service
pip install -r requirements.txt
```

### Configuration

Create a `.env` file with:

```
SENDER_EMAIL=your-email@gmail.com
SENDER_PASSWORD=your-app-password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
FLASK_ENV=development
MAX_FILE_SIZE=10485760
```

**Note:** For Gmail, use an App-Specific Password instead of your regular password.

## Running

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## API Endpoints

### POST /api/validate
Validate user inputs (email, weights, impacts).

**Request:**
```json
{
  "email": "user@example.com",
  "weights": "1,1,1,2",
  "impacts": "+,+,-,+"
}
```

**Response:**
```json
{
  "valid": true,
  "errors": {}
}
```

### POST /api/analyze
Perform TOPSIS analysis on uploaded file.

**Request:** (multipart/form-data)
- file: Data file (CSV, Excel, JSON)
- email: Recipient email
- weights: Comma-separated weights
- impacts: Comma-separated impacts

**Response:**
```json
{
  "success": true,
  "results": [
    {"name": "Option1", "score": 0.845, "rank": 1},
    {"name": "Option2", "score": 0.562, "rank": 2}
  ],
  "download_filename": "topsis_result_20240101_120000.csv",
  "email_sent": true
}
```

### GET /api/download/<filename>
Download result file.

## File Format

### CSV
```
Mobile,Storage,RAM,Price,Battery
M1,256,8,30000,5000
M2,512,12,40000,6000
```

### Excel (.xlsx, .xls)
Same structure as CSV. Formulas are evaluated to values.

### JSON
```json
[
  {"Mobile": "M1", "Storage": 256, "RAM": 8, "Price": 30000, "Battery": 5000},
  {"Mobile": "M2", "Storage": 512, "RAM": 12, "Price": 40000, "Battery": 6000}
]
```

## Algorithm

**Step 1:** Normalize decision matrix
**Step 2:** Apply weights
**Step 3:** Find ideal solutions
**Step 4:** Calculate separations
**Step 5:** Calculate scores and ranks

## Error Handling

- Invalid file format → 400 error
- Missing required fields → 400 error
- File too large → 413 error
- Server error → 500 error

## Email Configuration

### Gmail Setup

1. Enable 2-factor authentication
2. Generate App-Specific Password
3. Use in `.env` file

### Other Email Providers

Update `.env` with appropriate SMTP settings.

## Security

- Files are temporarily stored and automatically deleted
- Input validation on all user inputs
- File upload restrictions (type, size)
- Secure filename handling

## Troubleshooting

**Email not sending:**
- Check SENDER_EMAIL and SENDER_PASSWORD in `.env`
- For Gmail, ensure App-Specific Password is used
- Check SMTP_SERVER and SMTP_PORT settings

**File upload errors:**
- Ensure file format is supported
- Check file size (max 10MB)
- Verify data format (first column non-numeric, rest numeric)

**Analysis errors:**
- Verify weights count matches criteria count
- Ensure all values are positive
- Check impacts are + or -

## License

MIT License
