Oke ✅ berikut **README.md lengkap dan profesional** untuk versi **final dashboard** kamu — yang punya **4 KPI, 4 grafik (termasuk pie chart)**, serta **sidebar meluncur (offcanvas)**.
File ini siap kamu lampirkan untuk tugas di Google Drive atau GitHub.

---

## 🧾 README.md — E-Commerce Sales Dashboard


# 🛒 E-Commerce Sales Dashboard

Dashboard interaktif berbasis **Dash (Plotly + Bootstrap)** untuk menganalisis data penjualan toko online (e-commerce).  
Aplikasi ini menampilkan **indikator KPI**, **grafik interaktif**, dan **sidebar filter meluncur** yang memudahkan pengguna dalam memantau performa penjualan secara dinamis.

---

## 🚀 Fitur Utama

✅ **4 KPI Utama**
- 💰 Total Penjualan  
- 📦 Total Transaksi  
- 🛍️ Rata-rata Penjualan  
- 🏆 Kategori Terlaris  

✅ **4 Grafik Interaktif**
1. **Line Chart** – Tren penjualan bulanan  
2. **Bar Chart** – Penjualan per kategori  
3. **Line Chart** – Rata-rata penjualan harian  
4. **Pie/Donut Chart** – Proporsi kontribusi penjualan per kategori  

✅ **Sidebar Meluncur (Offcanvas Filter)**
- Pilih **tahun**, **kategori produk**, dan **rentang tanggal**  
- Sidebar muncul dari sisi kiri saat tombol ⚙️ diklik (seperti Streamlit sidebar)

✅ **Desain Profesional**
- Menggunakan tema Bootstrap **SANDSTONE**  
- Warna lembut, rapi, responsif, dan cocok untuk laporan akademik  
- Tombol filter di **pojok kiri atas** untuk akses cepat  

---

## 🧠 Arsitektur Sistem

```

📂 Project Directory
│
├── app_dash_sales_final_pie.py   # File utama aplikasi
├── data/
│   └── sales_data.csv            # Dataset dummy penjualan
├── requirements.txt              # Daftar dependensi
└── README.md                     # Dokumentasi proyek

````

**Alur sistem:**
1. Aplikasi membaca data CSV (`sales_data.csv`) menggunakan `pandas`.
2. Sidebar (Offcanvas) digunakan untuk memilih filter waktu dan kategori.
3. Callback Dash secara otomatis memperbarui semua grafik dan KPI berdasarkan filter.
4. Visualisasi ditampilkan dengan `plotly.express` menggunakan layout responsif Bootstrap.

---

## 📊 Contoh Dataset

File `data/sales_data.csv` berisi data dummy dengan kolom:

| Kolom | Deskripsi |
|--------|------------|
| `Date` | Tanggal transaksi (2023–2025) |
| `Category` | Kategori produk (Electronics, Fashion, Home, dsb) |
| `Sales` | Nilai total penjualan dalam rupiah |

Contoh data:

| Date | Category | Sales |
|------|-----------|-------|
| 2024-01-05 | Electronics | 15,000,000 |
| 2024-01-15 | Fashion | 7,000,000 |
| 2024-02-10 | Home | 5,500,000 |

---

## ⚙️ Framework & Library yang Digunakan

| Library | Fungsi |
|----------|--------|
| **Dash** | Framework utama untuk aplikasi web Python. |
| **Plotly Express** | Membuat grafik interaktif dengan cepat. |
| **Dash Bootstrap Components** | Menyediakan tema dan layout modern. |
| **Pandas** | Membaca dan memproses data dari CSV. |

---

## 📦 Requirements

Isi file `requirements.txt`:

```txt
dash==3.0.0
dash-bootstrap-components==1.6.0
pandas==2.2.3
plotly==5.24.1
````

---

## 🧩 Cara Menjalankan Aplikasi

1. **Clone atau ekstrak proyek ini**

   ```bash
   git clone https://github.com/yourusername/ecommerce-dashboard
   cd ecommerce-dashboard
   ```

2. **(Opsional) Buat virtual environment**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   ```

3. **Install dependensi**

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**

   ```bash
   python app_dash_sales_final_pie.py
   ```

5. **Akses dashboard di browser**

   ```
   http://localhost:8050
   ```

---

## 🎨 Tampilan Antarmuka

* Navbar biru elegan dengan tombol ⚙️ Filter di kiri atas
* Sidebar meluncur dari kiri (Offcanvas Filter)
* Empat kartu KPI berjejer di atas grafik
* Empat grafik responsif di bawahnya (Line, Bar, Line, Pie)
* Tampilan ringan, rapi, dan interaktif

---

## 🧠 Ide Pengembangan Lanjutan

✨ Tambahkan **tabel Top 10 Produk Terlaris** di bawah grafik.
✨ Integrasikan dengan **database MySQL/PostgreSQL** agar data bisa real-time.
✨ Gunakan **`dcc.Interval`** untuk update otomatis (live dashboard).
✨ Tambahkan **download button** (ekspor CSV atau gambar grafik).
✨ Ubah tema ke `dbc.themes.MATERIA` untuk tampilan glossy modern.

---

## 📜 Lisensi

Proyek ini menggunakan lisensi **MIT** — bebas digunakan untuk keperluan akademik dan pembelajaran.



👨‍💻 **Dibuat oleh:**
**Yusuf Rajabi**
