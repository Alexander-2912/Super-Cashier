'''Module ini berisi fungsi-fungsi yang akan dipanggil dan digunakan'''

nama_customer = None
no_telp = None
list_customer_barang = []

#1
def transaction(nama_customerr, no_telpp):
    '''Fungsi untuk menerima parameter nama_customerr dan no_telp
       serta mengecek apakah tipe data yang diterima telah sesuai dengan yang diinginkan
    '''
    if type(nama_customerr) != str:
        return False
    if type(no_telpp) != float:
        return False
    nama_customer = nama_customerr
    no_telp = no_telpp
    return True

#2
def add_item(nama_item, jumlah_item, harga_per_item):
    '''Fungsi untuk menerima parameter nama_item, jumlah_item, dan harga_per_item
       nilai yang diterima akan disimpan kedalam list list_customer_barang
    '''
    print("item yang dibeli adalah: " , nama_item  , "      ", str(jumlah_item) , "      ", str(harga_per_item))
    list_customer_barang.append([nama_item, jumlah_item, harga_per_item])

#3
def update_item_name(nama_item, nama_item_baru):
    '''Fungsi untuk menerima parameter nama_item, dan nama_item_baru
       Fungsi ini digunakan untuk mengganti nama item yang telah dimasukkan sebelumnya
       dengan nama yang baru
    '''
    for nama in list_customer_barang:
        if nama[0] == nama_item:
            nama[0] = nama_item_baru
    return True

def update_item_qty(nama_item, jumlah_item):
    '''Fungsi untuk menerima parameter nama_item, dan jumlah_item
       Fungsi ini digunakan untuk mengganti jumlah item yang telah dimasukkan sebelumnya
       dengan jumlah item yang baru
    '''
    for nama in list_customer_barang:
        if nama[0] == nama_item:
            nama[1] = jumlah_item
    return True

def update_item_price(nama_item, harga_item):
    '''Fungsi untuk menerima parameter nama_item, dan harga_item
       Fungsi ini digunakan untuk mengganti harga item yang telah dimasukkan sebelumnya
       dengan harga item yang baru
    '''
    for nama in list_customer_barang:
        if nama[0] == nama_item:
            nama[2] = harga_item
    return True

#4
def delete_item(nama_item):
    '''Fungsi untuk menerima parameter nama_item
       Fungsi ini digunakan untuk menghapus barang yang telah dimasukkan sebelumnya
       menggunakan nama item yang ingin dihapus
    '''
    for index, nama in enumerate(list_customer_barang):
        if nama[0] == nama_item:
            break
    list_customer_barang.pop(index)
    print(list_customer_barang)
    return True

#5
def check_order():
    '''Fungsi ini digunakan untuk mencetak seluruh item yang dimasukkan
       serta mengecek apakah ada kesalahan input data
    '''
    for nama in list_customer_barang:
        if nama[0] == "" or nama[1] == "" or nama[2] == "":
            print("Terdapat kesalahan input data")
            break
    else:
        print("Pemesanan sudah benar")
        print(list_customer_barang)
    return True

nomor_id = 0 # diletakkan di luar fungsi agar tidak merubah nilai variabel menjadi 0 setiap kali dijalankan
def number():
    '''Fungsi ini digunakan untuk membuat increment pada nomor_id'''
    global nomor_id
    nomor_id += 1

#6
def check_out():
    '''Fungsi ini digunakan untuk menghitung total harga, diskon, dan harga setelah diskon
       kepada item-item yang telah dimasukkan sebelumnya
    '''
    number()
    total_harga = 0
    jumlah_akhir = 0
    diskon = 0
    harga_diskon = 0

    for nama in list_customer_barang:
        total_harga = int(nama[1]) * int(nama[2])
        jumlah_akhir = total_harga + jumlah_akhir

    if jumlah_akhir > 200000 and jumlah_akhir <= 300000:
        diskon = jumlah_akhir*0.05
        harga_diskon = jumlah_akhir - diskon

    elif jumlah_akhir > 300000 and jumlah_akhir <= 500000:
        diskon = jumlah_akhir*0.06
        harga_diskon = jumlah_akhir - diskon

    elif jumlah_akhir > 500000:
        diskon = jumlah_akhir*0.07
        harga_diskon = jumlah_akhir - diskon

    else:
        diskon = 0
        harga_diskon = jumlah_akhir - diskon
    print("Item yang dibeli adalah: ", list_customer_barang)
    print("Total harga belanja: ", harga_diskon)
    return True
        

def reset_transaction():
    '''Fungsi untuk menghapus seluruh item yang telah digunakan sebelumnya'''
    list_customer_barang.clear()
    return True