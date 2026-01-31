@echo off
:: Advanced Windows 11 Setup Bypass Script
:: To be used during Windows 11 setup with Shift+F10
:: This script is designed to work in Windows PE environment

echo ========================================
echo Windows 11 Setup Requirements Bypass
echo ========================================
echo.
echo This script will bypass Windows 11 hardware checks
echo during the installation process.
echo.
echo Requirements being bypassed:
echo  - TPM 2.0
echo  - Secure Boot
echo  - RAM (minimum 4GB)
echo  - CPU Compatibility
echo.
pause

echo.
echo Loading registry hive...

:: Check if we're in Windows PE (setup environment)
reg query "HKLM\SYSTEM\Setup\LabConfig" >nul 2>&1
if %errorlevel% equ 0 (
    echo Registry key already exists. Updating values...
) else (
    echo Creating registry key...
)

echo.
echo Setting bypass values...

reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassTPMCheck /t REG_DWORD /d 1 /f >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] TPM check bypass enabled
) else (
    echo [ERROR] Failed to set TPM bypass
)

reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassSecureBootCheck /t REG_DWORD /d 1 /f >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Secure Boot check bypass enabled
) else (
    echo [ERROR] Failed to set Secure Boot bypass
)

reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassRAMCheck /t REG_DWORD /d 1 /f >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] RAM check bypass enabled
) else (
    echo [ERROR] Failed to set RAM bypass
)

reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassCPUCheck /t REG_DWORD /d 1 /f >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] CPU check bypass enabled
) else (
    echo [ERROR] Failed to set CPU bypass
)

echo.
echo ========================================
echo Configuration Complete!
echo ========================================
echo.
echo You can now close this window and continue
echo with the Windows 11 installation.
echo.
echo Press any key to verify the settings...
pause >nul

echo.
echo Current registry values:
echo ------------------------
reg query "HKLM\SYSTEM\Setup\LabConfig" /v BypassTPMCheck
reg query "HKLM\SYSTEM\Setup\LabConfig" /v BypassSecureBootCheck
reg query "HKLM\SYSTEM\Setup\LabConfig" /v BypassRAMCheck
reg query "HKLM\SYSTEM\Setup\LabConfig" /v BypassCPUCheck

echo.
echo Press any key to close...
pause >nul
