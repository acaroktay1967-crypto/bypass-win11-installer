# Windows 11 Installer Bypass / Windows 11 Yükleyici Gereksinimleri Atlama

Bu araç, Windows 11 kurulumu sırasında TPM 2.0, Secure Boot, RAM ve CPU gereksinimlerini atlamanıza olanak tanır.

This tool allows you to bypass TPM 2.0, Secure Boot, RAM, and CPU requirements during Windows 11 installation.

---

## 📥 Dosyaları Nasıl İndiririm? / How to Download Files?

### 🇹🇷 Türkçe - İndirme Talimatları

Bu repository'deki dosyaları bilgisayarınıza indirmek için 3 farklı yöntem kullanabilirsiniz:

#### Yöntem 1: ZIP Dosyası İndirme (En Kolay - Önerilen)

1. Bu sayfanın üst kısmında yeşil **"Code"** (Kod) butonuna tıklayın
2. Açılan menüden **"Download ZIP"** seçeneğine tıklayın
3. İndirilen `bypass-win11-installer-main.zip` dosyasını bilgisayarınızda bir klasöre çıkarın
4. Çıkarılan klasörde şu dosyaları bulacaksınız:
   - `bypass-win11-requirements.reg`
   - `bypass-installer.bat`
   - `setup-bypass.bat`
   - `README.md`
   - `INSTALLATION-GUIDE.md`

#### Yöntem 2: Git ile Klonlama (Gelişmiş Kullanıcılar için)

Eğer bilgisayarınızda Git yüklüyse:

**Genel Kullanım:**
```bash
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer
```

**Belirli Bir Klasöre Klonlama (Örnek: C:\Users\Oktay):**
```bash
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer
```

Bu komutlar repository'yi `C:\Users\Oktay\bypass-win11-installer` konumuna kopyalayacaktır.

#### Yöntem 3: Tek Dosya İndirme

Sadece belirli bir dosyaya ihtiyacınız varsa:

1. İndirmek istediğiniz dosyaya tıklayın (örn: `bypass-win11-requirements.reg`)
2. Sağ üstteki **"Raw"** (Ham) butonuna tıklayın
3. Sayfada **sağ tıklayıp** "Farklı Kaydet" veya "Save As" seçeneğini seçin
4. Dosyayı bilgisayarınıza kaydedin

**💡 İpucu:** Çoğu kullanıcı için en kolay yöntem **Yöntem 1** (ZIP indirme) dir.

---

### 🇬🇧 English - Download Instructions

You can download the files from this repository to your computer using 3 different methods:

#### Method 1: Download ZIP (Easiest - Recommended)

1. Click the green **"Code"** button at the top of this page
2. Select **"Download ZIP"** from the dropdown menu
3. Extract the downloaded `bypass-win11-installer-main.zip` file to a folder on your computer
4. In the extracted folder, you will find:
   - `bypass-win11-requirements.reg`
   - `bypass-installer.bat`
   - `setup-bypass.bat`
   - `README.md`
   - `INSTALLATION-GUIDE.md`

#### Method 2: Clone with Git (For Advanced Users)

If you have Git installed on your computer:

**General Usage:**
```bash
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer
```

**Clone to a Specific Folder (Example: C:\Users\Oktay):**
```bash
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer
```

These commands will copy the repository to `C:\Users\Oktay\bypass-win11-installer`.

#### Method 3: Download Individual Files

If you only need a specific file:

1. Click on the file you want to download (e.g., `bypass-win11-requirements.reg`)
2. Click the **"Raw"** button in the top right
3. **Right-click** on the page and select "Save As"
4. Save the file to your computer

**💡 Tip:** For most users, **Method 1** (ZIP download) is the easiest approach.

**📖 Detaylı İndirme Rehberi / Detailed Download Guide:** Daha fazla bilgi için [DOWNLOAD-GUIDE.md](DOWNLOAD-GUIDE.md) dosyasına bakın / For more information, see [DOWNLOAD-GUIDE.md](DOWNLOAD-GUIDE.md)

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

### Yöntem 4: PowerShell Script (Önerilen - Gelişmiş)

PowerShell scripti daha fazla bilgi ve renklendirme sağlar:

1. `bypass-installer.ps1` dosyasına sağ tıklayın
2. **PowerShell ile çalıştır** veya **Yönetici olarak çalıştır** seçin
3. Komut satırında şunu yazabilirsiniz:
   ```powershell
   powershell -ExecutionPolicy Bypass -File bypass-installer.ps1
   ```
4. Ekrandaki talimatları izleyin

**Not:** 4GB RAM'li bilgisayarlar için özel olarak optimize edilmiştir.

### Yöntem 5: Python Script (Çapraz Platform)

Python yüklüyse (3.6 veya üzeri):

1. Komut İstemi'ni **Yönetici olarak çalıştır**
2. Script klasörüne gidin:
   ```bash
   cd bypass-win11-installer
   ```
3. Python scriptini çalıştırın:
   ```bash
   python bypass-installer.py
   ```
4. Ekrandaki talimatları izleyin

**Özellikler:**
- ✅ 4GB RAM desteği
- ✅ Renkli terminal çıktısı
- ✅ Detaylı hata mesajları
- ✅ Otomatik yönetici kontrolü

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

### Method 4: PowerShell Script (Recommended - Advanced)

PowerShell script provides more information and colored output:

1. Right-click on `bypass-installer.ps1`
2. Select **Run with PowerShell** or **Run as administrator**
3. Or run from command line:
   ```powershell
   powershell -ExecutionPolicy Bypass -File bypass-installer.ps1
   ```
4. Follow the on-screen instructions

**Note:** Specially optimized for computers with 4GB RAM.

### Method 5: Python Script (Cross-Platform)

If you have Python installed (3.6 or higher):

1. Open Command Prompt **as Administrator**
2. Navigate to the script folder:
   ```bash
   cd bypass-win11-installer
   ```
3. Run the Python script:
   ```bash
   python bypass-installer.py
   ```
4. Follow the on-screen instructions

**Features:**
- ✅ 4GB RAM support
- ✅ Colored terminal output
- ✅ Detailed error messages
- ✅ Automatic administrator check

---

## 📁 Files Included / Dosyalar

- **bypass-win11-requirements.reg** - Registry file to import during setup / Kurulum sırasında içe aktarılacak registry dosyası
- **bypass-installer.bat** - Automated batch script / Otomatik batch scripti
- **bypass-installer.ps1** - PowerShell script with enhanced features / Gelişmiş özelliklerle PowerShell scripti
- **bypass-installer.py** - Python script (cross-platform) / Python scripti (çapraz platform)
- **setup-bypass.bat** - Advanced setup script for Windows PE / Windows PE için gelişmiş kurulum scripti
- **README.md** - This file / Bu dosya
- **INSTALLATION-GUIDE.md** - Detailed installation guide / Detaylı kurulum rehberi
- **DOWNLOAD-GUIDE.md** - How to download files / Dosyaları nasıl indireceğiniz hakkında rehber

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