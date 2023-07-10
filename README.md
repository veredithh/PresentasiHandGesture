# PresentasiHandGesture

**Persyaratan Sistem Minimum**:
> Microsoft® Windows® **64-bit 8/10/11**,
> **RAM 8GB** atau lebih,
> Ruang disk **minimum 1 GB**,
> Resolusi layar **minimum 1920 x 1080**,
> Kamera/Webcam dengan resolusi **minimum 480p** dengan frame rate yang tidak patah-patah.
> Untuk alternatif dapat menginstall aplikasi Iriun Webcam, yang dapat membuat smartphone menjadi webcam.

**Instalasi**:
1. Pastikan **Python telah terinstal** di komputer Anda. Jika belum, Anda dapat mengunduh Python dari _https://www.python.org/downloads/_ dan mengikuti instruksi instalasi yang disediakan.
2. Buka **terminal** atau **command prompt**.
3. Navigasikan ke direktori proyek ini dengan perintah 'cd'.
4. Jalankan perintah berikut untuk menginstal dependensi yang diperlukan:
   > **pip install -r requirements.txt**
   (Perintah ini akan menginstal semua module yang diperlukan secara otomatis.)
5. Setelah selesai, Anda dapat menjalankan program dengan menjalankan perintah berikut:
   > **python main.py**
   (Gantilah "main.py" dengan nama file program Python yang sesuai.)
6. Folder presentasi dapat diganti dengan _slide_ presentasi yang ingin digunakan. Format _slide_ presentasi disarankan menggunakan '.jpg' dengan ukuran 1280 x 720

**Perintah/Gesture Tangan**:

Untuk memberikan perintah mengendalikan presentasi, user dapat mengangkat jarinya yang kemudian akan menghasilkan perintah sebagai berikut:
1. **Kembali ke _Slide_ Sebelumnya** : Jari Jempol (Hanya berfungsi jika tangan diatas garis hijau)
2. **Lanjut ke _Slide_ Berikutnya** : Jari Telunjuk dan Jari Tengah (Hanya berfungsi jika tangan diatas garis hijau)
3. **_Pointer_** : Jari Telunjuk
4. **Menggambar pada _Slide_** : Jari Telunjuk, Jari Tengah, dan Jari Manis
5. **Menghapus Gambar** : Jari Telunjuk, Jari Tengah, Jari Manis, dan Jari Kelingkung
6. **Keluar dari Aplikasi/_End Program_** : Jari Telunjuk dan Jari Kelingking (Hanya berfungsi jika tangan diatas garis hijau)/Tekan 'Q' pada keyboard
