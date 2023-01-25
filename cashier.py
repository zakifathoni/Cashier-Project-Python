# Import Library
from tabulate import tabulate

class Transaction:
    def __init__(self):
        self.transaction = []
        self.total_price = 0
        self.discount = 0.0
        
    def add_item(self, item):
        self.transaction.append(item)
        self.total_price += item[1] * item[2]
        
    def update_item_name(self, name, updated_name):
        for item in self.transaction:
            if item[0] == name:
                item[0] = updated_name
                
    def update_item_qty(self, name, updated_qty):
        for item in self.transaction:
            if item[0] == name:
                self.total_price -= item[1] * item[2]
                item[1] = updated_qty
                self.total_price += item[1] * item[2]
                
    def update_item_price(self, name, updated_price):
        for item in self.transaction:
            if item[0] == name:
                self.total_price -= item[1] * item[2]
                item[2] = updated_price
                self.total_price += item[1] * item[2]
                
    def delete_item(self, name):
        for item in self.transaction:
            if item[0] == name:
                self.transaction.remove(item)
                self.total_price -= item[1] * item[2]
                
    def reset_transaction(self):
        self.transaction = []
        self.total_price = 0
        self.discount = 0
        
    def check_order(self):
        if len(self.transaction) == 0:
            print("Terdapat kesalahan input data")
        else:
            print("Pemesanan sudah benar")
            table = []
            for i, item in enumerate(self.transaction):
                table.append([i+1, item[0], item[1], item[2], item[1] * item[2]])
            table_header = ["No.", "Nama item", "Jumlah Item", "Harga/Item", "Total Harga"]
            print(tabulate(table, headers=table_header, tablefmt="fancy_grid"))
            
    def hitung_total_price(self):
        if self.total_price > 500_000:
            self.discount = 0.1
        elif self.total_price > 300_000:
            self.discount = 0.08
        elif self.total_price > 200_000:
            self.discount = 0.05
        print("Total Harga: ", self.total_price)
        print("Diskon: ", self.discount*100, "%")
        print("Total Harga setelah diskon: ", self.total_price - (self.total_price * self.discount))