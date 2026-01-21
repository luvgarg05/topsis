# Complete Guide: Uploading TOPSIS Package to PyPI

## 📦 Package Information

- **Package Name**: `topsis-lavanya-102313066`
- **Display Name**: Topsis-Lavanya-102313066
- **Version**: 1.0.0
- **Author**: Lavanya Garg (Roll: 102313066)

---

## ✅ Pre-Upload Checklist

Before uploading, ensure you have:

- [x] ✅ Package built successfully (`python -m build`)
- [x] ✅ Package checked with twine (`twine check dist/*`)
- [x] ✅ README.md file included
- [x] ✅ LICENSE file included
- [x] ✅ All dependencies listed in setup.py
- [x] ✅ Entry points configured correctly
- [x] ✅ Package tested locally

---

## 🚀 Step-by-Step Upload Process

### **Step 1: Create PyPI Account**

1. Go to **https://pypi.org/account/register/**
2. Fill in your details:
   - Username: (choose a unique username)
   - Email: lgarg_be23@thapar.edu
   - Password: (create a strong password)
3. Verify your email address
4. **Important**: Enable Two-Factor Authentication (2FA) for security

### **Step 2: Create API Token (Recommended Method)**

1. Log in to PyPI: **https://pypi.org/manage/account/**
2. Go to **"API tokens"** section
3. Click **"Add API token"**
4. Token name: `topsis-lavanya-102313066` (or any name you prefer)
5. Scope: **"Entire account"** (for first upload) or **"Project: topsis-lavanya-102313066"** (for updates)
6. Click **"Add token"**
7. **COPY THE TOKEN IMMEDIATELY** - You won't see it again!
   - Format: `pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### **Step 3: Configure Credentials**

#### **Option A: Using API Token (Recommended)**

Create/Edit file: `%USERPROFILE%\.pypirc` (Windows) or `~/.pypirc` (Linux/Mac)

```ini
[pypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

[testpypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Replace** `pypi-xxxxxxxx...` with your actual API token.

#### **Option B: Using Username/Password (Less Secure)**

```ini
[pypi]
username = your_pypi_username
password = your_pypi_password
```

### **Step 4: Test Upload to TestPyPI (Optional but Recommended)**

TestPyPI is a test environment to verify your package before uploading to real PyPI.

1. **Create TestPyPI account**: https://test.pypi.org/account/register/
2. **Get TestPyPI API token**: https://test.pypi.org/manage/account/
3. **Upload to TestPyPI**:
   ```bash
   python -m twine upload --repository testpypi dist/*
   ```
4. **Test installation from TestPyPI**:
   ```bash
   pip install -i https://test.pypi.org/simple/ topsis-lavanya-102313066
   ```

### **Step 5: Upload to PyPI**

#### **Method 1: Using Command Line (Recommended)**

```bash
# Navigate to package directory
cd topsis_package

# Upload to PyPI
python -m twine upload dist/*
```

**You will be prompted for:**
- Username: `__token__` (if using API token) or your PyPI username
- Password: Your API token or password

#### **Method 2: Using Batch Script**

```bash
# Run the provided batch script
publish.bat
```

### **Step 6: Verify Upload**

1. **Check PyPI page**: https://pypi.org/project/topsis-lavanya-102313066/
2. **Test installation**:
   ```bash
   pip install topsis-lavanya-102313066
   ```
3. **Test CLI command**:
   ```bash
   topsis-cli --help
   ```

---

## 📋 Complete Upload Commands

### **Windows (Command Prompt)**

```cmd
REM Navigate to package directory
cd topsis_package

REM Clean old builds (optional)
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info

REM Build package
python -m build

REM Check package
python -m twine check dist/*

REM Upload to PyPI
python -m twine upload dist/*
```

### **Windows (PowerShell)**

```powershell
# Navigate to package directory
cd topsis_package

# Clean old builds (optional)
Remove-Item -Recurse -Force build, dist, *.egg-info -ErrorAction SilentlyContinue

# Build package
python -m build

# Check package
python -m twine check dist/*

# Upload to PyPI
python -m twine upload dist/*
```

### **Linux/Mac**

```bash
# Navigate to package directory
cd topsis_package

# Clean old builds (optional)
rm -rf build dist *.egg-info

# Build package
python -m build

# Check package
python -m twine check dist/*

# Upload to PyPI
python -m twine upload dist/*
```

---

## 🔧 Troubleshooting

### **Error: "HTTPError: 400 Bad Request"**
- **Cause**: Package name already exists or invalid metadata
- **Solution**: 
  - Check if package name is unique
  - Verify all required fields in setup.py
  - Ensure version number is incremented if updating

### **Error: "HTTPError: 403 Forbidden"**
- **Cause**: Invalid credentials or insufficient permissions
- **Solution**:
  - Verify API token is correct
  - Check token scope (should be "Entire account" or project-specific)
  - Ensure username/password are correct

### **Error: "File already exists"**
- **Cause**: Version already uploaded
- **Solution**: Increment version in `setup.py`:
  ```python
  version='1.0.1',  # Increment version
  ```

### **Error: "No module named 'build'"**
- **Solution**: Install build tools:
  ```bash
  pip install build twine
  ```

### **Error: "Invalid distribution"**
- **Solution**: Check package structure:
  ```bash
  python -m twine check dist/*
  ```

---

## 📝 Updating the Package

When you need to update the package:

1. **Update version** in `setup.py`:
   ```python
   version='1.0.1',  # Increment version number
   ```

2. **Rebuild package**:
   ```bash
   python -m build
   ```

3. **Upload new version**:
   ```bash
   python -m twine upload dist/*
   ```

---

## 🎯 Assignment Requirements Checklist

According to your assignment, ensure:

- [x] ✅ Package name follows convention: `Topsis-FirstName-RollNumber`
  - **Your package**: `topsis-lavanya-102313066` ✓
- [x] ✅ User Manual provided (README.md) ✓
- [x] ✅ Package installable via pip ✓
- [x] ✅ CLI command works after installation ✓
- [x] ✅ Tested locally before upload ✓

---

## 📚 Additional Resources

- **PyPI Documentation**: https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/
- **Twine Documentation**: https://twine.readthedocs.io/
- **TestPyPI**: https://test.pypi.org/
- **PyPI Account**: https://pypi.org/manage/account/

---

## ✅ Final Verification Steps

After upload, verify:

1. **Package page loads**: https://pypi.org/project/topsis-lavanya-102313066/
2. **Installation works**:
   ```bash
   pip install topsis-lavanya-102313066
   ```
3. **CLI command works**:
   ```bash
   topsis-cli data.csv "1,1,1,2" "+,+,-,+" output.csv
   ```
4. **Import works**:
   ```python
   from topsis_lavanya_102313066 import topsis
   ```

---

## 🎉 Success!

Once uploaded, your package will be available at:
**https://pypi.org/project/topsis-lavanya-102313066/**

Users can install it with:
```bash
pip install topsis-lavanya-102313066
```

---


