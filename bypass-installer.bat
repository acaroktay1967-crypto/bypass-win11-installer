@echo off
:: Windows 11 System Requirements Bypass Script
:: This script adds registry entries to bypass TPM, Secure Boot, RAM, and CPU checks
:: Run as Administrator

echo ========================================
echo Windows 11 Requirements Bypass Tool
echo ========================================
echo.
echo This script will modify registry to bypass:
echo - TPM 2.0 requirement
echo - Secure Boot requirement
echo - RAM requirement
echo - CPU compatibility requirement
echo.
echo WARNING: Installing Windows 11 on unsupported hardware
echo may result in compatibility issues or lack of updates.
echo.
pause

echo.
echo Creating registry entries...

reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassTPMCheck /t REG_DWORD /d 1 /f
reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassSecureBootCheck /t REG_DWORD /d 1 /f
reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassRAMCheck /t REG_DWORD /d 1 /f
reg add "HKLM\SYSTEM\Setup\LabConfig" /v BypassCPUCheck /t REG_DWORD /d 1 /f

echo.
echo ========================================
echo Registry entries created successfully!
echo ========================================
echo.
echo You can now proceed with Windows 11 installation.
echo.
pause
