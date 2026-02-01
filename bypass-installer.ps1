# Windows 11 System Requirements Bypass Script (PowerShell)
# Bu betik TPM, Secure Boot, RAM ve CPU kontrollerini atlamak için registry girişleri ekler
# This script adds registry entries to bypass TPM, Secure Boot, RAM, and CPU checks
# Yönetici olarak çalıştırın / Run as Administrator

# Türkçe ve İngilizce mesajlar / Turkish and English messages
$title = @"
========================================
Windows 11 Gereksinimleri Atlama Aracı
Windows 11 Requirements Bypass Tool
========================================
"@

Write-Host $title -ForegroundColor Cyan
Write-Host ""

# Yönetici kontrolü / Administrator check
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "HATA / ERROR: Bu betik yönetici olarak çalıştırılmalıdır!" -ForegroundColor Red
    Write-Host "ERROR: This script must be run as Administrator!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Lütfen PowerShell'i sağ tıklayıp 'Yönetici olarak çalıştır' seçeneğini kullanın." -ForegroundColor Yellow
    Write-Host "Please right-click PowerShell and select 'Run as Administrator'." -ForegroundColor Yellow
    Write-Host ""
    Read-Host "Çıkmak için Enter'a basın / Press Enter to exit"
    exit 1
}

Write-Host "Bu betik registry'yi değiştirerek şunları atlayacak:" -ForegroundColor Yellow
Write-Host "This script will modify registry to bypass:" -ForegroundColor Yellow
Write-Host "  - TPM 2.0 gereksinimi / TPM 2.0 requirement" -ForegroundColor White
Write-Host "  - Secure Boot gereksinimi / Secure Boot requirement" -ForegroundColor White
Write-Host "  - RAM gereksinimi (4GB minimum) / RAM requirement (4GB minimum)" -ForegroundColor White
Write-Host "  - CPU uyumluluk gereksinimi / CPU compatibility requirement" -ForegroundColor White
Write-Host ""
Write-Host "UYARI / WARNING:" -ForegroundColor Red
Write-Host "Windows 11'i desteklenmeyen donanımda yüklemek," -ForegroundColor Yellow
Write-Host "gelecekte güncelleme alamama veya uyumluluk sorunlarına yol açabilir." -ForegroundColor Yellow
Write-Host "Installing Windows 11 on unsupported hardware" -ForegroundColor Yellow
Write-Host "may result in compatibility issues or lack of updates." -ForegroundColor Yellow
Write-Host ""

$confirmation = Read-Host "Devam etmek istiyor musunuz? (E/H) / Do you want to continue? (Y/N)"
if ($confirmation -notmatch '^[EeYy]$') {
    Write-Host "İşlem iptal edildi. / Operation cancelled." -ForegroundColor Yellow
    exit 0
}

Write-Host ""
Write-Host "Registry girişleri oluşturuluyor... / Creating registry entries..." -ForegroundColor Cyan
Write-Host ""

# Registry yolunu oluştur / Create registry path
$regPath = "HKLM:\SYSTEM\Setup\LabConfig"

try {
    # Registry yolunun var olup olmadığını kontrol et / Check if registry path exists
    if (-not (Test-Path $regPath)) {
        Write-Host "Registry yolu oluşturuluyor... / Creating registry path..." -ForegroundColor Gray
        New-Item -Path $regPath -Force | Out-Null
    }

    # Registry değerlerini ekle / Add registry values
    Write-Host "[1/4] BypassTPMCheck ayarlanıyor... / Setting BypassTPMCheck..." -ForegroundColor Gray
    Set-ItemProperty -Path $regPath -Name "BypassTPMCheck" -Value 1 -Type DWord -Force
    Write-Host "      ✓ TPM kontrolü atlandı / TPM check bypassed" -ForegroundColor Green

    Write-Host "[2/4] BypassSecureBootCheck ayarlanıyor... / Setting BypassSecureBootCheck..." -ForegroundColor Gray
    Set-ItemProperty -Path $regPath -Name "BypassSecureBootCheck" -Value 1 -Type DWord -Force
    Write-Host "      ✓ Secure Boot kontrolü atlandı / Secure Boot check bypassed" -ForegroundColor Green

    Write-Host "[3/4] BypassRAMCheck ayarlanıyor... / Setting BypassRAMCheck..." -ForegroundColor Gray
    Set-ItemProperty -Path $regPath -Name "BypassRAMCheck" -Value 1 -Type DWord -Force
    Write-Host "      ✓ RAM kontrolü atlandı (4GB destekleniyor) / RAM check bypassed (4GB supported)" -ForegroundColor Green

    Write-Host "[4/4] BypassCPUCheck ayarlanıyor... / Setting BypassCPUCheck..." -ForegroundColor Gray
    Set-ItemProperty -Path $regPath -Name "BypassCPUCheck" -Value 1 -Type DWord -Force
    Write-Host "      ✓ CPU kontrolü atlandı / CPU check bypassed" -ForegroundColor Green

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✓ Registry girişleri başarıyla oluşturuldu!" -ForegroundColor Green
    Write-Host "✓ Registry entries created successfully!" -ForegroundColor Green
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    
    # Mevcut ayarları göster / Display current settings
    Write-Host "Mevcut registry ayarları / Current registry settings:" -ForegroundColor Cyan
    Write-Host "-----------------------------------------------------" -ForegroundColor Gray
    Get-ItemProperty -Path $regPath | Select-Object BypassTPMCheck, BypassSecureBootCheck, BypassRAMCheck, BypassCPUCheck | Format-List
    
    Write-Host "Artık Windows 11 kurulumuna devam edebilirsiniz." -ForegroundColor Green
    Write-Host "You can now proceed with Windows 11 installation." -ForegroundColor Green
    Write-Host ""
    Write-Host "Not: Bu ayarlar bilgisayar yeniden başlatılsa bile kalıcıdır." -ForegroundColor Yellow
    Write-Host "Note: These settings persist even after computer restart." -ForegroundColor Yellow

} catch {
    Write-Host ""
    Write-Host "HATA / ERROR:" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Write-Host ""
    Write-Host "Registry girişleri oluşturulurken bir hata oluştu." -ForegroundColor Red
    Write-Host "An error occurred while creating registry entries." -ForegroundColor Red
    Write-Host ""
    Read-Host "Çıkmak için Enter'a basın / Press Enter to exit"
    exit 1
}

Write-Host ""
Read-Host "Çıkmak için Enter'a basın / Press Enter to exit"
