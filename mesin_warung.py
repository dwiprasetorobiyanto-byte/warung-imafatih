import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppWarungPro(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("ImaFatih - Laba Otomatis")
        self.geometry("500x750")

        # Judul Utama
        self.label_judul = ctk.CTkLabel(self, text="MANAJEMEN LABA WARUNG", font=("Roboto", 22, "bold"))
        self.label_judul.pack(pady=20)

        # Frame Input
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=10, padx=40, fill="both", expand=True)

        # Input untuk masing-masing jajan
        self.entry_a = self.buat_input("Jajan A (Rp 1.000)", 0)
        self.entry_b = self.buat_input("Jajan B (Rp 2.000)", 1)
        self.entry_c = self.buat_input("Jajan C (Rp 3.000)", 2)
        self.entry_d = self.buat_input("Jajan D (Rp 4.000)", 3)

        # Tombol Hitung
        self.btn_hitung = ctk.CTkButton(self, text="HITUNG LABA HARI INI", command=self.hitung_laba, font=("Roboto", 14, "bold"))
        self.btn_hitung.pack(pady=15)

        # Tombol Simpan Laporan
        self.btn_simpan = ctk.CTkButton(self, text="SIMPAN KE LAPORAN", command=self.simpan_laporan, fg_color="#3498db")
        self.btn_simpan.pack(pady=5)

        # Output Tampilan
        self.label_omzet = ctk.CTkLabel(self, text="Total Omzet: Rp 0", font=("Roboto", 14))
        self.label_omzet.pack(pady=2)

        self.label_laba = ctk.CTkLabel(self, text="LABA BERSIH: Rp 0", font=("Roboto", 20, "bold"), text_color="#2ecc71")
        self.label_laba.pack(pady=15)
        
        self.label_status = ctk.CTkLabel(self, text="", font=("Roboto", 12))
        self.label_status.pack(pady=5)

    def buat_input(self, nama, baris):
        label = ctk.CTkLabel(self.frame, text=nama)
        label.grid(row=baris, column=0, padx=20, pady=10, sticky="w")
        entry = ctk.CTkEntry(self.frame, placeholder_text="Qty")
        entry.grid(row=baris, column=1, padx=20, pady=10)
        return entry

    def hitung_laba(self):
        try:
            # Ambil Jumlah Terjual
            q_a = int(self.entry_a.get() or 0)
            q_b = int(self.entry_b.get() or 0)
            q_c = int(self.entry_c.get() or 0)
            q_d = int(self.entry_d.get() or 0)

            # Logika Perhitungan (Otomatis Potong Modal)
            # Rumus: (Harga Jual - Harga Modal) * Jumlah Terjual
            untung_a = (1000 - 800) * q_a
            untung_b = (2000 - 1600) * q_b
            untung_c = (3000 - 2400) * q_c
            untung_d = (4000 - 3200) * q_d

            self.total_omzet = (q_a * 1000) + (q_b * 2000) + (q_c * 3000) + (q_d * 4000)
            self.total_laba = untung_a + untung_b + untung_c + untung_d

            # Update Tampilan
            self.label_omzet.configure(text=f"Total Omzet: Rp {self.total_omzet:,.0f}")
            self.label_laba.configure(text=f"LABA BERSIH: Rp {self.total_laba:,.0f}")
            self.label_status.configure(text="Hitungan selesai.", text_color="white")

        except ValueError:
            self.label_status.configure(text="Error: Masukkan angka saja!", text_color="#e74c3c")

    def simpan_laporan(self):
        try:
            if not hasattr(self, 'total_laba'):
                self.label_status.configure(text="Hitung dulu sebelum simpan!", text_color="yellow")
                return

            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = f"[{waktu}] Omzet: Rp {self.total_omzet:,.0f} | Laba Bersih: Rp {self.total_laba:,.0f}\n"

            # Simpan ke file teks (Append mode)
            with open("laporan_warung.txt", "a") as file:
                file.write(data)
            
            self.label_status.configure(text="Laporan berhasil disimpan ke laporan_warung.txt", text_color="#2ecc71")
        except Exception as e:
            self.label_status.configure(text=f"Gagal simpan: {str(e)}", text_color="red")

if __name__ == "__main__":
    app = AppWarungPro()
    app.mainloop()