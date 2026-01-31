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
C: Registry dosyası yöntemi (Seçenek A) en kolay ve hızlısıdır. Batch script (Seçenek C) daha otomatiktir ve hata kontrolü sağlar.

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
A: The registry file method (Option A) is easiest and fastest. The batch script (Option C) is more automated and provides error checking.

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
