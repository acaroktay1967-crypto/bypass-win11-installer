# Windows 11 Installer Bypass / Windows 11 Yükleyici Gereksinimleri Atlama

Bu araç, Windows 11 kurulumu sırasında TPM 2.0, Secure Boot, RAM ve CPU gereksinimlerini atlamanıza olanak tanır.

This tool allows you to bypass TPM 2.0, Secure Boot, RAM, and CPU requirements during Windows 11 installation.

---

## 🇹🇷 Türkçe Kullanım Kılavuzu

### ⚠️ Uyarı
Windows 11'i desteklenmeyen donanımda yüklemek, gelecekte güncelleme almama veya uyumluluk sorunları yaşama riskini beraberinde getirebilir. Bu yöntemleri kullanmadan önce riskleri anladığınızdan emin olun.

### Yöntem 1: Registry Dosyası Kullanımı (Kolay)

1. Windows 11 USB yükleyiciden bilgisayarınızı başlatın
2. "Bu PC Windows 11'i çalıştıramaz" mesajını gördüğünüzde, **Shift + F10** tuşlarına basarak Komut İstemi'ni açın
3. Komut İstemi'nde `regedit` yazın ve Enter'a basın
4. Registry Düzenleyici'de: **File > Import** menüsünden `bypass-win11-requirements.reg` dosyasını içe aktarın
5. Registry Düzenleyici'yi ve Komut İstemi'ni kapatın
6. Windows 11 kurulumuna devam edin

### Yöntem 2: Manuel Registry Düzenleme

1. Windows 11 USB yükleyiciden bilgisayarınızı başlatın
2. Sistem gereksinimleri uyarısı ekranında **Shift + F10** tuşlarına basın
3. Komut İstemi'nde `regedit` yazın ve Enter'a basın
4. Şu konuma gidin: `HKEY_LOCAL_MACHINE\SYSTEM\Setup`
5. `Setup` üzerine sağ tıklayın, **Yeni > Anahtar** seçin ve `LabConfig` adını verin
6. `LabConfig` içinde aşağıdaki DWORD (32-bit) değerlerini oluşturun ve her birini **1** olarak ayarlayın:
   - `BypassTPMCheck`
   - `BypassSecureBootCheck`
   - `BypassRAMCheck`
   - `BypassCPUCheck`
7. Registry Düzenleyici'yi kapatın ve kuruluma devam edin

### Yöntem 3: Batch Script (Windows'ta)

Windows'tan çalıştırıyorsanız:

1. `bypass-installer.bat` dosyasına sağ tıklayın
2. **Yönetici olarak çalıştır** seçeneğini seçin
3. Ekrandaki talimatları izleyin
4. Windows 11 kurulumunu başlatın

---

## 🇬🇧 English Usage Guide

### ⚠️ Warning
Installing Windows 11 on unsupported hardware may result in lack of future updates or compatibility issues. Make sure you understand the risks before using these methods.

### Method 1: Using Registry File (Easy)

1. Boot your computer from Windows 11 USB installer
2. When you see "This PC can't run Windows 11" message, press **Shift + F10** to open Command Prompt
3. In Command Prompt, type `regedit` and press Enter
4. In Registry Editor, go to **File > Import** and import the `bypass-win11-requirements.reg` file
5. Close Registry Editor and Command Prompt
6. Continue with Windows 11 installation

### Method 2: Manual Registry Editing

1. Boot your computer from Windows 11 USB installer
2. At the system requirements warning screen, press **Shift + F10**
3. In Command Prompt, type `regedit` and press Enter
4. Navigate to: `HKEY_LOCAL_MACHINE\SYSTEM\Setup`
5. Right-click on `Setup`, select **New > Key**, and name it `LabConfig`
6. Inside `LabConfig`, create the following DWORD (32-bit) values and set each to **1**:
   - `BypassTPMCheck`
   - `BypassSecureBootCheck`
   - `BypassRAMCheck`
   - `BypassCPUCheck`
7. Close Registry Editor and continue with installation

### Method 3: Batch Script (On Windows)

If running from Windows:

1. Right-click on `bypass-installer.bat`
2. Select **Run as administrator**
3. Follow the on-screen instructions
4. Start Windows 11 installation

---

## 📁 Files Included / Dosyalar

- **bypass-win11-requirements.reg** - Registry file to import during setup / Kurulum sırasında içe aktarılacak registry dosyası
- **bypass-installer.bat** - Automated batch script / Otomatik batch scripti
- **README.md** - This file / Bu dosya

---

## 🔧 Technical Details / Teknik Detaylar

This tool modifies the following registry key:

```
HKEY_LOCAL_MACHINE\SYSTEM\Setup\LabConfig
```

With the following values:

- `BypassTPMCheck` = 1 (Disables TPM 2.0 requirement check)
- `BypassSecureBootCheck` = 1 (Disables Secure Boot requirement check)
- `BypassRAMCheck` = 1 (Disables RAM requirement check)
- `BypassCPUCheck` = 1 (Disables CPU compatibility check)

---

## 📝 System Requirements That Can Be Bypassed

- ✅ TPM 2.0 (Trusted Platform Module)
- ✅ Secure Boot
- ✅ CPU compatibility (8th gen Intel or 2nd gen AMD Ryzen)
- ✅ RAM requirements (4GB minimum)
- ✅ Storage requirements
- ✅ GPU compatibility (DirectX 12)

---

## ⚖️ Legal Disclaimer / Yasal Uyarı

**EN:** This tool is provided for educational and informational purposes only. Use at your own risk. The authors are not responsible for any damage or issues that may arise from using this tool. Microsoft recommends installing Windows 11 only on compatible hardware.

**TR:** Bu araç yalnızca eğitim ve bilgilendirme amaçlıdır. Kullanımı kendi sorumluluğunuzdadır. Yazarlar, bu aracın kullanımından kaynaklanabilecek herhangi bir hasar veya sorundan sorumlu değildir. Microsoft, Windows 11'i yalnızca uyumlu donanımda yüklemenizi önerir.

---

## 🤝 Contributing / Katkıda Bulunma

Feel free to submit issues or pull requests to improve this tool.

---

## 📄 License / Lisans

MIT License - Free to use and modify / Ücretsiz kullanım ve değiştirme

---

## 🌐 Resources / Kaynaklar

- [Microsoft Windows 11 Specifications](https://www.microsoft.com/windows/windows-11-specifications)
- [Tom's Hardware - How to Bypass Windows 11 TPM](https://www.tomshardware.com/how-to/bypass-windows-11-tpm-requirement)

---

**Made with ❤️ for the community / Topluluk için ❤️ ile yapıldı**