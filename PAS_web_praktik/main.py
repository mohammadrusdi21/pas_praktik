
import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# ==========================================
# KONFIGURASI APLIKASI
# ==========================================

APP_TITLE = "PAS Praktik - Pemrograman Web"
DATA_DIR = "data"
PACKAGE_FILE = os.path.join(DATA_DIR, "packages.json")
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")

BG = "#F1F5F9"
PRIMARY = "#2563EB"
DARK = "#172554"
WHITE = "#FFFFFF"
GREEN = "#16A34A"


# ==========================================
# DATA 31 PAKET PROYEK
# ==========================================

PACKAGES = [
    ("Website Profil Pribadi", "Mudah",
     "Membuat website biodata dan portofolio pribadi.",
     ["Foto profil", "Biodata", "Riwayat pendidikan", "Kontak"],
     ["Gunakan HTML semantik", "Atur layout dengan CSS",
      "Tambahkan interaksi tombol dengan JavaScript"]),

    ("Website Profil Sekolah", "Mudah",
     "Membuat website informasi profil sekolah.",
     ["Identitas sekolah", "Visi dan misi", "Program keahlian", "Kontak"],
     ["Navigasi halaman", "Layout responsif", "Menu interaktif"]),

    ("Website Perpustakaan", "Sedang",
     "Membuat katalog buku digital sederhana.",
     ["Daftar buku", "Pencarian buku", "Kategori", "Detail buku"],
     ["Array objek JavaScript", "Fitur pencarian", "Filter kategori"]),

    ("Aplikasi Kalkulator", "Mudah",
     "Membuat kalkulator operasi matematika.",
     ["Penjumlahan", "Pengurangan", "Perkalian", "Pembagian"],
     ["Event click", "Operator matematika", "Validasi input"]),

    ("Aplikasi Kasir Sederhana", "Sedang",
     "Membuat aplikasi transaksi penjualan.",
     ["Input barang", "Harga", "Jumlah", "Total belanja"],
     ["Perhitungan otomatis", "Array barang", "Cetak transaksi"]),

    ("Aplikasi To Do List", "Sedang",
     "Membuat aplikasi pengelolaan tugas.",
     ["Tambah tugas", "Edit tugas", "Hapus tugas", "Status selesai"],
     ["DOM manipulation", "Event listener", "LocalStorage"]),

    ("Website Toko Online", "Sulit",
     "Membuat tampilan toko online sederhana.",
     ["Daftar produk", "Keranjang", "Harga", "Total belanja"],
     ["Array objek", "Keranjang belanja", "Responsive design"]),

    ("Aplikasi Absensi Siswa", "Sedang",
     "Membuat aplikasi pencatatan kehadiran siswa.",
     ["Nama siswa", "Tanggal", "Status hadir", "Rekap"],
     ["Manipulasi tabel", "Validasi form", "Penyimpanan lokal"]),

    ("Aplikasi Nilai Siswa", "Sedang",
     "Membuat aplikasi pengolahan nilai siswa.",
     ["Nama siswa", "Nilai tugas", "UTS", "UAS", "Nilai akhir"],
     ["Operator matematika", "Percabangan", "Array"]),

    ("Website Berita", "Mudah",
     "Membuat portal berita sederhana.",
     ["Judul berita", "Gambar", "Kategori", "Isi berita"],
     ["Grid layout", "Card berita", "Navigasi"]),

    ("Aplikasi Penghitung Diskon", "Mudah",
     "Membuat aplikasi perhitungan diskon belanja.",
     ["Harga awal", "Persentase diskon", "Potongan", "Total bayar"],
     ["Input angka", "Operator matematika", "Validasi"]),

    ("Aplikasi Konversi Suhu", "Mudah",
     "Membuat aplikasi konversi suhu.",
     ["Celcius", "Fahrenheit", "Kelvin", "Hasil konversi"],
     ["Fungsi JavaScript", "Percabangan", "Perhitungan"]),

    ("Website Galeri Foto", "Mudah",
     "Membuat galeri foto interaktif.",
     ["Daftar gambar", "Kategori", "Preview gambar", "Navigasi"],
     ["CSS Grid", "Responsive image", "Event JavaScript"]),

    ("Aplikasi Pendaftaran Siswa", "Sedang",
     "Membuat form pendaftaran siswa baru.",
     ["Nama", "NISN", "Alamat", "Jurusan", "Validasi"],
     ["Form HTML", "Validasi JavaScript", "Tabel data"]),

    ("Aplikasi Data Karyawan", "Sedang",
     "Membuat aplikasi pengelolaan data karyawan.",
     ["Tambah karyawan", "Edit data", "Hapus data", "Pencarian"],
     ["CRUD", "Array objek", "LocalStorage"]),

    ("Aplikasi Inventaris Barang", "Sedang",
     "Membuat aplikasi pencatatan inventaris.",
     ["Kode barang", "Nama barang", "Stok", "Kategori"],
     ["CRUD", "Filter data", "Validasi input"]),

    ("Website Undangan Digital", "Mudah",
     "Membuat undangan acara berbasis web.",
     ["Nama acara", "Tanggal", "Lokasi", "Ucapan"],
     ["CSS animation", "Responsive layout", "Interaksi tombol"]),

    ("Aplikasi Kuis Online", "Sedang",
     "Membuat aplikasi kuis pilihan ganda.",
     ["Pertanyaan", "Pilihan jawaban", "Skor", "Hasil"],
     ["Array soal", "Percabangan", "Timer sederhana"]),

    ("Aplikasi Pengelola Keuangan", "Sedang",
     "Membuat aplikasi pencatatan keuangan.",
     ["Pemasukan", "Pengeluaran", "Saldo", "Riwayat"],
     ["Perhitungan saldo", "LocalStorage", "Filter transaksi"]),

    ("Website Restoran", "Mudah",
     "Membuat website informasi dan menu restoran.",
     ["Profil restoran", "Menu makanan", "Harga", "Kontak"],
     ["Card menu", "Layout responsif", "Navigasi"]),

    ("Aplikasi Pemesanan Tiket", "Sulit",
     "Membuat sistem pemesanan tiket sederhana.",
     ["Nama pemesan", "Tujuan", "Tanggal", "Jumlah tiket"],
     ["Validasi form", "Perhitungan harga", "Konfirmasi pesanan"]),

    ("Aplikasi Rental Mobil", "Sulit",
     "Membuat aplikasi penyewaan mobil.",
     ["Data mobil", "Harga sewa", "Durasi", "Total biaya"],
     ["CRUD", "Perhitungan biaya", "Validasi"]),

    ("Website Kursus Online", "Sedang",
     "Membuat website informasi kursus.",
     ["Daftar kursus", "Materi", "Instruktur", "Pendaftaran"],
     ["Navigasi", "Card kursus", "Form pendaftaran"]),

    ("Aplikasi Catatan Digital", "Sedang",
     "Membuat aplikasi pencatatan digital.",
     ["Tambah catatan", "Edit catatan", "Hapus catatan", "Cari"],
     ["DOM", "LocalStorage", "CRUD"]),

    ("Aplikasi Monitoring Stok", "Sulit",
     "Membuat aplikasi pemantauan stok barang.",
     ["Data barang", "Stok masuk", "Stok keluar", "Laporan"],
     ["Perhitungan stok", "CRUD", "Filter data"]),

    ("Website Company Profile", "Sedang",
     "Membuat website profil perusahaan.",
     ["Tentang perusahaan", "Layanan", "Tim", "Kontak"],
     ["Responsive design", "CSS Flexbox", "Form kontak"]),

    ("Aplikasi Penggajian", "Sulit",
     "Membuat aplikasi perhitungan gaji karyawan.",
     ["Gaji pokok", "Tunjangan", "Potongan", "Gaji bersih"],
     ["Operator matematika", "Percabangan", "Validasi"]),

    ("Aplikasi Booking Lapangan", "Sulit",
     "Membuat aplikasi pemesanan lapangan olahraga.",
     ["Nama pemesan", "Jadwal", "Durasi", "Biaya"],
     ["Validasi jadwal", "Perhitungan biaya", "Penyimpanan data"]),

    ("Website E-Learning", "Sulit",
     "Membuat website pembelajaran digital.",
     ["Daftar materi", "Video", "Latihan", "Evaluasi"],
     ["Navigasi materi", "Kuis interaktif", "Progress belajar"]),

    ("Aplikasi Dashboard Penjualan", "Sulit",
     "Membuat dashboard informasi penjualan.",
     ["Total penjualan", "Jumlah transaksi", "Produk terlaris", "Grafik"],
     ["Pengolahan array", "Visualisasi data", "Filter laporan"]),

    ("Aplikasi Manajemen Sekolah", "Sulit",
     "Membuat aplikasi pengelolaan data sekolah.",
     ["Data siswa", "Data guru", "Data kelas", "Rekap data"],
     ["CRUD", "Pencarian", "Dashboard", "LocalStorage"])
]


# ==========================================
# PENYIMPANAN DATA
# ==========================================

os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(PACKAGE_FILE):
    with open(PACKAGE_FILE, "w", encoding="utf-8") as f:
        json.dump(PACKAGES, f, indent=4, ensure_ascii=False)

if not os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump({}, f)


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ==========================================
# APLIKASI UTAMA
# ==========================================

class LabWebApp:

    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.root.configure(bg=BG)

        self.packages = load_json(PACKAGE_FILE, PACKAGES)
        self.progress = load_json(PROGRESS_FILE, {})

        self.selected_index = None

        self.build_interface()
        self.show_package_list()

    # --------------------------------------
    # HEADER
    # --------------------------------------

    def build_interface(self):

        header = tk.Frame(self.root, bg=DARK, height=85)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="PAS PRAKTIK | PEMROGRAMAN WEB",
            font=("Arial", 23, "bold"),
            fg=WHITE,
            bg=DARK
        ).pack(side="left", padx=25, pady=15)

        tk.Label(
            header,
            text="PROJECT HTML • CSS • JAVASCRIPT | By: Mohammad Rusdi",
            font=("Arial", 11),
            fg="#BFDBFE",
            bg=DARK
        ).pack(side="left", padx=5)

        # Navigasi
        nav = tk.Frame(self.root, bg=WHITE, height=48)
        nav.pack(fill="x")

        ttk.Button(
            nav, text="Daftar Paket",
            command=self.show_package_list
        ).pack(side="left", padx=10, pady=8)

        ttk.Button(
            nav, text="Panduan",
            command=self.show_guide
        ).pack(side="left", padx=5, pady=8)

        self.content = tk.Frame(self.root, bg=BG)
        self.content.pack(fill="both", expand=True, padx=20, pady=15)

    # --------------------------------------
    # HALAMAN DAFTAR PAKET
    # --------------------------------------

    def show_package_list(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="PILIH PAKET PROJECT",
            font=("Arial", 19, "bold"),
            bg=BG,
            fg=DARK
        ).pack(anchor="w", pady=(0, 5))

        tk.Label(
            self.content,
            text="Pilih salah satu project untuk melihat instruksi praktikum.",
            font=("Arial", 10),
            bg=BG,
            fg="#64748B"
        ).pack(anchor="w", pady=(0, 15))

        # Pencarian
        search_frame = tk.Frame(self.content, bg=BG)
        search_frame.pack(fill="x", pady=5)

        tk.Label(
            search_frame,
            text="Cari paket:",
            bg=BG,
            font=("Arial", 10, "bold")
        ).pack(side="left")

        self.search_var = tk.StringVar()

        search_entry = ttk.Entry(
            search_frame,
            textvariable=self.search_var,
            width=35
        )
        search_entry.pack(side="left", padx=10)

        self.search_var.trace_add(
            "write",
            lambda *args: self.populate_packages()
        )

        # Filter
        self.level_var = tk.StringVar(value="Semua")

        ttk.Combobox(
            search_frame,
            textvariable=self.level_var,
            values=["Semua", "Mudah", "Sedang", "Sulit"],
            state="readonly",
            width=12
        ).pack(side="left")

        self.level_var.trace_add(
            "write",
            lambda *args: self.populate_packages()
        )

        # Daftar paket
        container = tk.Frame(self.content, bg=BG)
        container.pack(fill="both", expand=True, pady=10)

        self.canvas = tk.Canvas(
            container,
            bg=BG,
            highlightthickness=0
        )

        scrollbar = ttk.Scrollbar(
            container,
            orient="vertical",
            command=self.canvas.yview
        )

        self.package_frame = tk.Frame(
            self.canvas,
            bg=BG
        )

        self.package_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas_window = self.canvas.create_window(
            (0, 0),
            window=self.package_frame,
            anchor="nw"
        )

        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfigure(
                self.canvas_window,
                width=e.width
            )
        )

        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.populate_packages()

    # --------------------------------------
    # MENAMPILKAN KARTU PAKET
    # --------------------------------------

    def populate_packages(self):

        for widget in self.package_frame.winfo_children():
            widget.destroy()

        keyword = self.search_var.get().lower()
        level = self.level_var.get()

        for index, item in enumerate(self.packages):

            name, difficulty, description, features, challenges = item

            if keyword not in name.lower() and keyword not in description.lower():
                continue

            if level != "Semua" and difficulty != level:
                continue

            done = len(self.progress.get(str(index), []))

            card = tk.Frame(
                self.package_frame,
                bg=WHITE,
                bd=1,
                relief="solid"
            )

            card.pack(fill="x", pady=6, padx=5)

            left = tk.Frame(card, bg=WHITE)
            left.pack(side="left", fill="both", expand=True, padx=15, pady=12)

            tk.Label(
                left,
                text=f"PAKET {index + 1:02d} - {name}",
                font=("Arial", 12, "bold"),
                bg=WHITE,
                fg=DARK
            ).pack(anchor="w")

            tk.Label(
                left,
                text=description,
                font=("Arial", 9),
                bg=WHITE,
                fg="#64748B"
            ).pack(anchor="w", pady=4)

            tk.Label(
                left,
                text=f"Tingkat: {difficulty}  |  Checklist: {done}/5",
                font=("Arial", 9, "bold"),
                bg=WHITE,
                fg=GREEN
            ).pack(anchor="w")

            ttk.Button(
                card,
                text="Pilih Paket",
                command=lambda i=index: self.show_detail(i)
            ).pack(side="right", padx=20, pady=20)

    # --------------------------------------
    # DETAIL PAKET
    # --------------------------------------

    def show_detail(self, index):

        self.selected_index = index

        self.clear_content()

        name, difficulty, description, features, challenges = self.packages[index]

        top = tk.Frame(self.content, bg=BG)
        top.pack(fill="x")

        ttk.Button(
            top,
            text="← Kembali",
            command=self.show_package_list
        ).pack(side="left")

        tk.Label(
            top,
            text=f"PAKET {index + 1:02d}",
            font=("Arial", 12, "bold"),
            bg=BG,
            fg=PRIMARY
        ).pack(side="right")

        tk.Label(
            self.content,
            text=name,
            font=("Arial", 21, "bold"),
            bg=BG,
            fg=DARK
        ).pack(anchor="w", pady=(15, 5))

        tk.Label(
            self.content,
            text=f"Tingkat Kesulitan: {difficulty}",
            font=("Arial", 10, "bold"),
            bg=BG,
            fg=GREEN
        ).pack(anchor="w")

        tk.Label(
            self.content,
            text=description,
            font=("Arial", 11),
            bg=BG,
            fg="#475569",
            wraplength=950,
            justify="left"
        ).pack(anchor="w", pady=12)

        # Fitur aplikasi
        self.section_title("A. Fitur yang Harus Dibuat")

        for feature in features:
            self.bullet(feature)

        # Tantangan
        self.section_title("B. Tantangan Praktikum")

        for challenge in challenges:
            self.bullet(challenge)

        # Checklist
        self.section_title("C. Checklist Pengerjaan")

        checklist = [
            "Membuat struktur file HTML, CSS, dan JavaScript",
            "Membuat tampilan menggunakan HTML dan CSS",
            "Menambahkan fungsi JavaScript",
            "Melakukan pengujian aplikasi",
            "Membuat laporan dokumentasi project"
        ]

        saved = self.progress.get(str(index), [])

        self.check_vars = []

        for i, task in enumerate(checklist):

            var = tk.BooleanVar(value=i in saved)
            self.check_vars.append(var)

            tk.Checkbutton(
                self.content,
                text=task,
                variable=var,
                command=lambda: self.save_progress(index),
                bg=BG,
                activebackground=BG,
                font=("Arial", 10)
            ).pack(anchor="w", pady=3)

        ttk.Button(
            self.content,
            text="Simpan Progress",
            command=lambda: self.save_progress(index, notify=True)
        ).pack(anchor="w", pady=15)

    # --------------------------------------
    # KOMPONEN HALAMAN
    # --------------------------------------

    def section_title(self, title):

        tk.Label(
            self.content,
            text=title,
            font=("Arial", 12, "bold"),
            bg=BG,
            fg=DARK
        ).pack(anchor="w", pady=(14, 5))

    def bullet(self, text):

        tk.Label(
            self.content,
            text="• " + text,
            font=("Arial", 10),
            bg=BG,
            fg="#334155"
        ).pack(anchor="w", padx=10, pady=2)

    # --------------------------------------
    # SIMPAN PROGRESS
    # --------------------------------------

    def save_progress(self, index, notify=False):

        completed = [
            i for i, var in enumerate(self.check_vars)
            if var.get()
        ]

        self.progress[str(index)] = completed

        save_json(PROGRESS_FILE, self.progress)

        if notify:
            messagebox.showinfo(
                "Progress",
                f"Progress Paket {index + 1} berhasil disimpan."
            )

    # --------------------------------------
    # PANDUAN
    # --------------------------------------

    def show_guide(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="PANDUAN PENGGUNAAN",
            font=("Arial", 20, "bold"),
            bg=BG,
            fg=DARK
        ).pack(anchor="w", pady=10)

        guide = [
            "1. Pilih menu Daftar Paket.",
            "2. Pilih salah satu dari 31 paket project.",
            "3. Baca deskripsi dan fitur aplikasi.",
            "4. Kerjakan project menggunakan HTML, CSS, dan JavaScript.",
            "5. Centang checklist setelah menyelesaikan setiap tahapan.",
            "6. Klik Simpan Progress.",
            "7. Progress tersimpan otomatis di folder data."
        ]

        for text in guide:
            tk.Label(
                self.content,
                text=text,
                font=("Arial", 11),
                bg=BG,
                fg="#334155"
            ).pack(anchor="w", pady=7)

        tk.Label(
            self.content,
            text="Teknologi Praktikum",
            font=("Arial", 13, "bold"),
            bg=BG,
            fg=DARK
        ).pack(anchor="w", pady=(20, 8))

        for text in ["HTML5", "CSS3", "JavaScript", "DOM Manipulation",
                     "Event Listener", "Array dan Object", "LocalStorage"]:
            self.bullet(text)

    # --------------------------------------
    # BERSIHKAN HALAMAN
    # --------------------------------------

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()


# ==========================================
# MENJALANKAN APLIKASI
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "TButton",
        font=("Arial", 9, "bold"),
        padding=7
    )

    style.configure(
        "TCombobox",
        padding=5
    )

    app = LabWebApp(root)

    root.mainloop()
