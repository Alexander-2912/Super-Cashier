'''Program utama yang digunakan untuk menampilkan menu utama
   yang juga digunakan sebagai tempat dimana user memberikan input
'''

import module

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

if __name__ == "__main__":
    main()