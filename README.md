# Super-Cashier
## Latar Belakang
Kasir sederhana yang dibuat dengan menggunakan bahasa pemrograman Python. Projek ini dibuat berdasarkan kebutuhan pemilik supermarket yang membutuhkan fitur-fitur kasir yang mendukung untuk melaksanakan sistem self-service.

## Requirements / Objectives
Dalam proses pembuatannya, projek ini memiliki beberapa requirements dan objectives. Requirements yang ada diantaranya adalah fitur-fitur kasir seperti menambahkan barang, menghapus barang, mengubah barang, membatalkan pembelian, melakukan check out, hingga menghitung total belanja berdasarkan kondisi tertentu. Objektif dari projek ini adalah customer dapat melihat keseluruhan barang yang dibeli, serta jumlah harga yang perlu dibayar.

## Alur Kode
1. Langkah 1.0, kita akan run main.py yang berfungsi sebagai *Main Class*.
2. Langkah 2.0, kita akan mendapatkan output menu dan kita dapat memberikan input berupa angka dari 1 (satu) sampai dengan 8 (delapan)
3. Langkah 3.0, apabila kita memberi input '1', maka kita akan diminta memasukkan input untuk nama customer dan nomor telepon
4. Langkah 3.1, apabila kita memberi input '2', maka kita akan diminta memasukkan input untuk nama barang, jumlah barang, dan harga barang
5. Langkah 3.2, apabila kita memberi input '3', maka kita akan diminta memasukkan input untuk memilih info item yang ingin dirubah
6. Langkah 3.2.1, apabila kita memberi input '1', maka kita akan diminta memasukkan input untuk nama barang yang ingin diganti dan nama barang baru
7. Langkah 3.2.2, apabila kita memberi input '2', maka kita akan diminta memasukkan input untuk nama barang yang jumlahnya ingin diubah dan jumlah barang baru
8. Langkah 3.2.3, apabila kita memberi input '3', maka kita akan diminta memasukkan input untuk nama barang yang harganya ingin diubah dan harga barang baru
9. Langkah 3.3, apabila kita memberi input '4', maka kita akan diminta memasukkan input untuk nama barang yang ingin dihapus
10. Langkah 3.4, apabila kita memberi input '5', maka kita akan mendapatkan output berupa seluruh item yang telah dimasukkan
11. Langkah 3.5, apabila kita memberi input '6', maka kita akan mendapatkan output berupa seluruh item yang telah dimasukkan serta harga total belanja
12. Langkah 3.6, apabila kita memberi input '7', maka kita akan menghapus seluruh item yang telah dimasukkan sebelumnya
13. Langkah 3.7, apabila kita memberi input '8', maka kita akan menghentikan program
14. Langkah 3.8, apabila kita memberi input diluar dari angka 1 (satu) sampai dengan (8), maka akan keluar output "Pilihan salah"
15. Langkah 4.0, program selesai

## Penjelasan Kode
Script main.py berfungsi sebagai *Main Class* yang harus di run pertama kali untuk memunculkan program yang telah dibuat. Didalamnya terdapat function main() sebagai fungsi utama dan menu() untuk menampilkan menu yang dapat user pilih, dan if function untuk memanggil function lainnya.

```
def main():
    '''Fungsi utama untuk menjalankan program
    '''
    while(True):
        menu()
        try:
            '''membuat exception handling apabila terjadi kesalahan 
            atau error dalam program
            '''
            menu_inp = int(input("Masukan pilihan anda: ") )
            if(menu_inp == 1):
                '''branching ini akan dijalankan apabila user menginput '1' 
                '''
                nama_customer = (input("Masukan nama customer: "))
                no_telp = (input("Masukan nomor telepon: "))
                trnsct_123 = module.transaction(nama_customer, no_telp) # membuat ID transaksi customer 
                print("Data customer berhasil diinputkan")

            elif menu_inp == 2:
                '''branching ini akan dijalankan apabila user menginput '2' 
                '''
                nama_item = input("Masukan nama barang: ")
                jumlah_item = str((input("Masukan jumlah barang: ")))
                harga_item = str((input("Masukkan harga barang: ")))
                module.add_item(nama_item, jumlah_item, harga_item)
                print("Data barang berhasil diinputkan")

            elif menu_inp == 3:
                '''branching ini akan dijalankan apabila user menginput '3' 
                '''
                print("Pilihan edit: ")
                print("1. Nama item")
                print("2. Jumlah barang")
                print("3. Harga barang")
                try:
                    update_inp = int(input("Masukan jenis nilai yang ingin diedit: "))
                    if update_inp == 1:
                        '''nested branching ini akan dijalankan apabila user menginput '1' 
                        '''
                        nama_item = input("Masukan nama barang: ")
                        nama_item_baru =  input("Masukan nama barang baru: ")
                        module.update_item_name(nama_item, nama_item_baru)
                        print("Nama barang berhasil diupdate")
                    elif update_inp == 2:
                        '''nested branching ini akan dijalankan apabila user menginput '2' 
                        '''
                        nama_item = input("Masukan nama barang: ")
                        jumlah_item = (input("Masukkan jumlah item: "))
                        module.update_item_qty(nama_item, jumlah_item)
                        print("Nama barang berhasil diupdate")
                    elif update_inp == 3:
                        '''nested branching ini akan dijalankan apabila user menginput '3' 
                        '''
                        nama_item = input("Masukan nama barang: ")
                        harga_item = (input("Masukkan harga item: "))
                        module.update_item_price(nama_item, harga_item)
                        print("Nilai barang berhasil diupdate")
                    else: 
                        '''nested branching ini akan dijalankan apabila user tidak menginput sesuai yang diminta 
                        '''
                        print("Pilihan salah")

                except ValueError:
                    '''exception error ini akan muncul apabila terdapat value error
                    '''
                    print("Terdapat kesalahan input value")

                except Exception:
                    '''exception error ini akan muncul apabila terdapat error yang belum di spesifikan
                    '''
                    print("Terdapat kesalahan")
                
            elif menu_inp == 4:
                '''branching ini akan dijalankan apabila user menginput '4' 
                '''
                nama_item = input("Masukan nama barang: ")
                print("Berhasil menghapus data barang")
                module.delete_item(nama_item)

            elif menu_inp == 5:
                '''branching ini akan dijalankan apabila user menginput '5' 
                '''
                print("Order anda: ")
                module.check_order()

            elif menu_inp == 6:
                '''branching ini akan dijalankan apabila user menginput '6' 
                '''
                module.check_out()

            elif menu_inp == 7:
                '''branching ini akan dijalankan apabila user menginput '7' 
                '''
                print("Barang telah dihapus semua")
                module.reset_transaction()

            elif menu_inp == 8:
                '''branching ini akan dijalankan apabila user menginput '8' 
                '''
                print("Anda telah keluar!")
                return False
            else:
                '''branching ini akan dijalankan apabila user tidak menginput sesuai yang diminta 
                '''
                print("Pilihan salah")
                
        except ValueError:
            print("Terdapat kesalahan input value")

        except Exception:
            print("Terdapat kesalahan")
```
```
def menu():
    '''Fungsi untuk menampilkan pilihan-pilihan yang dapat user pilih'''
    print("Menu: ")
    print("1. Membuat ID Customer") #transaction
    print("2. Menambahkan barang") #add item
    print("3. Update info item") #update item name
    print("4. Menghapus item") #delete item
    print("5. Mengecek order") #check order
    print("6. Check out") #check out
    print("7. Batal belanja") #reset transaction
    print("8. Keluar")
```
```
if __name__ == "__main__":
    '''Digunakan untuk memanggil function main()
    '''
    main()
```
