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
   
   PowerShell için (önerilen - hata vermez):
   ```powershell
   New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force
   cd C:\Users\Oktay
   ```
   
   Komut İstemi (CMD) için:
   ```batch
   mkdir C:\Users\Oktay 2>nul
   cd C:\Users\Oktay
   ```
   
   Not: `mkdir` komutu klasör varsa hata verir, bu normaldir ve göz ardı edilebilir.

3. **Repository'yi Klonlayın**
   ```bash
   git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
   ```
   
   Bu komut `bypass-win11-installer` adında bir klasör oluşturacak ve tüm dosyaları oraya kopyalayacaktır.
   
   **Not:** Eğer "destination path already exists" hatası alırsanız, repository zaten klonlanmış demektir. Güncellemek için:
   ```bash
   cd bypass-win11-installer
   git pull
   ```
   
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

Tüm işlem adımları (PowerShell için):

```powershell
# 1. Klasörü oluştur (eğer yoksa) - hata vermez
New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force

# 2. Klasöre git
cd C:\Users\Oktay

# 3. Repository'yi klonla (eğer zaten klonlanmışsa, güncelle)
if (Test-Path "bypass-win11-installer") {
    Write-Host "Repository zaten mevcut. Güncelleniyor..."
    cd bypass-win11-installer
    git pull
} else {
    Write-Host "Repository klonlanıyor..."
    git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
    cd bypass-win11-installer
}

# 4. Dosyaları listele ve kontrol et
dir
```

**Basit Versiyon (tek satırlar):**
```powershell
# Klasör oluştur (hata vermez)
New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force | Out-Null

# Klasöre git ve klonla
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git 2>$null || (cd bypass-win11-installer; git pull)
cd bypass-win11-installer
dir
```

**Komut İstemi (CMD) için:**
```batch
REM Klasör oluştur (hata mesajı göz ardı edilir)
mkdir C:\Users\Oktay 2>nul

REM Klasöre git
cd C:\Users\Oktay

REM Repository'yi klonla veya güncelle
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git 2>nul || cd bypass-win11-installer && git pull

REM Klasöre gir
cd bypass-win11-installer

REM Dosyaları listele
dir
```

Sonuç: Dosyalar `C:\Users\Oktay\bypass-win11-installer\` konumunda olacaktır.

#### ⚠️ Sık Karşılaşılan Hatalar ve Çözümleri

**Hata 1: "An item with the specified name already exists"**
```
mkdir : An item with the specified name C:\Users\Oktay already exists.
```
**Çözüm:** Klasör zaten var, bu normaldir. Bu hatayı görmezden gelebilir veya PowerShell'de `New-Item -Force` kullanabilirsiniz:
```powershell
New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force
```

**Hata 2: "destination path already exists and is not an empty directory"**
```
fatal: destination path 'bypass-win11-installer' already exists and is not an empty directory.
```
**Çözüm:** Repository zaten klonlanmış. Güncellemek için:
```powershell
cd C:\Users\Oktay\bypass-win11-installer
git pull
```

Veya yeniden klonlamak için önce silin:
```powershell
cd C:\Users\Oktay
Remove-Item -Path "bypass-win11-installer" -Recurse -Force
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
```

#### Git'in Avantajları
- Güncellemeleri kolayca çekebilirsiniz: `git pull`
- Değişiklikleri takip edebilirsiniz
- Farklı dalları (branches) görebilirsiniz

#### 🗑️ Repository'yi Silme (Temizleme)

Eğer klonlanmış repository'yi tamamen silmek isterseniz:

**Yöntem 1: PowerShell ile Silme (Önerilen)**
```powershell
# Klasörü tamamen sil
cd C:\Users\Oktay
Remove-Item -Path "bypass-win11-installer" -Recurse -Force

# Veya tam yol ile
Remove-Item -Path "C:\Users\Oktay\bypass-win11-installer" -Recurse -Force
```

**Yöntem 2: Komut İstemi (CMD) ile Silme**
```batch
REM Klasörü tamamen sil
cd C:\Users\Oktay
rmdir /s /q bypass-win11-installer

REM Veya tam yol ile
rmdir /s /q "C:\Users\Oktay\bypass-win11-installer"
```

**Yöntem 3: Windows Explorer ile Silme**
1. Dosya Gezgini'ni açın
2. `C:\Users\Oktay\bypass-win11-installer` klasörüne gidin
3. Klasöre **sağ tıklayın**
4. **"Sil"** veya **"Delete"** seçeneğini seçin
5. Onay penceresinde **"Evet"** butonuna tıklayın

**Yöntem 4: Mobil Cihazdan (iPhone/Android) Silme**
Eğer dosyaları mobil cihazınıza indirdiyseniz:
1. Dosya yöneticisi uygulamasını açın (Dosyalar/Files)
2. İndirilenler (Downloads) klasörüne gidin
3. `bypass-win11-installer` klasörünü bulun
4. Uzun basın ve **"Sil"** seçeneğini seçin

**⚠️ Uyarı:**
- Bu işlem geri alınamaz! Klasör Geri Dönüşüm Kutusu'na gider.
- Klasör içinde değişiklik yaptıysanız, önce yedek alın.
- Silme işlemi birkaç saniye sürebilir (dosya sayısına bağlı).

#### ♻️ Silme Sonrası: Temiz Başlangıç

Repository'yi sildiyseniz (tebrikler, temiz başlangıç! 🎉), şimdi ne yapmalısınız:

**Senaryo 1: Yeniden Klonlamak İstiyorsanız**
```powershell
# Temiz klonlama
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer

# Dosyaları kontrol et
dir
```

**Senaryo 2: ZIP Dosyası İndirmek İstiyorsanız**
Eğer Git kullanmak istemiyorsanız, GitHub'dan doğrudan ZIP indirebilirsiniz:
1. [Repository sayfasına](https://github.com/acaroktay1967-crypto/bypass-win11-installer) gidin
2. Yeşil **"Code"** butonuna tıklayın
3. **"Download ZIP"** seçeneğini seçin
4. İndirilen ZIP'i `C:\Users\Oktay` konumuna çıkarın

**Senaryo 3: Sadece İhtiyacınız Olan Dosyaları İndirin**
Tüm repository yerine sadece ihtiyacınız olan bypass dosyalarını indirebilirsiniz:
- `bypass-win11-requirements.reg`
- `bypass-installer.ps1`
- `bypass-installer.bat`

(Detaylar için aşağıdaki "Tek Tek Dosya İndirme" bölümüne bakın)

**💡 İpuçları:**
- **Sık güncelleme yapılıyorsa:** Git clone kullanın (kolay güncelleme)
- **Tek seferlik kullanım:** ZIP indirin (daha basit)
- **Minimalist yaklaşım:** Sadece gerekli dosyaları indirin
- **Mobil cihazdan:** ZIP indirin veya GitHub mobil uygulamasını kullanın

**📱 iPhone/Mobil Cihazlardan İndirme:**
Eğer iPhone veya başka mobil cihazdan indirdiyseniz:
1. Dosyaları bilgisayara aktarın (AirDrop, kablo, bulut depolama)
2. Veya GitHub Desktop uygulamasını kullanın
3. Veya doğrudan ZIP indirip USB ile aktarın

**✅ Silme İşlemi Tamamlandı mı?**
Silme işlemini başarıyla tamamladıysanız:
- ✓ Geri Dönüşüm Kutusu'nu boşaltabilirsiniz (kalıcı silme için)
- ✓ Yeni klonlama/indirme için yukarıdaki seçeneklerden birini kullanın
- ✓ USB kurulum için Rufus rehberine geçebilirsiniz (INSTALLATION-GUIDE.md)

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

#### 📋 ADIM 1: Dosya Kontrolü - ÇOK ÖNEMLİ!

**Olması Gereken Dosyalar:**

```
bypass-win11-installer\
├── 📄 README.md                          (yaklaşık 16 KB)
├── 📄 DOWNLOAD-GUIDE.md                  (yaklaşık 25 KB)
├── 📄 INSTALLATION-GUIDE.md              (yaklaşık 26 KB)
├── 📄 bypass-win11-requirements.reg      (yaklaşık 217 bytes)
├── 📄 bypass-installer.bat               (yaklaşık 1.2 KB)
├── 📄 bypass-installer.ps1               (yaklaşık 6 KB)
├── 📄 bypass-installer.py                (yaklaşık 9 KB)
└── 📄 setup-bypass.bat                   (yaklaşık 2.3 KB)
```

**✅ TOPLAM: 8 dosya olmalı!**

**Dosya Sayısı Kontrolü (PowerShell):**
```powershell
cd C:\Users\Oktay\bypass-win11-installer
(Get-ChildItem -File).Count
# Sonuç: 8 göstermeli!
```

**Dosya Sayısı Kontrolü (CMD):**
```cmd
cd C:\Users\Oktay\bypass-win11-installer
dir /b /a-d | find /c /v ""
REM Sonuç: 8 göstermeli!
```

#### 🚨 Sadece 2-3 Dosya mı Görüyorsunuz?

Eğer klasörde sadece birkaç dosya varsa (örneğin sadece `bypass_win11.py` ve `README.md`):

**Muhtemel Nedenler:**
1. 🔸 Eski bir commit/branch indirdiniz
2. 🔸 Repository tam yüklenmedi
3. 🔸 Yanlış klasöre bakıyorsunuz
4. 🔸 Git pull yapmadınız

**Çözüm 1: Git ile Güncelleme (Hızlı)**

```powershell
cd C:\Users\Oktay\bypass-win11-installer
git pull origin main
Get-ChildItem
```

**Çözüm 2: Doğru Branch'e Geçin**

```powershell
cd C:\Users\Oktay\bypass-win11-installer
git branch              # Mevcut branch'i görün
git checkout main       # Ana branch'e geçin
git pull                # Güncellemeleri çekin
Get-ChildItem           # Dosyaları listeleyin
```

**Çözüm 3: Yeniden İndirin (En Garanti)**

1. Eski klasörü silin:
```powershell
Remove-Item -Recurse -Force C:\Users\Oktay\bypass-win11-installer
```

2. ZIP olarak yeniden indirin:
   - GitHub sayfasında yeşil **"Code"** butonuna tıklayın
   - **"Download ZIP"** seçeneğini seçin
   - İndirin ve çıkartın
   - 8 dosya olduğunu doğrulayın

3. Veya tekrar klonlayın:
```powershell
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer
(Get-ChildItem -File).Count  # 8 olmalı
```

**Çözüm 4: Klasör Konumu Kontrolü**

Doğru klasörde olduğunuzdan emin olun:

```powershell
# Bulunduğunuz konumu göster
pwd

# Eğer "bypass-win11-installer" içindeyseniz ve hala eksikse,
# yukarıdaki Çözüm 3'ü deneyin
```

#### ADIM 2: Dosya Boyutlarını Kontrol Edin

Dosyalar çok küçükse (birkaç byte), indirme başarısız olmuş olabilir:

```powershell
Get-ChildItem | Format-Table Name, Length
```

Eğer tüm dosyalar çok küçükse (< 100 byte), yeniden indirin.

#### ADIM 3: README.md'yi Okuyun

1. **README.md'yi Açın**
   - Kullanım talimatlarını öğrenmek için okuyun
   - Hangi yöntemi kullanacağınıza karar verin

#### ADIM 4: INSTALLATION-GUIDE.md'ye Göz Atın

1. **Detaylı Kurulum Adımları**
   - Rufus kullanımı
   - USB oluşturma
   - Kurulum sırasında bypass dosyalarını kullanma

#### ADIM 5: Dosyaları Güvenli Tutun

1. **Kolay Erişilebilir Bir Yerde Saklayın**
   - `C:\Users\Oktay\bypass-win11-installer\` önerilen konum
   - Masaüstü veya Belgeler de olabilir

2. **Yedek Kopya Oluşturun (Önerilen)**
   ```powershell
   Copy-Item -Path "C:\Users\Oktay\bypass-win11-installer" -Destination "C:\Users\Oktay\bypass-win11-installer-backup" -Recurse
   ```

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
   
   PowerShell (recommended - won't error):
   ```powershell
   New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force
   cd C:\Users\Oktay
   ```
   
   Command Prompt (CMD):
   ```batch
   mkdir C:\Users\Oktay 2>nul
   cd C:\Users\Oktay
   ```
   
   Note: `mkdir` will error if folder exists, this is normal and can be ignored.

3. **Clone the Repository**
   ```bash
   git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
   ```
   
   This command will create a folder named `bypass-win11-installer` and copy all files there.
   
   **Example:** If you're in `C:\Users\Oktay`, files will be copied to `C:\Users\Oktay\bypass-win11-installer`.
   
   **Note:** If you get "destination path already exists" error, the repository is already cloned. To update:
   ```bash
   cd bypass-win11-installer
   git pull
   ```

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

All steps together (PowerShell):

```powershell
# 1. Create folder (if it doesn't exist) - won't error
New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force

# 2. Navigate to folder
cd C:\Users\Oktay

# 3. Clone repository (if already cloned, update it)
if (Test-Path "bypass-win11-installer") {
    Write-Host "Repository already exists. Updating..."
    cd bypass-win11-installer
    git pull
} else {
    Write-Host "Cloning repository..."
    git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
    cd bypass-win11-installer
}

# 4. List and verify files
dir
```

**Simple Version (one-liners):**
```powershell
# Create folder (won't error)
New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force | Out-Null

# Navigate and clone
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git 2>$null || (cd bypass-win11-installer; git pull)
cd bypass-win11-installer
dir
```

**Command Prompt (CMD):**
```batch
REM Create folder (error message ignored)
mkdir C:\Users\Oktay 2>nul

REM Navigate to folder
cd C:\Users\Oktay

REM Clone or update repository
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git 2>nul || cd bypass-win11-installer && git pull

REM Enter folder
cd bypass-win11-installer

REM List files
dir
```

Result: Files will be located at `C:\Users\Oktay\bypass-win11-installer\`.

#### ⚠️ Common Errors and Solutions

**Error 1: "An item with the specified name already exists"**
```
mkdir : An item with the specified name C:\Users\Oktay already exists.
```
**Solution:** Folder already exists, this is normal. You can ignore this error or use PowerShell with `-Force`:
```powershell
New-Item -Path "C:\Users\Oktay" -ItemType Directory -Force
```

**Error 2: "destination path already exists and is not an empty directory"**
```
fatal: destination path 'bypass-win11-installer' already exists and is not an empty directory.
```
**Solution:** Repository already cloned. To update:
```powershell
cd C:\Users\Oktay\bypass-win11-installer
git pull
```

Or to re-clone, delete first:
```powershell
cd C:\Users\Oktay
Remove-Item -Path "bypass-win11-installer" -Recurse -Force
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
```

Result: Files will be located at `C:\Users\Oktay\bypass-win11-installer\`.

#### Git Advantages
- Easily pull updates: `git pull`
- Track changes
- View different branches

#### 🗑️ Deleting Repository (Cleanup)

If you want to completely delete the cloned repository:

**Method 1: Delete with PowerShell (Recommended)**
```powershell
# Delete folder completely
cd C:\Users\Oktay
Remove-Item -Path "bypass-win11-installer" -Recurse -Force

# Or with full path
Remove-Item -Path "C:\Users\Oktay\bypass-win11-installer" -Recurse -Force
```

**Method 2: Delete with Command Prompt (CMD)**
```batch
REM Delete folder completely
cd C:\Users\Oktay
rmdir /s /q bypass-win11-installer

REM Or with full path
rmdir /s /q "C:\Users\Oktay\bypass-win11-installer"
```

**Method 3: Delete with Windows Explorer**
1. Open File Explorer
2. Navigate to `C:\Users\Oktay\bypass-win11-installer`
3. **Right-click** on the folder
4. Select **"Delete"**
5. Click **"Yes"** in the confirmation dialog

**Method 4: Delete from Mobile Device (iPhone/Android)**
If you downloaded files to your mobile device:
1. Open File Manager app (Files)
2. Go to Downloads folder
3. Find `bypass-win11-installer` folder
4. Long press and select **"Delete"**

**⚠️ Warning:**
- This action cannot be undone! Folder goes to Recycle Bin.
- If you made changes in the folder, backup first.
- Deletion may take a few seconds (depends on file count).

#### ♻️ After Deletion: Fresh Start

If you deleted the repository (congrats on a fresh start! 🎉), here's what to do next:

**Scenario 1: Want to Clone Again**
```powershell
# Clean clone
cd C:\Users\Oktay
git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git
cd bypass-win11-installer

# Verify files
dir
```

**Scenario 2: Want to Download ZIP Instead**
If you don't want to use Git, download ZIP directly from GitHub:
1. Go to [repository page](https://github.com/acaroktay1967-crypto/bypass-win11-installer)
2. Click the green **"Code"** button
3. Select **"Download ZIP"**
4. Extract ZIP to `C:\Users\Oktay`

**Scenario 3: Download Only Files You Need**
Instead of the entire repository, download only the bypass files you need:
- `bypass-win11-requirements.reg`
- `bypass-installer.ps1`
- `bypass-installer.bat`

(See "Download Individual Files" section below for details)

**💡 Tips:**
- **Frequent updates:** Use Git clone (easy updates)
- **One-time use:** Download ZIP (simpler)
- **Minimalist approach:** Download only necessary files
- **From mobile:** Download ZIP or use GitHub mobile app

**📱 Downloading from iPhone/Mobile Devices:**
If you downloaded from iPhone or other mobile device:
1. Transfer files to computer (AirDrop, cable, cloud storage)
2. Or use GitHub Desktop app
3. Or download ZIP directly and transfer via USB

**✅ Deletion Complete?**
If you successfully completed the deletion:
- ✓ You can empty Recycle Bin (for permanent deletion)
- ✓ Use one of the options above for new clone/download
- ✓ Ready to proceed with Rufus guide for USB installation (INSTALLATION-GUIDE.md)

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
