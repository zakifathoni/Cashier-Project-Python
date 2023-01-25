# CASHIER PROJECT PACMANN

### Latar Belakang
Sistem kasir yang dikembangkan dengan bahasa pemrograman Python ini dirancang untuk memberikan kenyamanan dan kemudahan bagi pelanggan dalam melakukan transaksi belanja di supermarket. Tujuan utama dari sistem ini adalah untuk memfasilitasi pelanggan dalam memasukkan item yang ingin dibeli, jumlah item, dan harga per item. Selain itu, pelanggan juga dapat melakukan pengubahan data transaksi yang telah dibuat, seperti mengubah data item, jumlah item, atau harga per item. Dalam hal ini, pelanggan dapat menghapus item yang tidak ingin dibeli dengan menghapus satu item atau mereset data transaksi secara keseluruhan. Selain itu, pelanggan juga dapat melihat data order yang telah diinput sebelumnya dan melihat total harga dari semua item yang dipilih.

### Requirements
1. Merancang sistem kasir yang dapat mempermudah pelanggan dalam menambah item yang ingin dibeli, beserta jumlah item dan harga item tersebut:
  - Membuat fitur untuk mengubah nama item yang ingin dibeli dalam sistem kasir.
  - Menyediakan opsi untuk mengubah jumlah item yang dipilih dalam transaksi.
  - Membuat fitur untuk mengubah harga item yang dipilih dalam transaksi.
  - Menyediakan fitur untuk menghapus item yang tidak jadi dibeli dalam transaksi.
  - Membuat opsi untuk mereset semua data transaksi dalam sistem kasir.
  - Menyediakan fitur untuk mengecek data order yang sudah dibuat dalam sistem kasir.
  - Membuat fitur untuk melihat total harga keseluruhan item yang dipilih dalam transaksi.
2. Membuat project sistem kasir menggunakan bahasa pemrograman Python.
3. Mengimplementasikan materi function, branching, dan data structure dalam pengembangan sistem kasir.
4. Menyertakan konsep OOP dalam program yang dirancang untuk sistem kasir.

### Flowchart

![FLOWCHART KASIR](https://user-images.githubusercontent.com/112263898/214484345-83c23672-da60-4c0c-ae48-aaa5467ae91c.png)

### Penggunaan:

1. Import library `tabulate` dengan perintah `from tabulate import tabulate`.
2. Buat objek transaksi dengan membuat instance dari kelas `Transaction`.
3. Gunakan method `add_item` untuk menambahkan item ke dalam transaksi.
4. Gunakan method `update_item_name`, `update_item_qty`, dan `update_item_price` untuk mengupdate nama item, jumlah item, dan harga/item.
5. Gunakan method `delete_item` untuk menghapus item dari transaksi.
6. Gunakan method `reset_transaction` untuk menghapus semua item dari transaksi.
7. Gunakan method `check_order` untuk menampilkan daftar item yang dibeli dalam bentuk tabel.
8. Gunakan method `hitung_total_price` untuk menghitung total harga dan diskon yang diterima.

> Note: Pada kode di atas, diskon yang diterima ditentukan berdasarkan total harga transaksi. Jika total harga > 500_000 maka diskon yang diterima adalah 10%, jika total harga > 300_000 maka diskon yang diterima adalah 8%, dan jika total harga > 200_000 maka diskon yang diterima adalah 5%. Anda dapat mengubah persentase diskon sesuai dengan kebutuhan Anda dengan mengubah kondisi pada method `hitung_total_price()`.

- Selain itu, Anda juga dapat menambahkan atau mengubah fitur lain pada kelas `Transaction` sesuai dengan kebutuhan Anda. Contohnya Anda dapat menambahkan feature untuk menambahkan customer name atau no.invoice pada transaksi.
