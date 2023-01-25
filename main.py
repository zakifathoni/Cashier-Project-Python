from cashier import Transaction
transaksi = Transaction()

# Test Case 1
print("Test Case 1")

transaksi.add_item(["Ayam Goreng", 2, 20000])
transaksi.add_item(["Pasta Gigi", 3, 15000])
print("Item yang dibeli adalah: ", transaksi.transaction)
print(" ")

# Test Case 2
print("Test Case 2")

transaksi.delete_item("Pasta Gigi")
print("Item yang dibeli setelah didelete : ", transaksi.transaction)
print(" ")

# Test Case 3
print("Test Case 3")

transaksi.reset_transaction()
print("Semua item berhasil dihapus!")
print(" ")

# Test Case 4
print("Test Case 4")

transaksi.add_item(["Ayam Goreng", 2, 20000])
transaksi.add_item(["Pasta Gigi", 3, 15000])
transaksi.add_item(["Mainan Mobil", 1, 200000])
transaksi.add_item(["Mie Instan", 5, 3000])
transaksi.hitung_total_price()
transaksi.check_order()