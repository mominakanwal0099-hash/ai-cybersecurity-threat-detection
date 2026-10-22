@echo off
REM ===================================================
REM AI Cyber Defense Center - Project Launcher
REM ===================================================

echo.
echo ========================================================
echo    AI CYBER THREAT DETECTION SUITE
echo    Final Year Project - Launcher
echo ========================================================
echo.

REM Change to project directory (where this bat file is located)
cd /d "%~dp0"

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ and add it to your PATH
    echo Download from: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check if pip is available
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

echo [OK] pip found
echo.

REM Install/Update dependencies
echo Installing required dependencies...
echo (This may take a few minutes on first run)
echo.

pip install -r requirements.txt --quiet
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to install some dependencies
    echo Trying again without --quiet flag...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo [ERROR] Could not install dependencies
        echo Please try manually: pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo.
echo [OK] All dependencies installed
echo.

REM Check that model files exist
echo Checking model files...

set MODELS_OK=1

if not exist "models\phishing_detector.pkl" (
    echo [WARNING] models\phishing_detector.pkl not found
    set MODELS_OK=0
)

if not exist "models\sms_spam_model.pkl" (
    echo [WARNING] models\sms_spam_model.pkl not found
    set MODELS_OK=0
)

if not exist "models\sms_vectorizer.pkl" (
    echo [WARNING] models\sms_vectorizer.pkl not found
    set MODELS_OK=0
)

if not exist "models\fake_job_model.pkl" (
    echo [WARNING] models\fake_job_model.pkl not found
    set MODELS_OK=0
)

if not exist "models\fake_job_vectorizer.pkl" (
    echo [WARNING] models\fake_job_vectorizer.pkl not found
    set MODELS_OK=0
)

if %MODELS_OK%==1 (
    echo [OK] All model files found
) else (
    echo.
    echo [WARNING] Some model files are missing!
    echo The app may not work correctly.
    echo Please ensure all .pkl files are in the models\ directory.
    echo.
)

echo.

REM Ask which app to run
echo ========================================================
echo   Choose which application to launch:
echo ========================================================
echo.
echo   [1] Main App (app.py)
echo       - Full suite: Phishing + SMS Spam + Fake Job
echo       - Dashboard, History, Model Performance
echo.
echo   [2] Advanced SOC App (advanced_app.py)
echo       - SOC Dashboard with live monitoring
echo       - Phishing-only detection
echo       - Threat Intelligence and Analytics
echo.

set /p CHOICE="Enter your choice (1 or 2, default=1): "

if "%CHOICE%"=="" set CHOICE=1

echo.
echo ========================================================

if "%CHOICE%"=="2" (
    echo Starting Advanced SOC App...
    echo The app will open in your browser at:
    echo   http://localhost:8501
    echo ========================================================
    echo.
    echo Press Ctrl+C to stop the server.
    echo.
    streamlit run advanced_app.py
) else (
    echo Starting Main Threat Detection Suite...
    echo The app will open in your browser at:
    echo   http://localhost:8501
    echo ========================================================
    echo.
    echo Press Ctrl+C to stop the server.
    echo.
    streamlit run app.py
)

pause
