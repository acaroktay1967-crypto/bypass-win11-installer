# bypass_win11_installer.py

import os
import subprocess
import tkinter as tk
from tkinter import messagebox

# PowerShell Script to bypass Windows 11 installation requirements
BY_PASS_SCRIPT = """
Write-Host \"Windows 11 gereksinimlerini bypass etmek için kayıt defteri düzenleniyor...\" -ForegroundColor Green

# Kayıt defteri yolunu belirliyoruz
$RegPath = \"HKLM:\SYSTEM\Setup\LabConfig\"

# LabConfig anahtarı yoksa oluşturuyoruz
if (-not (Test-Path $RegPath)) {
    New-Item -Path \"HKLM:\SYSTEM\Setup\\" -Name \"LabConfig\" -Force
}

# TPM, Secure Boot ve RAM gereksinimlerini bypass eden anahtarları ekliyoruz
New-ItemProperty -Path $RegPath -Name \"BypassTPMCheck\" -PropertyType DWord -Value 1 -Force | Out-Null
New-ItemProperty -Path $RegPath -Name \"BypassSecureBootCheck\" -PropertyType DWord -Value 1 -Force | Out-Null
New-ItemProperty -Path $RegPath -Name \"BypassRAMCheck\" -PropertyType DWord -Value 1 -Force | Out-Null
New-ItemProperty -Path $RegPath -Name \"BypassCPUCheck\" -PropertyType DWord -Value 1 -Force | Out-Null

Write-Host \"TPM, Secure Boot ve diğer kontroller başarıyla bypass edildi!\" -ForegroundColor Yellow
"""

# Run the PowerShell Script
def run_bypass_script():
    try:
        # Save PowerShell script to a file
        with open("bypass_win11.ps1", "w") as script_file:
            script_file.write(BY_PASS_SCRIPT)

        # Execute the PowerShell script
        subprocess.run([
            "powershell", "-ExecutionPolicy", "Bypass", "-File", "bypass_win11.ps1"
        ], check=True)

        # Success message
        messagebox.showinfo("Başarılı", "Windows 11 gereksinimleri başarıyla bypass edildi!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Hata", f"PowerShell çalıştırılırken bir hata oluştu: {e}")
    finally:
        # Remove temporary script file
        if os.path.exists("bypass_win11.ps1"):
            os.remove("bypass_win11.ps1")

# Create GUI for the tool
def create_gui():
    window = tk.Tk()
    window.title("Windows 11 Bypass Aracı")

    label = tk.Label(window, text="Windows 11 asgari gereksinimlerini bypass etmek için butona tıklayın.", wraplength=300)
    label.pack(pady=10)

    bypass_button = tk.Button(window, text="Bypass İşlemini Başlat", command=run_bypass_script, bg="green", fg="white")
    bypass_button.pack(pady=20)

    exit_button = tk.Button(window, text="Çıkış", command=window.destroy, bg="red", fg="white")
    exit_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    create_gui()