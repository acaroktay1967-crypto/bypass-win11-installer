#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows 11 System Requirements Bypass Script (Python)
Bu betik TPM, Secure Boot, RAM ve CPU kontrollerini atlamak için registry girişleri ekler
This script adds registry entries to bypass TPM, Secure Boot, RAM, and CPU checks

Yönetici olarak çalıştırın / Run as Administrator
Python 3.6 veya üzeri gereklidir / Python 3.6 or higher required
"""

import sys
import ctypes
import winreg
import platform

# Renkli çıktı için ANSI kodları / ANSI codes for colored output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    GRAY = '\033[90m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_colored(text, color=Colors.WHITE):
    """Renkli metin yazdır / Print colored text"""
    print(f"{color}{text}{Colors.RESET}")

def is_admin():
    """Yönetici yetkisi kontrolü / Check for administrator privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def check_platform():
    """Windows kontrolü / Check if running on Windows"""
    if platform.system() != 'Windows':
        print_colored("HATA / ERROR: Bu betik sadece Windows'ta çalışır!", Colors.RED)
        print_colored("ERROR: This script only works on Windows!", Colors.RED)
        return False
    return True

def create_registry_value(key_path, value_name, value_data):
    """Registry değeri oluştur / Create registry value"""
    try:
        # Registry anahtarını aç veya oluştur / Open or create registry key
        key = winreg.CreateKeyEx(
            winreg.HKEY_LOCAL_MACHINE,
            key_path,
            0,
            winreg.KEY_WRITE | winreg.KEY_WOW64_64KEY
        )
        
        # Değeri ayarla / Set the value
        winreg.SetValueEx(key, value_name, 0, winreg.REG_DWORD, value_data)
        winreg.CloseKey(key)
        return True
    except Exception as e:
        print_colored(f"Hata / Error: {str(e)}", Colors.RED)
        return False

def verify_registry_values(key_path):
    """Registry değerlerini doğrula / Verify registry values"""
    try:
        key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            key_path,
            0,
            winreg.KEY_READ | winreg.KEY_WOW64_64KEY
        )
        
        values = {}
        value_names = ["BypassTPMCheck", "BypassSecureBootCheck", "BypassRAMCheck", "BypassCPUCheck"]
        
        for name in value_names:
            try:
                value, _ = winreg.QueryValueEx(key, name)
                values[name] = value
            except (WindowsError, OSError):
                values[name] = None
        
        winreg.CloseKey(key)
        return values
    except (WindowsError, OSError):
        return None

def main():
    """Ana fonksiyon / Main function"""
    # Başlık / Title
    print_colored("\n" + "=" * 50, Colors.CYAN)
    print_colored("Windows 11 Gereksinimleri Atlama Aracı", Colors.CYAN)
    print_colored("Windows 11 Requirements Bypass Tool", Colors.CYAN)
    print_colored("=" * 50, Colors.CYAN)
    print_colored(f"Python {sys.version.split()[0]} - {platform.platform()}", Colors.GRAY)
    print_colored("=" * 50 + "\n", Colors.CYAN)
    
    # Platform kontrolü / Platform check
    if not check_platform():
        input("\nÇıkmak için Enter'a basın / Press Enter to exit...")
        return 1
    
    # Yönetici kontrolü / Administrator check
    if not is_admin():
        print_colored("HATA / ERROR: Bu betik yönetici olarak çalıştırılmalıdır!", Colors.RED)
        print_colored("ERROR: This script must be run as Administrator!\n", Colors.RED)
        print_colored("Lütfen komut istemini veya Python'ı sağ tıklayıp", Colors.YELLOW)
        print_colored("'Yönetici olarak çalıştır' seçeneğini kullanın.", Colors.YELLOW)
        print_colored("Please right-click Command Prompt or Python and", Colors.YELLOW)
        print_colored("select 'Run as Administrator'.\n", Colors.YELLOW)
        input("Çıkmak için Enter'a basın / Press Enter to exit...")
        return 1
    
    # Bilgilendirme / Information
    print_colored("Bu betik registry'yi değiştirerek şunları atlayacak:", Colors.YELLOW)
    print_colored("This script will modify registry to bypass:", Colors.YELLOW)
    print_colored("  ✓ TPM 2.0 gereksinimi / TPM 2.0 requirement", Colors.WHITE)
    print_colored("  ✓ Secure Boot gereksinimi / Secure Boot requirement", Colors.WHITE)
    print_colored("  ✓ RAM gereksinimi (4GB minimum) / RAM requirement (4GB minimum)", Colors.WHITE)
    print_colored("  ✓ CPU uyumluluk gereksinimi / CPU compatibility requirement\n", Colors.WHITE)
    
    # Uyarı / Warning
    print_colored("⚠ UYARI / WARNING:", Colors.RED)
    print_colored("Windows 11'i desteklenmeyen donanımda yüklemek,", Colors.YELLOW)
    print_colored("gelecekte güncelleme alamama veya uyumluluk sorunlarına yol açabilir.", Colors.YELLOW)
    print_colored("Installing Windows 11 on unsupported hardware", Colors.YELLOW)
    print_colored("may result in compatibility issues or lack of updates.\n", Colors.YELLOW)
    
    # Onay / Confirmation
    confirmation = input("Devam etmek istiyor musunuz? (E/H) / Do you want to continue? (Y/N): ").strip().upper()
    if confirmation not in ['E', 'Y', 'EVET', 'YES']:
        print_colored("\nİşlem iptal edildi. / Operation cancelled.", Colors.YELLOW)
        return 0
    
    print_colored("\nRegistry girişleri oluşturuluyor... / Creating registry entries...\n", Colors.CYAN)
    
    # Registry yolu / Registry path
    reg_path = r"SYSTEM\Setup\LabConfig"
    
    # Registry değerlerini oluştur / Create registry values
    bypass_checks = [
        ("BypassTPMCheck", "TPM kontrolü / TPM check"),
        ("BypassSecureBootCheck", "Secure Boot kontrolü / Secure Boot check"),
        ("BypassRAMCheck", "RAM kontrolü (4GB destekleniyor) / RAM check (4GB supported)"),
        ("BypassCPUCheck", "CPU kontrolü / CPU check")
    ]
    
    success_count = 0
    for i, (value_name, description) in enumerate(bypass_checks, 1):
        print_colored(f"[{i}/4] {value_name} ayarlanıyor... / Setting {value_name}...", Colors.GRAY)
        if create_registry_value(reg_path, value_name, 1):
            print_colored(f"      ✓ {description} atlandı / bypassed", Colors.GREEN)
            success_count += 1
        else:
            print_colored(f"      ✗ {description} ayarlanamadı / failed", Colors.RED)
    
    print()
    
    if success_count == len(bypass_checks):
        print_colored("=" * 50, Colors.GREEN)
        print_colored("✓ Registry girişleri başarıyla oluşturuldu!", Colors.GREEN)
        print_colored("✓ Registry entries created successfully!", Colors.GREEN)
        print_colored("=" * 50 + "\n", Colors.GREEN)
        
        # Mevcut ayarları doğrula / Verify current settings
        print_colored("Mevcut registry ayarları / Current registry settings:", Colors.CYAN)
        print_colored("-" * 50, Colors.GRAY)
        values = verify_registry_values(reg_path)
        if values:
            for name, value in values.items():
                status = "✓ Aktif / Enabled" if value == 1 else "✗ Kapalı / Disabled"
                color = Colors.GREEN if value == 1 else Colors.RED
                print_colored(f"  {name}: {status}", color)
        print_colored("-" * 50 + "\n", Colors.GRAY)
        
        print_colored("Artık Windows 11 kurulumuna devam edebilirsiniz.", Colors.GREEN)
        print_colored("You can now proceed with Windows 11 installation.\n", Colors.GREEN)
        print_colored("Not: Bu ayarlar bilgisayar yeniden başlatılsa bile kalıcıdır.", Colors.YELLOW)
        print_colored("Note: These settings persist even after computer restart.\n", Colors.YELLOW)
        
        return_code = 0
    else:
        print_colored("=" * 50, Colors.RED)
        print_colored("⚠ Bazı registry girişleri oluşturulamadı!", Colors.RED)
        print_colored("⚠ Some registry entries could not be created!", Colors.RED)
        print_colored("=" * 50 + "\n", Colors.RED)
        print_colored(f"Başarılı / Successful: {success_count}/{len(bypass_checks)}\n", Colors.YELLOW)
        return_code = 1
    
    input("Çıkmak için Enter'a basın / Press Enter to exit...")
    return return_code

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print_colored("\n\nİşlem kullanıcı tarafından iptal edildi.", Colors.YELLOW)
        print_colored("Operation cancelled by user.", Colors.YELLOW)
        sys.exit(0)
    except Exception as e:
        print_colored(f"\n\nBeklenmeyen hata / Unexpected error: {str(e)}", Colors.RED)
        input("\nÇıkmak için Enter'a basın / Press Enter to exit...")
        sys.exit(1)
