# Assignment Steps: PyPI Package Upload

## ✅ Package Status: READY FOR UPLOAD

Your PyPI package is **fully prepared** and ready to upload!

---

## 📦 Package Details

- **Package Name**: `topsis-lavanya-102313066`
- **Version**: 1.0.0
- **Display Name**: Topsis-Lavanya-102313066
- **Author**: Lavanya Garg (Roll: 102313066)
- **Status**: ✅ Built and Verified

---

## 🎯 Assignment Requirements (Part-II)

### ✅ Completed Requirements:

1. ✅ **Python Package Created**
   - Package structure: `topsis_package/topsis_lavanya_102313066/`
   - Core files: `topsis.py`, `cli.py`, `__init__.py`
   - Setup configuration: `setup.py`

2. ✅ **Naming Convention**
   - Format: `Topsis-FirstName-RollNumber`
   - Your package: `topsis-lavanya-102313066` ✓
   - Matches requirement: `Topsis-Shyam-10155792` pattern

3. ✅ **User Manual Provided**
   - Location: `topsis_package/README.md`
   - Includes: Installation, Usage, Examples, Documentation

4. ✅ **CLI Command Configured**
   - Command: `topsis-cli`
   - Usage: `topsis-cli <InputDataFile> <Weights> <Impacts> <OutputResultFileName>`
   - Tested: ✅ Works correctly

5. ✅ **Package Tested Locally**
   - Installation: ✅ Success
   - CLI command: ✅ Works
   - Import: ✅ Works

---

## 📋 Steps to Upload to PyPI (Assignment Task)

### **Step 1: Create PyPI Account**

1. Go to: **https://pypi.org/account/register/**
2. Fill registration form:
   - Username: (choose unique username)
   - Email: lgarg_be23@thapar.edu
   - Password: (create strong password)
3. Verify email address
4. **Enable 2FA** (recommended for security)

### **Step 2: Get API Token**

1. Log in: **https://pypi.org/manage/account/**
2. Go to **"API tokens"** section
3. Click **"Add API token"**
4. Token name: `topsis-lavanya-102313066`
5. Scope: **"Entire account"** (for first upload)
6. Click **"Add token"**
7. **COPY THE TOKEN** (format: `pypi-xxxxxxxx...`)

### **Step 3: Configure Credentials**

**Windows:**
1. Open Notepad
2. Create file: `C:\Users\HP\.pypirc`
3. Add content:
   ```ini
   [pypi]
   username = __token__
   password = pypi-YOUR_TOKEN_HERE
   ```
4. Replace `YOUR_TOKEN_HERE` with your actual token
5. Save file

**Note**: If file doesn't exist, create it. Hide file extensions in Windows Explorer if needed.

### **Step 4: Upload Package**

**Option A: Using Batch Script (Easiest)**

```bash
cd topsis_package
publish.bat
```

**Option B: Using Command Line**

```bash
cd topsis_package
python -m twine upload dist/*
```

**When prompted:**
- Username: `__token__`
- Password: Your API token (pypi-xxxxxxxx...)

### **Step 5: Verify Upload**

1. **Check PyPI page**: https://pypi.org/project/topsis-lavanya-102313066/
2. **Test installation**:
   ```bash
   pip install topsis-lavanya-102313066
   ```
3. **Test CLI**:
   ```bash
   topsis-cli data.csv "1,1,1,2" "+,+,-,+" output.csv
   ```

---

## 📁 Package Files Ready

All files are prepared in `topsis_package/`:

```
topsis_package/
├── dist/                                    # ✅ Built packages
│   ├── topsis_lavanya_102313066-1.0.0-py3-none-any.whl
│   └── topsis-lavanya-102313066-1.0.0.tar.gz
├── topsis_lavanya_102313066/                # ✅ Source code
│   ├── __init__.py
│   ├── topsis.py
│   └── cli.py
├── setup.py                                  # ✅ Package config
├── README.md                                 # ✅ User manual
├── LICENSE                                   # ✅ MIT License
├── MANIFEST.in                               # ✅ Include files
├── publish.bat                               # ✅ Upload script
├── PYPI_UPLOAD_GUIDE.md                     # ✅ Detailed guide
├── QUICK_UPLOAD.md                          # ✅ Quick reference
└── ASSIGNMENT_STEPS.md                       # ✅ This file
```

---

## 🧪 Testing Checklist (Before Upload)

- [x] Package builds successfully
- [x] Package passes twine check
- [x] CLI command works: `topsis-cli --help`
- [x] Import works: `from topsis_lavanya_102313066 import topsis`
- [x] Function works: `topsis("data.csv", "1,1,1,2", "+,+,-,+", "output.csv")`
- [x] README.md is complete
- [x] LICENSE file included

---

## 📝 Assignment Submission Checklist

After uploading, include in your submission:

- [ ] PyPI package URL: https://pypi.org/project/topsis-lavanya-102313066/
- [ ] Installation command: `pip install topsis-lavanya-102313066`
- [ ] Usage example: `topsis-cli data.csv "1,1,1,2" "+,+,-,+" output.csv`
- [ ] Screenshot of PyPI package page
- [ ] Screenshot of successful installation
- [ ] Screenshot of CLI usage

---

## 🆘 Troubleshooting

### **Error: "Package already exists"**
- Solution: Your package name is already taken (unlikely) or version exists
- Fix: Increment version in `setup.py` to `1.0.1`

### **Error: "Invalid credentials"**
- Solution: Check `.pypirc` file format
- Fix: Ensure `username = __token__` and token starts with `pypi-`

### **Error: "File not found"**
- Solution: Run `python -m build` first
- Fix: Ensure you're in `topsis_package` directory

### **Error: "No module named 'twine'"**
- Solution: Install twine: `pip install twine`

---

## 📚 Reference Links

- **PyPI Registration**: https://pypi.org/account/register/
- **API Tokens**: https://pypi.org/manage/account/token/
- **Your Package Page**: https://pypi.org/project/topsis-lavanya-102313066/ (after upload)
- **Twine Docs**: https://twine.readthedocs.io/

---

## ✅ Final Steps Summary

1. ✅ Package built: `python -m build`
2. ✅ Package checked: `python -m twine check dist/*`
3. ⏳ Create PyPI account
4. ⏳ Get API token
5. ⏳ Configure `.pypirc` file
6. ⏳ Upload: `python -m twine upload dist/*`
7. ⏳ Verify: Visit PyPI page and test installation

---

**You're all set! Follow the steps above to upload your package to PyPI.** 🚀

For detailed instructions, see: **PYPI_UPLOAD_GUIDE.md**
