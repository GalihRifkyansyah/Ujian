# BANK Easy
# menu: 1. pengelolaan rekening dan saldo
#       2. Transaksi Perbankan
#       3. Riwayat Tranksaksi
#       4. Sistem Manajemen Rekening

def show_menu_home():
    print("""
===========================
SELAMAT DATANG DI BANK EASY
===========================
1. Data Rekening dan Saldo
2. Transaksi Perbankan
3. Riwayat Transaksi
4. Sistem Manajemen Rekening
5. Exit
""") 
             
def data_rekening_dan_saldo():
    print('\nNasabah Baru :')
    nama = input('Masukkan nama anda: ')
    saldo = int(input('Masukkan saldo anda: '))
    print(f'Rekening Baru dengan nama {nama}, Deposit awal {saldo}')
    

def main():
 
    
    while True:
        show_menu_home()
        inputan = input ('pilih menu (1-5) : ')
        if input == '1':
             data_rekening_dan_saldo()
        elif input == '2':
            transaksi_perbankan()
        elif input == '3': 
            riwayat_transaksi()
        elif input == '4':
            sistem_manajemen_rekening()
        elif input == '5':
            print('Terimakasih sudah Transaksi di Bank Easy ')
            break
        else:
            print('Inputan Error' )

if __name__ == '__main__':
    main()
