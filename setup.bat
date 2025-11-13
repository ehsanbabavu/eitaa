@echo off
chcp 65001 > nul
echo ========================================
echo نصب خودکار برنامه اتوماسیون ایتا
echo Eitaa Automation - Automatic Setup
echo ========================================
echo.

echo [1/4] بررسی نصب Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python نصب نیست!
    echo لطفا Python را از https://www.python.org/downloads/ دانلود و نصب کنید
    echo حتماً گزینه "Add Python to PATH" را فعال کنید
    pause
    exit /b 1
)
echo ✓ Python نصب شده است
python --version
echo.

echo [2/4] بررسی نصب pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  pip command not found, trying python -m pip...
    python -m pip --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ pip نصب نیست!
        pause
        exit /b 1
    )
)
echo ✓ pip نصب شده است
echo.

echo [3/4] نصب کتابخانه‌های مورد نیاز...
echo این ممکن است چند دقیقه طول بکشد...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo.
    echo ❌ خطا در نصب کتابخانه‌ها!
    echo لطفا اتصال اینترنت خود را بررسی کنید
    pause
    exit /b 1
)
echo.
echo ✓ کتابخانه‌ها با موفقیت نصب شدند
echo.

echo [4/4] بررسی نصب Google Chrome...
where chrome >nul 2>&1
if %errorlevel% neq 0 (
    where "C:\Program Files\Google\Chrome\Application\chrome.exe" >nul 2>&1
    if %errorlevel% neq 0 (
        where "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" >nul 2>&1
        if %errorlevel% neq 0 (
            echo ⚠️  Google Chrome پیدا نشد
            echo لطفا Chrome را از https://www.google.com/chrome/ دانلود و نصب کنید
            echo.
        ) else (
            echo ✓ Google Chrome نصب شده است
        )
    ) else (
        echo ✓ Google Chrome نصب شده است
    )
) else (
    echo ✓ Google Chrome نصب شده است
)
echo.

echo ========================================
echo ✅ نصب با موفقیت تکمیل شد!
echo ========================================
echo.
echo برای اجرای برنامه از دستور زیر استفاده کنید:
echo   python eitaa_automation.py
echo.
echo یا با شماره دلخواه:
echo   python eitaa_automation.py 9101234567
echo.
pause
