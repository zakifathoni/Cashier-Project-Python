# Cashier-Project-Python-Pacmann
Repository ini berisi kode python untuk membuat objek transaksi yang dapat menambahkan, mengupdate, menghapus, dan menampilkan item yang dibeli serta menghitung total harga dan diskon yang diterima.

# Flowchart



# Penggunaan:

1. Import library `tabulate` dengan perintah `from tabulate import tabulate`.
2. Buat objek transaksi dengan membuat instance dari kelas `Transaction`, misal `transaksi = Transaction()`.
3. Gunakan method `add_item` untuk menambahkan item ke dalam transaksi, dengan format `transaksi.add_item(["nama item", jumlah item, harga/item])`.
4. Gunakan method `update_item_name`, `update_item_qty`, dan `update_item_price` untuk mengupdate nama item, jumlah item, dan harga/item.
5. Gunakan method `delete_item` untuk menghapus item dari transaksi.
6. Gunakan method `reset_transaction` untuk menghapus semua item dari transaksi.
7. Gunakan method `check_order` untuk menampilkan daftar item yang dibeli dalam bentuk tabel.
8. Gunakan method `hitung_total_price` untuk menghitung total harga dan diskon yang diterima.

> Note: Pada kode di atas, diskon yang diterima ditentukan berdasarkan total harga transaksi. Jika total harga > 500_000 maka diskon yang diterima adalah 10%, jika total harga > 300_000 maka diskon yang diterima adalah 8%, dan jika total harga > 200_000 maka diskon yang diterima adalah 5%. Anda dapat mengubah persentase diskon sesuai dengan kebutuhan Anda dengan mengubah kondisi pada method `hitung_total_price()`.

Selain itu, Anda juga dapat menambahkan atau mengubah fitur lain pada kelas `Transaction` sesuai dengan kebutuhan Anda. Contohnya Anda dapat menambahkan feature untuk menambahkan customer name atau no.invoice pada transaksi.
