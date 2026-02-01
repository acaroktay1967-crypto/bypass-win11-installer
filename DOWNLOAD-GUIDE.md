# 📥 İndirme Rehberi / Download Guide

Bu doküman, repository'deki dosyaları bilgisayarınıza nasıl indireceğinizi adım adım açıklar.

This document explains step-by-step how to download files from this repository to your computer.

---

## 🇹🇷 TÜRKÇE REHBERİ

### Genel Bakış

Bu repository, Windows 11 kurulum gereksinimlerini atlamanız için gerekli araçları içerir. Dosyaları kullanabilmek için önce bilgisayarınıza indirmeniz gerekir.

### Hangi Yöntemi Seçmeliyim?

| Yöntem | Kim İçin | Zorluk | Önerilen |
|--------|----------|---------|----------|
| **ZIP İndirme** | Herkes için | ⭐ Çok Kolay | ✅ Evet |
| **Git Clone** | Geliştiriciler | ⭐⭐ Orta | Opsiyonel |
| **Tek Dosya** | Belirli dosya gerekiyorsa | ⭐⭐ Orta | Duruma Göre |

### 📦 Yöntem 1: ZIP Dosyası İndirme (ÖNERİLEN)

Bu, dosyaları indirmenin en kolay ve en hızlı yoludur.

#### Adım 1: GitHub Sayfasına Gidin
- Tarayıcınızda şu adresi açın: https://github.com/acaroktay1967-crypto/bypass-win11-installer

#### Adım 2: Code Butonuna Tıklayın
- Sayfanın sağ üst kısmında (dosya listesinin üzerinde) yeşil **"<> Code"** yazan butonu bulun
- Bu butona tıklayın

#### Adım 3: Download ZIP Seçin
- Açılan küçük pencerede en altta **"Download ZIP"** seçeneğini göreceksiniz
- Bu seçeneğe tıklayın
- Tarayıcınız `bypass-win11-installer.zip` veya `bypass-win11-installer-copilot-win11-yukleme.zip` isimli bir dosya indirecek

#### Adım 4: ZIP Dosyasını Çıkarın
1. İndirilen ZIP dosyasını bulun (genellikle "İndirilenler" klasöründe)
2. ZIP dosyasına **sağ tıklayın**
3. **"Tümünü ayıkla"** veya **"Extract All"** seçeneğini seçin
4. Dosyaları çıkarmak istediğiniz konumu seçin
5. **"Ayıkla"** veya **"Extract"** butonuna tıklayın

#### Adım 5: Dosyaları Kontrol Edin
Çıkarılan klasörde şu dosyaları görmelisiniz:
- ✅ `bypass-win11-requirements.reg` - Registry dosyası
- ✅ `bypass-installer.bat` - Windows için batch scripti
- ✅ `setup-bypass.bat` - Kurulum sırasında kullanılacak script
- ✅ `README.md` - Kullanım talimatları
- ✅ `INSTALLATION-GUIDE.md` - Detaylı kurulum rehberi

#### Adım 6: USB'ye Kopyalayın (Opsiyonel)
Eğer Windows 11 kurulumu sırasında kullanacaksanız:
1. Boş bir USB bellek takın
2. Çıkardığınız dosyaları USB belleğe kopyalayın
3. USB'yi Windows 11 kurulum USB'nizle birlikte hazır bulundurun

### 💻 Yöntem 2: Git ile Klonlama

Bu yöntem, Git programını kullanmayı bilen kullanıcılar içindir.

#### Ön Gereksinimler
- Bilgisayarınızda Git yüklü olmalı
- Git'i indirmek için: https://git-scm.com/downloads

#### Adımlar

1. **Komut İstemi veya Terminal Açın**
   - Windows: `Win + R` → `cmd` yazın → Enter
   - veya PowerShell açın

2. **Klonlamak İstediğiniz Dizine Gidin**
   
   **Örnek 1: Masaüstüne klonlama**
   ```bash
   cd C:\Users\KullaniciAdiniz\Desktop
   ```
   
   **Örnek 2: C:\Users\Oktay klasörüne klonlama**
   ```bash
   cd C:\Users\Oktay
   ```
   
   **Not:** Eğer klasör yoksa, önce oluşturun:
   ```bash
   mkdir C:\Users\Oktay
   cd C:\Users\Oktay
   ```

3. **Repository'yi Klonlayın**
   ```bash
   git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
   ```
   
   Bu komut `bypass-win11-installer` adında bir klasör oluşturacak ve tüm dosyaları oraya kopyalayacaktır.
   
   **Örnek:** `C:\Users\Oktay` içindeyseniz, dosyalar `C:\Users\Oktay\bypass-win11-installer` konumuna kopyalanır.

4. **Klasöre Girin**
   ```bash
   cd bypass-win11-installer
   ```

5. **Dosyaları Listeleyin**
   ```bash
   dir
   ```
   
   Şu dosyaları görmelisiniz:
   - bypass-win11-requirements.reg
   - bypass-installer.bat
   - bypass-installer.ps1
   - bypass-installer.py
   - setup-bypass.bat
   - README.md
   - INSTALLATION-GUIDE.md
   - DOWNLOAD-GUIDE.md

#### Tam Örnek: C:\Users\Oktay'a Klonlama

Tüm işlem adımları:

```bash
# 1. Klasörü oluştur (eğer yoksa)
mkdir C:\Users\Oktay

# 2. Klasöre git
cd C:\Users\Oktay

# 3. Repository'yi klonla
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git

# 4. Klonlanan klasöre gir
cd bypass-win11-installer

# 5. Dosyaları listele ve kontrol et
dir
```

Sonuç: Dosyalar `C:\Users\Oktay\bypass-win11-installer\` konumunda olacaktır.

#### Git'in Avantajları
- Güncellemeleri kolayca çekebilirsiniz: `git pull`
- Değişiklikleri takip edebilirsiniz
- Farklı dalları (branches) görebilirsiniz

### 📄 Yöntem 3: Tek Tek Dosya İndirme

Sadece belirli dosyalara ihtiyacınız varsa bu yöntemi kullanın.

#### Örnek: bypass-win11-requirements.reg Dosyasını İndirme

1. **GitHub Sayfasında Dosyaya Gidin**
   - Ana sayfada `bypass-win11-requirements.reg` dosyasına tıklayın

2. **Raw Görünümünü Açın**
   - Sağ üstte **"Raw"** butonunu bulun
   - Bu butona tıklayın
   - Tarayıcı dosyanın içeriğini gösterecek

3. **Dosyayı Kaydedin**
   - Sayfada **sağ tıklayın**
   - **"Farklı Kaydet"** veya **"Save Page As"** seçin
   - Dosya adını kontrol edin: `bypass-win11-requirements.reg`
   - Dosya türünün `.reg` olduğundan emin olun (`.txt` değil!)
   - **"Kaydet"** butonuna tıklayın

#### Diğer Dosyalar İçin
Aynı işlemi diğer dosyalar için tekrarlayın:
- `bypass-installer.bat`
- `setup-bypass.bat`

**⚠️ ÖNEMLİ:** Dosyaları kaydederken uzantılarının değişmediğinden emin olun!

### 🔍 Sorun Giderme

#### "ZIP dosyası açılmıyor"
- Windows 10/11'de yerleşik ZIP desteği vardır
- Sağ tık → "Tümünü Ayıkla" kullanın
- Alternatif: 7-Zip veya WinRAR kullanabilirsiniz

#### "Dosyalar indirildikten sonra kayboldu"
- İndirilenler klasörünü kontrol edin: `C:\Users\KullaniciAdiniz\Downloads`
- Tarayıcınızın indirme geçmişine bakın (Ctrl+J)

#### "Git komutu tanınmıyor"
- Git'i yüklemeniz gerekir: https://git-scm.com/downloads
- Kurulumdan sonra terminal/komut istemini yeniden başlatın

#### "USB'ye kopyalarken hata alıyorum"
- USB'nin yazma korumalı olmadığından emin olun
- USB'de yeterli alan olduğunu kontrol edin (en az 10 MB)
- USB'yi FAT32 veya NTFS olarak formatlamayı deneyin

### 📱 Mobil Cihazlardan İndirme

GitHub'ı mobil cihazdan kullanıyorsanız:

1. GitHub sayfasını mobil tarayıcıda açın
2. Sağ üstten menüyü açın (⋮)
3. "Masaüstü sitesi" veya "Desktop site" seçeneğini aktifleştirin
4. Yukarıdaki yöntemlerden birini kullanın

### ✅ İndirme Sonrası Ne Yapmalı?

1. **Dosyaları Kontrol Edin**
   - Tüm dosyaların düzgün indirildiğinden emin olun
   - Dosya boyutlarını kontrol edin (çok küçükse sorun olabilir)

2. **README.md'yi Okuyun**
   - Kullanım talimatlarını öğrenmek için README dosyasını açın
   - Hangi yöntemi kullanacağınıza karar verin

3. **INSTALLATION-GUIDE.md'ye Göz Atın**
   - Detaylı kurulum adımları için bu rehberi okuyun

4. **Dosyaları Güvenli Tutun**
   - İndirilen dosyaları kolay bulabileceğiniz bir yere kaydedin
   - Yedek kopya oluşturabilirsiniz

### 🎯 Önerilen İş Akışı

İşte önerilen adım adım süreç:

```
1. ZIP dosyasını indirin
   ↓
2. Masaüstünde veya Belgeler'de bir klasöre çıkarın
   ↓
3. README.md dosyasını okuyun
   ↓
4. İhtiyacınız olan dosyaları USB'ye kopyalayın
   ↓
5. Windows 11 kurulumu sırasında kullanın
```

---

## 🇬🇧 ENGLISH GUIDE

### Overview

This repository contains the necessary tools to bypass Windows 11 installation requirements. To use the files, you first need to download them to your computer.

### Which Method Should I Choose?

| Method | For Whom | Difficulty | Recommended |
|--------|----------|------------|-------------|
| **ZIP Download** | Everyone | ⭐ Very Easy | ✅ Yes |
| **Git Clone** | Developers | ⭐⭐ Medium | Optional |
| **Single File** | Specific file needed | ⭐⭐ Medium | Case by case |

### 📦 Method 1: ZIP File Download (RECOMMENDED)

This is the easiest and fastest way to download the files.

#### Step 1: Go to GitHub Page
- Open this URL in your browser: https://github.com/acaroktay1967-crypto/bypass-win11-installer

#### Step 2: Click the Code Button
- Find the green **"<> Code"** button in the top right (above the file list)
- Click this button

#### Step 3: Select Download ZIP
- In the small popup window, you'll see **"Download ZIP"** at the bottom
- Click this option
- Your browser will download a file named `bypass-win11-installer.zip` or `bypass-win11-installer-copilot-win11-yukleme.zip`

#### Step 4: Extract the ZIP File
1. Locate the downloaded ZIP file (usually in "Downloads" folder)
2. **Right-click** on the ZIP file
3. Select **"Extract All"**
4. Choose where you want to extract the files
5. Click the **"Extract"** button

#### Step 5: Verify Files
In the extracted folder, you should see:
- ✅ `bypass-win11-requirements.reg` - Registry file
- ✅ `bypass-installer.bat` - Batch script for Windows
- ✅ `setup-bypass.bat` - Script for use during installation
- ✅ `README.md` - Usage instructions
- ✅ `INSTALLATION-GUIDE.md` - Detailed installation guide

#### Step 6: Copy to USB (Optional)
If using during Windows 11 installation:
1. Insert a blank USB drive
2. Copy the extracted files to the USB drive
3. Keep the USB ready with your Windows 11 installation USB

### 💻 Method 2: Clone with Git

This method is for users familiar with Git.

#### Prerequisites
- Git must be installed on your computer
- Download Git: https://git-scm.com/downloads

#### Steps

1. **Open Command Prompt or Terminal**
   - Windows: `Win + R` → type `cmd` → Enter
   - or open PowerShell

2. **Navigate to Desired Directory**
   
   **Example 1: Clone to Desktop**
   ```bash
   cd C:\Users\YourUsername\Desktop
   ```
   
   **Example 2: Clone to C:\Users\Oktay folder**
   ```bash
   cd C:\Users\Oktay
   ```
   
   **Note:** If the folder doesn't exist, create it first:
   ```bash
   mkdir C:\Users\Oktay
   cd C:\Users\Oktay
   ```

3. **Clone the Repository**
   ```bash
   git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
   ```
   
   This command will create a folder named `bypass-win11-installer` and copy all files there.
   
   **Example:** If you're in `C:\Users\Oktay`, files will be copied to `C:\Users\Oktay\bypass-win11-installer`.

4. **Enter the Folder**
   ```bash
   cd bypass-win11-installer
   ```

5. **List Files**
   ```bash
   dir
   ```
   
   You should see:
   - bypass-win11-requirements.reg
   - bypass-installer.bat
   - bypass-installer.ps1
   - bypass-installer.py
   - setup-bypass.bat
   - README.md
   - INSTALLATION-GUIDE.md
   - DOWNLOAD-GUIDE.md

#### Complete Example: Cloning to C:\Users\Oktay

All steps together:

```bash
# 1. Create folder (if it doesn't exist)
mkdir C:\Users\Oktay

# 2. Navigate to folder
cd C:\Users\Oktay

# 3. Clone repository
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git

# 4. Enter cloned folder
cd bypass-win11-installer

# 5. List and verify files
dir
```

Result: Files will be located at `C:\Users\Oktay\bypass-win11-installer\`.

#### Git Advantages
- Easily pull updates: `git pull`
- Track changes
- View different branches

### 📄 Method 3: Download Individual Files

Use this method if you only need specific files.

#### Example: Downloading bypass-win11-requirements.reg

1. **Navigate to File on GitHub**
   - Click on `bypass-win11-requirements.reg` on the main page

2. **Open Raw View**
   - Find the **"Raw"** button in the top right
   - Click this button
   - Browser will show the file contents

3. **Save the File**
   - **Right-click** on the page
   - Select **"Save As"**
   - Check filename: `bypass-win11-requirements.reg`
   - Ensure file type is `.reg` (not `.txt`!)
   - Click **"Save"**

#### For Other Files
Repeat the same process for other files:
- `bypass-installer.bat`
- `setup-bypass.bat`

**⚠️ IMPORTANT:** Ensure file extensions don't change when saving!

### 🔍 Troubleshooting

#### "ZIP file won't open"
- Windows 10/11 has built-in ZIP support
- Use Right-click → "Extract All"
- Alternative: Use 7-Zip or WinRAR

#### "Files disappeared after downloading"
- Check Downloads folder: `C:\Users\YourUsername\Downloads`
- Check browser download history (Ctrl+J)

#### "Git command not recognized"
- You need to install Git: https://git-scm.com/downloads
- Restart terminal/command prompt after installation

#### "Error copying to USB"
- Ensure USB is not write-protected
- Check USB has enough space (at least 10 MB)
- Try formatting USB as FAT32 or NTFS

### 📱 Downloading from Mobile Devices

If using GitHub on a mobile device:

1. Open GitHub page in mobile browser
2. Open menu from top right (⋮)
3. Enable "Desktop site" option
4. Use one of the methods above

### ✅ What to Do After Download?

1. **Verify Files**
   - Ensure all files downloaded properly
   - Check file sizes (if too small, there may be an issue)

2. **Read README.md**
   - Open README file to learn usage instructions
   - Decide which method to use

3. **Review INSTALLATION-GUIDE.md**
   - Read this guide for detailed installation steps

4. **Keep Files Safe**
   - Save downloaded files in an easy-to-find location
   - Create a backup copy if needed

### 🎯 Recommended Workflow

Here's the recommended step-by-step process:

```
1. Download ZIP file
   ↓
2. Extract to a folder on Desktop or Documents
   ↓
3. Read README.md
   ↓
4. Copy needed files to USB
   ↓
5. Use during Windows 11 installation
```

---

## 🆘 Need More Help? / Daha Fazla Yardım mı Gerekiyor?

### 🇹🇷 Türkçe
Sorunlarınız devam ediyorsa:
- GitHub'da bir Issue açın
- README.md dosyasındaki talimatları tekrar okuyun
- INSTALLATION-GUIDE.md'deki SSS bölümüne bakın

### 🇬🇧 English
If you're still having issues:
- Open an Issue on GitHub
- Re-read the instructions in README.md
- Check the FAQ section in INSTALLATION-GUIDE.md

---

**Son Güncelleme / Last Updated:** Şubat 2026 / February 2026
**Versiyon / Version:** 1.1
