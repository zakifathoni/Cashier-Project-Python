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

### Penggunaan

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

### Method dan attribute

1. `add_item(self, item)`: method ini digunakan untuk menambah item ke list transaksi yang berisi 3 elemen (nama item, jumlah item, dan harga item).
2. `update_item_name(self, name, updated_name)`: method ini digunakan untuk mengubah nama item yang ada di list transaksi. Method ini menerima 2 parameter, yaitu nama item yang akan diubah dan nama baru dari item tersebut.
3. `update_item_qty(self, name, updated_qty)`: method ini digunakan untuk mengubah jumlah item yang ada di list transaksi. Method ini menerima 2 parameter, yaitu nama item yang jumlahnya akan diubah dan jumlah baru dari item tersebut.
4. `update_item_price(self, name, updated_price)`: method ini digunakan untuk mengubah harga item yang ada di list transaksi. Method ini menerima 2 parameter, yaitu nama item yang harganya akan diubah dan harga baru dari item tersebut.
5. `delete_item(self, name)`: method ini digunakan untuk menghapus item yang ada di list transaksi. Method ini menerima 1 parameter, yaitu nama item yang akan dihapus.
6. `reset_transaction(self)`: method ini digunakan untuk mereset data transaksi menjadi kosong dan mengeset total harga dan diskon menjadi 0.
7. `check_order(self)`: method ini digunakan untuk mengecek apakah ada kesalahan input data pada transaksi atau tidak. Jika tidak ada kesalahan, method ini akan menampilkan daftar item yang ada dalam transaksi dalam bentuk tabel yang menampilkan nomor item, nama item, jumlah item, harga item, dan total harga dari setiap item.
8. `hitung_total_price(self)`: method ini digunakan untuk menghitung total harga dari transaksi yang sedang berlangsung dan menentukan diskon yang diterima berdasarkan total harga yang diperoleh.
9. `transaction`: attribute bertipe list ini digunakan untuk menyimpan daftar item yang ada dalam transaksi.
10. `total_price`: attribute bertipe float ini digunakan untuk menyimpan total harga dari transaksi yang sedang berlangsung.
11. `discount`: attribute bertipe float ini digunakan untuk menyimpan persentase diskon yang diterima dari transaksi yang sedang berlangsung.

### Test case:
1. Test Case 1
Menambahkan item dengan method `add_item`

Input
- `transaksi.add_item(["Ayam Goreng", 2, 20000])`
- `transaksi.add_item(["Pasta Gigi", 3, 15000])`
- `print("Item yang dibeli adalah: ", transaksi.transaction)`

output:
Item yang dibeli adalah:  [['Ayam Goreng', 2, 20000], ['Pasta Gigi', 3, 15000]]

2. Test Case 2
Menghapus item dengan method `delete_item`

Input:
transaksi.delete_item("Pasta Gigi")
print("Item yang dibeli setelah didelete : ", transaksi.transaction)

Output:
Item yang dibeli setelah didelete :  [['Ayam Goreng', 2, 20000]]

3. Test Case 3
Menghapus semua data transaksi dengan method `reset_transaction`

Input:
transaksi.reset_transaction()
print("Semua item berhasil dihapus!")

Output:
Semua item berhasil dihapus!

4. Test Case 4
Mengecek data order dengan method `check_order`
Menampilkan total belanja dengan `method total_price`

Input:
transaksi.add_item(["Ayam Goreng", 2, 20000])
transaksi.add_item(["Pasta Gigi", 3, 15000])
transaksi.add_item(["Mainan Mobil", 1, 200000])
transaksi.add_item(["Mie Instan", 5, 3000])
transaksi.hitung_total_price()
transaksi.check_order()

Output:
Total Harga:  300000
Diskon:  5.0 %
Total Harga setelah diskon:  285000.0
Pemesanan sudah benar

![tabel kasir](https://user-images.githubusercontent.com/112263898/214578771-67abe312-8031-4476-a046-4ae746224d56.png)

### Kesimpulan:
Kode di atas merupakan sebuah proyek yang dapat digunakan untuk mengelola transaksi pembelian barang di sebuah toko atau supermarket. Proyek ini menggunakan class Transaction yang memiliki beberapa method seperti add_item, update_item_name, update_item_qty, update_item_price, delete_item, reset_transaction, check_order, dan hitung_total_price. Method-method tersebut digunakan untuk menambah, mengubah, menghapus item, mereset transaksi, memeriksa pemesanan, dan menghitung total harga serta diskon. Proyek ini juga menggunakan library tabulate untuk menampilkan data transaksi dalam bentuk tabel yang rapi.

   - Kritik:
Proyek ini hanya menggunakan metode kondisional untuk menentukan diskon, sehingga jika toko atau supermarket ingin mengubah metode diskon, maka harus mengubah kode program. Sebaiknya dapat menggunakan metode yang lebih fleksibel seperti meng-input diskon dari user atau menggunakan external file untuk menyimpan data diskon.
Proyek ini hanya menggunakan print statement untuk menampilkan data transaksi, sebaiknya dapat digabungkan dengan GUI atau tampilan web untuk lebih memudahkan user dalam melihat data transaksi.
   - Saran:
Untuk menambah fleksibilitas proyek, dapat menambahkan fitur untuk menyimpan data transaksi dalam external file seperti CSV atau database.
Dapat menambahkan fitur pembayaran dan pengiriman barang untuk menyempurnakan proyek ini menjadi sebuah aplikasi e-commerce.
Dapat menambahkan fitur autentikasi user untuk menyimpan data transaksi per user dan meningkatkan keamanan data.
