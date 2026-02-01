# Windows 11 Kurulum Rehberi / Windows 11 Installation Guide

## 🇹🇷 TÜRKÇE REHBER

### Windows 11 Sistem Gereksinimleri Nelerdir?

Windows 11, Microsoft tarafından belirlenen aşağıdaki minimum sistem gereksinimlerini talep eder:

- **İşlemci (CPU):** Intel 8. nesil veya AMD Ryzen 2000 serisi ve üzeri
- **RAM:** Minimum 4 GB
- **Depolama:** 64 GB veya daha fazla
- **TPM:** TPM 2.0 (Trusted Platform Module)
- **Secure Boot:** UEFI, Secure Boot özelliği aktif
- **Grafik Kartı:** DirectX 12 uyumlu
- **Ekran:** 720p çözünürlük, 9" veya daha büyük

### Neden Bu Gereksinimleri Atlamak İsteyebilirsiniz?

- Eski ama hala güçlü bir bilgisayarınız var
- TPM 2.0 modülü yok veya devre dışı
- BIOS'ta Secure Boot seçeneği yok
- CPU uyumluluk listesinde değil ama performans yeterli
- Sanal makinede Windows 11 çalıştırmak istiyorsunuz

### Adım Adım Kurulum

#### 1. Hazırlık

1. **Windows 11 ISO dosyasını indirin:**
   - Microsoft'un resmi sitesinden Windows 11 ISO'yu indirin
   - Önyüklenebilir bir USB sürücü oluşturun (Rufus veya Windows Media Creation Tool kullanabilirsiniz)

2. **Yedekleme:**
   - Önemli dosyalarınızın yedeğini alın
   - Kurulum sırasında veri kaybı olabilir

#### 1.1. Rufus ile Windows 11 Kurulum USB'si Oluşturma

Rufus, Windows kurulum USB'leri oluşturmak için en popüler ve kolay araçtır.

**Gereksinimler:**
- Rufus programı (https://rufus.ie adresinden indirin)
- En az 8 GB USB bellek (tercihen 16 GB)
- Windows 11 ISO dosyası

**📍 SİZİN DURUMUNUZ:**
✅ Windows 11 Türkçe x64 ISO dosyanız Masaüstünde (Desktop) hazır!
✅ Rufus programını indirdiniz
⏳ Şimdi USB oluşturma zamanı!

**Adım Adım Rufus Kullanımı:**

**ADIM 0: Hazırlık (SİZİN İÇİN)**
   - ISO dosyanızın konumunu not edin:
     ```
     C:\Users\[KullanıcıAdınız]\Desktop\Windows11_Turkish_x64.iso
     ```
     (Dosya adı farklı olabilir, örnek: `Win11_22H2_Turkish_x64.iso`)
   - USB belleğinizi bilgisayara takın (8 GB veya daha büyük)
   - USB'deki önemli dosyaları başka yere kopyalayın (SİLİNECEK!)

1. **Rufus'u Çalıştırın**
   - İndirdiğiniz `rufus.exe` dosyasına çift tıklayın
   - Yönetici izni isterse **"Evet"** deyin

2. **USB Belleği Takın ve Seçin**
   - USB belleğinizi bilgisayara takın
   - Rufus'ta **"Aygıt (Device)"** bölümünden USB belleğinizi seçin
   - **⚠️ UYARI:** USB'deki TÜM veriler silinecek! Önemli dosyalarınızı yedekleyin

3. **ISO Dosyasını Seçin (ÖNEMLİ!)**
   
   - **Önyükleme seçimi (Boot selection):** "Disk veya ISO kalıbı" seçin
   - **"SEÇIN"** veya **"SELECT"** butonuna tıklayın
   - Açılan pencerede:
     1. **Sol taraftan:** "Masaüstü" veya "Desktop" seçin
     2. Windows 11 ISO dosyanızı bulun (örnek: `Windows11_Turkish_x64.iso`)
     3. Dosyaya tıklayın
     4. **"Aç"** veya **"Open"** butonuna tıklayın
   
   ✅ Rufus'ta ISO dosya adı görünecek (örnek: `Windows11_Turkish_x64.iso`)

4. **Rufus Ayarları:**
   
   - **Bölümleme düzeni (Partition scheme):** 
     - Modern bilgisayarlar için (2013 sonrası): **GPT**
     - Eski bilgisayarlar için (2013 öncesi): **MBR**
     - **Emin değilseniz:** GPT seçin (çoğu bilgisayar için uygun)
   
   - **Hedef sistem (Target system):** 
     - **UEFI (non CSM)** (modern bilgisayarlar)
     - veya **BIOS or UEFI** (her ikisi için)
   
   - **Birim etiketi (Volume label):** 
     - "WIN11_TR" veya "WIN11_SETUP" (istediğiniz ismi verebilirsiniz)
   
   - **Dosya sistemi (File system):** 
     - **NTFS** (önerilen, Windows 11 için ideal)

5. **USB Oluşturmayı Başlat**
   - **"BAŞLAT"** veya **"START"** butonuna tıklayın
   
   - **Eğer soru çıkarsa:**
     - **"ISO modunda yaz"** (ISO Image mode) → ÖNERİLEN ✅
     - veya "DD modunda yaz" → Seçmeyin ❌
   
   - **Veri silinme uyarısı:**
     - "USB'deki TÜM veriler silinecek" uyarısını okuyun
     - **"TAMAM"** veya **"OK"** butonuna tıklayın
   
   - **İşlem süresi:** 5-15 dakika
     - İlerleme çubuğunu izleyin
     - Bitene kadar USB'yi çıkarmayın!
   
   - **İşlem tamamlandığında:** "HAZIR" veya "READY" yazısını göreceksiniz

6. **Bypass Dosyalarını Kopyalayın**
   
   **🚫 DİKKAT: ISO DOSYASININ İÇİNE DEĞİL!**
   
   ❌ Windows 11 ISO dosyasının içine kopyalamayın!
   ✅ USB belleğe kopyalayın!
   
   **📍 NEREYE KOPYALANIR?**
   
   - ❌ `Windows11_Turkish_x64.iso` dosyasının içine → HAYIR!
   - ✅ USB belleğe (E:, F:, D: gibi) → EVET!
   
   **⏱️ NE ZAMAN?**
   
   1. ✅ Önce: Rufus ile ISO'yu USB'ye yazdınız
   2. ✅ Şimdi: Bypass dosyalarını USB'ye kopyalayın
   
   USB oluşturulduktan sonra, **BU REPOSITORY'DEKİ** bypass dosyalarını USB'ye kopyalayın:
   
   **❓ "Bypass dosyaları" nedir?**
   
   Bu, indirdiğiniz/klonladığınız `bypass-win11-installer` repository'sindeki dosyalardır.
   Yani **GitHub'dan indirdiğiniz bu proje dosyaları**!
   
   **📂 Kaynak Konum (Repository dosyaları - SİZİN BİLGİSAYARINIZDA):**
   ```
   C:\Users\Oktay\bypass-win11-installer\
   ```
   
   Bu klasörde şu dosyaları bulacaksınız:
   - ✅ `bypass-win11-requirements.reg` → Registry dosyası
   - ✅ `bypass-installer.ps1` → PowerShell scripti
   - ✅ `bypass-installer.py` → Python scripti
   - ✅ `bypass-installer.bat` → Batch scripti
   - ✅ `setup-bypass.bat` → Kurulum scripti
   - ✅ `README.md` → Kullanım rehberi
   
   **🎯 Hedef Konum (USB bellek):**
   ```
   E:\bypass-win11-installer\
   ```
   (USB sürücü harfi farklı olabilir: D:, E:, F: vb.)
   
   **💡 Eğer bu dosyaları henüz indirmediyseniz:**
   
   Bu dosyalar GitHub'daki bu repository'de bulunuyor. İndirmek için:
   
   - **Yöntem 1:** [README.md](README.md) dosyasındaki "📥 Dosyaları Nasıl İndiririm?" bölümüne bakın
   - **Yöntem 2:** Bu sayfanın üstündeki yeşil "Code" → "Download ZIP" ile indirin
   - **Yöntem 3:** Git ile klonlayın: `git clone https://github.com/acaroktay1967-crypto/bypass-win11-installer.git`
   
   **📋 Nasıl Kopyalarsınız:**
   
   1. **Dosya Gezgini**'ni açın (Windows tuşu + E)
   2. Sol bölmede: `C:\Users\Oktay\bypass-win11-installer` klasörünü bulun
      - Veya nereye indirdiyseniz oraya gidin
   3. **Tüm klasörü** sağ tıklayın → **Kopyala** (veya Ctrl+C)
   4. USB belleğe gidin (örnek: E:)
   5. Boş alana sağ tıklayın → **Yapıştır** (veya Ctrl+V)
   
   **✅ Sonuç:**
   
   USB'nizde şu yapı oluşacak:
   ```
   USB Bellek (E:\)
   │
   ├── 📁 Windows Kurulum Dosyaları (Rufus tarafından oluşturuldu)
   │   ├── bootmgr
   │   ├── sources\
   │   │   ├── boot.wim
   │   │   └── install.wim
   │   ├── efi\
   │   └── ... (diğer Windows dosyaları)
   │
   └── 📁 bypass-win11-installer\  ← SİZ KOPYALADINIZ (ADIM 6)
       ├── bypass-win11-requirements.reg
       ├── bypass-installer.ps1
       ├── bypass-installer.py
       ├── bypass-installer.bat
       ├── setup-bypass.bat
       └── README.md
   ```
   
   **📊 ÖZET:**
   - **Rufus** → Windows dosyalarını USB'ye yazdı (bootmgr, sources, efi vb.)
   - **Siz** → Bypass klasörünü USB'ye kopyaladınız
   - **Sonuç** → USB'de hem Windows hem bypass dosyaları var

**✅ İŞLEM TAMAMLANDI!**

Artık USB belleğinizde:
- ✅ Windows 11 Türkçe x64 kurulum dosyaları
- ✅ Bypass araçları

**💡 İpuçları:** 
- USB'de hem Windows kurulum dosyaları hem de bypass araçları olacak
- Kurulum sırasında **Shift + F10** ile komut istemine erişebilirsiniz
- USB sürücü harfini bulmak için: `diskpart` → `list volume`
- USB'yi güvenli çıkarın: Sistem tepsisinden "USB'yi Güvenli Çıkar"

**🎯 Sonraki Adım:**
- Bilgisayarı kapatın
- BIOS'a girin (genellikle F2, F12, Del tuşu)
- Boot sırasını USB'den başlatacak şekilde ayarlayın
- Bilgisayarı USB'den başlatın
- Windows 11 kurulumuna başlayın!

**Rufus Alternatifi:**
Eğer Rufus kullanmak istemezseniz:
- **Windows Media Creation Tool** (Microsoft'tan)
- **Ventoy** (birden fazla ISO için)
- **WoeUSB** (Linux için)

#### 2. Kurulum Süreci

**Seçenek A: Registry Dosyası ile (Önerilen)**

1. USB'den bilgisayarı başlatın
2. "Bu PC Windows 11'i çalıştıramaz" uyarısını gördüğünüzde:
   - **Shift + F10** tuşlarına aynı anda basın
3. Komut İstemi açılacak, şu adımları izleyin:
   ```
   notepad
   ```
4. Notepad'de **File > Open** menüsünden USB sürücünüzde bulunan `bypass-win11-requirements.reg` dosyasını bulun
5. Dosyayı kapatın ve Command Prompt'a dönün
6. Şunu yazın:
   ```
   regedit
   ```
7. Registry Editor'de **File > Import** ile `bypass-win11-requirements.reg` dosyasını içe aktarın
8. Tüm pencereleri kapatın ve "Geri" butonuna tıklayıp kuruluma devam edin

**Seçenek B: Manuel Registry Girişi**

1. USB'den bilgisayarı başlatın
2. **Shift + F10** ile Command Prompt açın
3. `regedit` yazın ve Enter'a basın
4. Sol tarafta şu yolu takip edin:
   ```
   HKEY_LOCAL_MACHINE\SYSTEM\Setup
   ```
5. `Setup` üzerine sağ tıklayın → **New > Key** → Adını `LabConfig` yapın
6. `LabConfig` seçiliyken, sağ tarafta boş alana sağ tıklayın → **New > DWORD (32-bit) Value**
7. Şu değerleri oluşturun (her biri için değeri **1** yapın):
   - `BypassTPMCheck`
   - `BypassSecureBootCheck`
   - `BypassRAMCheck`
   - `BypassCPUCheck`
8. Her değeri çift tıklayarak açın ve "Value data" kısmına **1** yazın
9. Registry Editor'ü kapatın ve kuruluma devam edin

**Seçenek C: Batch Script ile**

1. USB'den bilgisayarı başlatın
2. **Shift + F10** ile Command Prompt açın
3. USB sürücünün harfini bulun (genellikle D: veya E:):
   ```
   dir d:
   ```
4. Doğru sürücüyü bulduğunuzda:
   ```
   d:
   setup-bypass.bat
   ```
5. Script otomatik olarak gerekli ayarları yapacak
6. Tamamlandığında kuruluma devam edin

**Seçenek D: PowerShell Script (Gelişmiş - Önerilen)**

PowerShell, daha fazla bilgi ve renkli çıktı sunar:

1. Windows'ta PowerShell'i **Yönetici olarak çalıştır**
2. Script klasörüne gidin:
   ```powershell
   cd C:\path\to\bypass-win11-installer
   ```
3. Execution Policy'yi geçici olarak atlayarak çalıştırın:
   ```powershell
   powershell -ExecutionPolicy Bypass -File bypass-installer.ps1
   ```
4. Ekranda şunları göreceksiniz:
   - Yönetici yetkisi kontrolü
   - Yapılacak değişikliklerin listesi
   - Onay istemi (E/H)
   - Her adımda ilerleme göstergesi
   - Başarı/hata mesajları (renkli)
   - Son durumun doğrulanması

**Özellikler:**
- ✅ 4GB RAM'li bilgisayarlar için özel destek
- ✅ Renkli terminal çıktısı
- ✅ Detaylı hata mesajları
- ✅ Registry değerlerini doğrulama
- ✅ İşlem sonrası durum raporu

**Seçenek E: Python Script (Çapraz Platform)**

Python yüklüyse (3.6 veya üzeri):

1. Komut İstemi'ni veya PowerShell'i **Yönetici olarak çalıştır**
2. Script klasörüne gidin:
   ```bash
   cd C:\path\to\bypass-win11-installer
   ```
3. Python scriptini çalıştırın:
   ```bash
   python bypass-installer.py
   ```
   veya Python 3 için:
   ```bash
   python3 bypass-installer.py
   ```
4. Script şunları yapacak:
   - Platform kontrolü (Windows gerekli)
   - Yönetici yetkisi kontrolü
   - Kullanıcı onayı alma
   - Registry değişikliklerini uygulama
   - Sonuçları doğrulama ve gösterme

**Özellikler:**
- ✅ Python 3.6+ uyumlu
- ✅ 4GB RAM desteği
- ✅ Renkli ANSI terminal çıktısı
- ✅ Detaylı hata yönetimi
- ✅ Başarı/başarısızlık sayacı
- ✅ Windows dışı platformlarda güvenli hata verme

**Hangi Yöntemi Seçmeliyim?**

| Yöntem | Kolay | Hızlı | Detay | Önerilen |
|--------|-------|-------|-------|----------|
| Registry Dosyası | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ | Başlangıç |
| Manuel | ⭐ | ⭐ | ⭐⭐⭐ | Öğrenme |
| Batch Script | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Standart |
| PowerShell | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ✅ Evet |
| Python | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Gelişmiş |

#### 3. Kurulum Sonrası

Kurulum başarıyla tamamlandıktan sonra:

1. Windows güncellemelerini kontrol edin
2. Tüm sürücülerin yüklendiğinden emin olun
3. Windows Update ayarlarını kontrol edin

### Sık Sorulan Sorular

**S: Bu yöntem güvenli mi?**
C: Evet, bu yöntem registry ayarlarını değiştirerek Microsoft'un resmi kurulum programını kullanır. Ancak desteklenmeyen donanımda çalıştırmak bazı riskler içerebilir.

**S: Güncellemeleri alabilecek miyim?**
C: Evet, çoğu durumda güncellemeleri almaya devam edeceksiniz. Ancak Microsoft gelecekte desteklenmeyen sistemler için güncellemeleri kısıtlayabilir.

**S: TPM 2.0 olmadan güvenlik sorunu olur mu?**
C: TPM, şifreleme ve güvenlik için önemlidir. Eğer hassas verilerle çalışıyorsanız, TPM 2.0 destekli bir sistem kullanmanız önerilir.

**S: Hangi yöntemi seçmeliyim?**
C: 
- **Yeni başlayanlar:** Registry dosyası yöntemi (Seçenek A) en kolay ve hızlısıdır.
- **Daha fazla kontrol isteyenler:** PowerShell scripti (Seçenek D) önerilir - renkli çıktı ve detaylı bilgi sağlar.
- **Python deneyimi olanlar:** Python scripti (Seçenek E) çapraz platform desteği ve detaylı hata yönetimi sunar.
- **Batch script:** Seçenek C basit ve otomatiktir, ancak PowerShell kadar detaylı değildir.

**S: 4GB RAM'li bilgisayarımda çalışır mı?**
C: Evet! Özellikle PowerShell ve Python scriptleri 4GB RAM'li sistemler için özel olarak optimize edilmiştir. BypassRAMCheck registry değeri 4GB'lık sistemlerde bile Windows 11 kurulumunu mümkün kılar.

**S: PowerShell scripti çalışmıyor, ne yapmalıyım?**
C: PowerShell'i mutlaka "Yönetici olarak çalıştır" seçeneği ile açın. Execution policy hatası alırsanız, scripti şu şekilde çalıştırın:
```powershell
powershell -ExecutionPolicy Bypass -File bypass-installer.ps1
```

**S: Python scripti için hangi modüller gerekli?**
C: Python scripti sadece standart kütüphane modüllerini kullanır (sys, ctypes, winreg, platform). Ekstra paket kurulumuna gerek yoktur. Python 3.6 veya üzeri sürüm yeterlidir.


---

## 🇬🇧 ENGLISH GUIDE

### What Are Windows 11 System Requirements?

Windows 11 requires the following minimum system requirements as determined by Microsoft:

- **Processor (CPU):** Intel 8th gen or AMD Ryzen 2000 series and newer
- **RAM:** Minimum 4 GB
- **Storage:** 64 GB or more
- **TPM:** TPM 2.0 (Trusted Platform Module)
- **Secure Boot:** UEFI with Secure Boot capability enabled
- **Graphics Card:** DirectX 12 compatible
- **Display:** 720p resolution, 9" or larger

### Why Would You Want to Bypass These Requirements?

- You have an older but still powerful computer
- No TPM 2.0 module or it's disabled
- No Secure Boot option in BIOS
- CPU is not on compatibility list but performance is sufficient
- Want to run Windows 11 in a virtual machine

### Step-by-Step Installation

#### 1. Preparation

1. **Download Windows 11 ISO file:**
   - Download Windows 11 ISO from Microsoft's official website
   - Create a bootable USB drive (you can use Rufus or Windows Media Creation Tool)

2. **Backup:**
   - Back up your important files
   - Data loss may occur during installation

#### 1.1. Creating Windows 11 Installation USB with Rufus

Rufus is the most popular and easy tool for creating Windows installation USB drives.

**Requirements:**
- Rufus program (download from https://rufus.ie)
- At least 8 GB USB drive (preferably 16 GB)
- Windows 11 ISO file

**Step-by-Step Rufus Usage:**

1. **Run Rufus**
   - Double-click the downloaded `rufus.exe` file
   - Click **"Yes"** if administrator permission is requested

2. **Insert USB Drive**
   - Insert your USB drive into the computer
   - **WARNING:** All data on the USB will be erased! Backup important files

3. **Rufus Settings:**
   
   - **Device:** Select your USB drive
   - **Boot selection:** Choose "Disk or ISO image"
   - Click **SELECT** button and choose your Windows 11 ISO file
   - **Partition scheme:** 
     - For modern computers: **GPT**
     - For older computers: **MBR**
   - **Target system:** **UEFI (non CSM)** (or **BIOS or UEFI** for BIOS)
   - **Volume label:** "WIN11_SETUP" (you can use any name)
   - **File system:** **NTFS** (recommended)

4. **Start**
   - Click **"START"** button
   - If prompted: Select **"Write in ISO mode"** (recommended)
   - Confirm the warning that data on USB will be erased
   - Process may take 5-15 minutes

5. **Copy Bypass Files**
   
   After USB is created, copy bypass files to USB:
   
   ```
   Copy files from C:\Users\Oktay\bypass-win11-installer folder
   to USB drive (example: E:\bypass-win11-installer)
   ```
   
   Files to copy:
   - `bypass-win11-requirements.reg`
   - `bypass-installer.ps1`
   - `setup-bypass.bat`
   - `README.md` (for reference)

**💡 Tip:** 
- USB will have both Windows installation files and bypass tools
- During installation, access command prompt with **Shift + F10**
- To find USB drive letter: `diskpart` → `list volume`

**Rufus Alternative:**
If you don't want to use Rufus:
- **Windows Media Creation Tool** (from Microsoft)
- **Ventoy** (for multiple ISOs)
- **WoeUSB** (for Linux)

#### 2. Installation Process

**Option A: Using Registry File (Recommended)**

1. Boot computer from USB
2. When you see "This PC can't run Windows 11" warning:
   - Press **Shift + F10** simultaneously
3. Command Prompt will open, follow these steps:
   ```
   notepad
   ```
4. In Notepad, use **File > Open** to locate the `bypass-win11-requirements.reg` file on your USB drive
5. Close the file and return to Command Prompt
6. Type:
   ```
   regedit
   ```
7. In Registry Editor, go to **File > Import** and import the `bypass-win11-requirements.reg` file
8. Close all windows and click "Back" to continue installation

**Option B: Manual Registry Entry**

1. Boot computer from USB
2. Open Command Prompt with **Shift + F10**
3. Type `regedit` and press Enter
4. Navigate to:
   ```
   HKEY_LOCAL_MACHINE\SYSTEM\Setup
   ```
5. Right-click on `Setup` → **New > Key** → Name it `LabConfig`
6. With `LabConfig` selected, right-click in empty space on right → **New > DWORD (32-bit) Value**
7. Create these values (set each to **1**):
   - `BypassTPMCheck`
   - `BypassSecureBootCheck`
   - `BypassRAMCheck`
   - `BypassCPUCheck`
8. Double-click each value and enter **1** in "Value data"
9. Close Registry Editor and continue installation

**Option C: Using Batch Script**

1. Boot computer from USB
2. Open Command Prompt with **Shift + F10**
3. Find your USB drive letter (usually D: or E:):
   ```
   dir d:
   ```
4. Once you find the correct drive:
   ```
   d:
   setup-bypass.bat
   ```
5. Script will automatically configure necessary settings
6. When complete, continue with installation

**Option D: PowerShell Script (Advanced - Recommended)**

PowerShell provides more information and colored output:

1. On Windows, open PowerShell **as Administrator**
2. Navigate to the script folder:
   ```powershell
   cd C:\path\to\bypass-win11-installer
   ```
3. Run with execution policy bypass:
   ```powershell
   powershell -ExecutionPolicy Bypass -File bypass-installer.ps1
   ```
4. You will see:
   - Administrator privilege check
   - List of changes to be made
   - Confirmation prompt (Y/N)
   - Progress indicator for each step
   - Success/error messages (colored)
   - Final verification of settings

**Features:**
- ✅ Special support for 4GB RAM computers
- ✅ Colored terminal output
- ✅ Detailed error messages
- ✅ Registry value verification
- ✅ Post-operation status report

**Option E: Python Script (Cross-Platform)**

If you have Python installed (3.6 or higher):

1. Open Command Prompt or PowerShell **as Administrator**
2. Navigate to the script folder:
   ```bash
   cd C:\path\to\bypass-win11-installer
   ```
3. Run the Python script:
   ```bash
   python bypass-installer.py
   ```
   or for Python 3:
   ```bash
   python3 bypass-installer.py
   ```
4. The script will:
   - Check platform (Windows required)
   - Check administrator privileges
   - Request user confirmation
   - Apply registry changes
   - Verify and display results

**Features:**
- ✅ Python 3.6+ compatible
- ✅ 4GB RAM support
- ✅ Colored ANSI terminal output
- ✅ Detailed error handling
- ✅ Success/failure counter
- ✅ Safe error handling on non-Windows platforms

**Which Method Should I Choose?**

| Method | Easy | Fast | Detail | Recommended |
|--------|------|------|--------|-------------|
| Registry File | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ | Beginners |
| Manual | ⭐ | ⭐ | ⭐⭐⭐ | Learning |
| Batch Script | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | Standard |
| PowerShell | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ✅ Yes |
| Python | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | Advanced |

#### 3. Post-Installation

After successful installation:

1. Check for Windows updates
2. Ensure all drivers are installed
3. Review Windows Update settings

### Frequently Asked Questions

**Q: Is this method safe?**
A: Yes, this method uses Microsoft's official installer by modifying registry settings. However, running on unsupported hardware may carry some risks.

**Q: Will I be able to receive updates?**
A: Yes, in most cases you will continue to receive updates. However, Microsoft may restrict updates for unsupported systems in the future.

**Q: Are there security concerns without TPM 2.0?**
A: TPM is important for encryption and security. If you work with sensitive data, a system with TPM 2.0 support is recommended.

**Q: Which method should I choose?**
A:
- **Beginners:** Registry file method (Option A) is easiest and fastest.
- **More control:** PowerShell script (Option D) is recommended - provides colored output and detailed information.
- **Python experience:** Python script (Option E) offers cross-platform support and detailed error handling.
- **Batch script:** Option C is simple and automated, but not as detailed as PowerShell.

**Q: Will this work on my 4GB RAM computer?**
A: Yes! The PowerShell and Python scripts are specifically optimized for 4GB RAM systems. The BypassRAMCheck registry value enables Windows 11 installation even on systems with only 4GB RAM.

**Q: PowerShell script won't run, what should I do?**
A: Make sure to open PowerShell with "Run as Administrator". If you get an execution policy error, run the script like this:
```powershell
powershell -ExecutionPolicy Bypass -File bypass-installer.ps1
```

**Q: What modules are required for the Python script?**
A: The Python script only uses standard library modules (sys, ctypes, winreg, platform). No additional package installation is required. Python 3.6 or higher is sufficient.


---

## 🔒 Security Considerations / Güvenlik Hususları

### EN:
- **BitLocker:** May not work properly without TPM 2.0
- **Windows Hello:** May have limited functionality
- **Secure Boot:** Disabling may increase vulnerability to rootkits
- **Updates:** Microsoft may limit updates for unsupported hardware

### TR:
- **BitLocker:** TPM 2.0 olmadan düzgün çalışmayabilir
- **Windows Hello:** Sınırlı işlevsellik gösterebilir
- **Secure Boot:** Devre dışı bırakmak rootkit'lere karşı güvenlik açığı oluşturabilir
- **Güncellemeler:** Microsoft desteklenmeyen donanımlar için güncellemeleri sınırlayabilir

---

## 📞 Support / Destek

If you encounter issues / Sorun yaşarsanız:

1. Check that all registry values are set correctly
2. Try a different method (A, B, or C)
3. Ensure your USB drive is properly created
4. Verify ISO file integrity

For more help, create an issue on GitHub.

---

**Last Updated:** January 2026
**Version:** 1.0
