# program_kalkulator.py

from modul_kalkulator import tambah, kurang, kali, bagi

def tampilkan_menu():
    """Menampilkan menu pilihan operasi kalkulator."""
    print("=== Kalkulator ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1/2/3/4/5): ")

        if pilihan == '5':
            print("Terima kasih telah menggunakan kalkulator!")
            break

        if pilihan in ['1', '2', '3', '4']:
            try:
                a = float(input("Masukkan angka pertama: "))
                b = float(input("Masukkan angka kedua: "))
            except ValueError:
                print("Input tidak valid, harap masukkan angka.")
                continue

            if pilihan == '1':
                print(f"Hasil: {tambah(a, b)}")
            elif pilihan == '2':
                print(f"Hasil: {kurang(a, b)}")
            elif pilihan == '3':
                print(f"Hasil: {kali(a, b)}")
            elif pilihan == '4':
                print(f"Hasil: {bagi(a, b)}")
        else:
            print("Pilihan tidak valid, silakan pilih lagi.")

if __name__ == "__main__":
    main()
