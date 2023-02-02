# Import Library
from tabulate import tabulate

# Membuat class Transaction
class Transaction:
    # Membuat method constructor 
    def __init__(self):
        """
        Inisialisasi atribut pada class Transaction.
        Atribut yang didefinisikan:
        - transaction (list) : list untuk menyimpan item-item yang dibeli
        - total_price (int) : total harga dari semua item yang dibeli
        - discount (float) : diskon yang diterima dari total harga
        """
        self.transaction = []
        self.total_price = 0
        self.discount = 0.0
        
    # Membuat method add_item    
    def add_item(self, item):
        """
        Method untuk menambahkan item ke dalam transaksi.
        Parameter yang diterima:
        - item (list) : list yang berisi informasi item, berupa [nama item, jumlah item, harga/item]
        """
        self.transaction.append(item)
        self.total_price += item[1] * item[2]
    
    # Membuat method update_item_name
    def update_item_name(self, name, updated_name):
        """
        Method untuk mengubah nama item yang sudah ditambahkan ke dalam transaksi.
        Parameter yang diterima:
        - name (str) : nama item sebelum diubah
        - updated_name (str) : nama item setelah diubah
        """
        for item in self.transaction:
            if item[0] == name:
                item[0] = updated_name
    
    # Membuat method update_item_qty
    def update_item_qty(self, name, updated_qty):
        """
        Method untuk mengubah jumlah item yang sudah ditambahkan ke dalam transaksi.
        Parameter yang diterima:
        - name (str) : nama item yang jumlahnya akan diubah
        - updated_qty (int) : jumlah item setelah diubah
        """
        for item in self.transaction:
            if item[0] == name:
                self.total_price -= item[1] * item[2]
                item[1] = updated_qty
                self.total_price += item[1] * item[2]
    
    # Membuat method update_item_price
    def update_item_price(self, name, updated_price):
        """
        Method untuk mengubah harga item yang sudah ditambahkan ke dalam transaksi.
        Parameter yang diterima:
        - name (str) : nama item yang harganya akan diubah
        - updated_price (float) : harga item setelah diubah
        """
        for item in self.transaction:
            if item[0] == name:
                self.total_price -= item[1] * item[2]
                item[2] = updated_price
                self.total_price += item[1] * item[2]
                
    # Membuat method delete_item
    def delete_item(self, name):
        """
        Method ini digunakan untuk menghapus item dari daftar transaksi.
        Parameter:
        - name (str) : Nama item yang akan dihapus dari daftar transaksi.
        """
        for item in self.transaction:
            if item[0] == name:
                self.transaction.remove(item)
                self.total_price -= item[1] * item[2]
    
    # Membuat method reset_transaction
    def reset_transaction(self):
        """
        Mereset data transaksi menjadi kosong dan total harga menjadi 0.
        """
        self.transaction = []
        self.total_price = 0
        self.discount = 0
                    
    # Membuat method hitung_total_price
    def hitung_total_price(self):
        """
        Menghitung total harga transaksi, diskon dan total harga setelah diskon.
        """
        if self.total_price > 500_000:
            self.discount = 0.1
        elif self.total_price > 300_000:
            self.discount = 0.08
        elif self.total_price > 200_000:
            self.discount = 0.05
        print("Total Harga: ", self.total_price)
        print("Diskon: ", self.discount*100, "%")
        print("Total Harga setelah diskon: ", self.total_price - (self.total_price * self.discount))
   
    # Membuat method check_order
    def check_order(self):
        """
        Method ini digunakan untuk memeriksa apakah transaksi sudah benar atau belum.
        Jika tidak ada item yang ditambahkan, maka akan muncul pesan "Terdapat kesalahan input data".
        Jika sudah benar, maka akan ditampilkan daftar item yang dibeli dalam bentuk tabel.
        """
        if len(self.transaction) == 0:
            print("Terdapat kesalahan input data")
        else:
            print("Pemesanan sudah benar")
            table = []
            for i, item in enumerate(self.transaction):
                table.append([i+1, item[0], item[1], item[2], item[1] * item[2]])
            table_header = ["No.", "Nama item", "Jumlah Item", "Harga/Item", "Total Harga"]
            print(tabulate(table, headers=table_header, tablefmt="fancy_grid"))
