@echo off
REM PyPI Publishing Script for Windows
REM This script builds and uploads the package to PyPI

echo ========================================
echo TOPSIS Package PyPI Upload Script
echo ========================================
echo.

REM Clean old builds
echo [1/4] Cleaning old distributions...
if exist build rmdir /s /q build 2>nul
if exist dist rmdir /s /q dist 2>nul
if exist *.egg-info rmdir /s /q *.egg-info 2>nul
echo Done!
echo.

REM Build distributions
echo [2/4] Building distributions...
python -m build
if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)
echo Done!
echo.

REM Check package
echo [3/4] Checking package...
python -m twine check dist/*
if errorlevel 1 (
    echo ERROR: Package check failed!
    pause
    exit /b 1
)
echo Done!
echo.

REM Upload to PyPI
echo [4/4] Ready to upload to PyPI!
echo.
echo IMPORTANT: You need PyPI credentials!
echo - Username: __token__ (if using API token) or your PyPI username
echo - Password: Your API token or password
echo.
echo Uploading to PyPI...
python -m twine upload dist/*
if errorlevel 1 (
    echo ERROR: Upload failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Package uploaded to PyPI!
echo ========================================
echo.
echo Your package is now available at:
echo https://pypi.org/project/topsis-lavanya-102313066/
echo.
echo Test installation with:
echo pip install topsis-lavanya-102313066
echo.
pause
