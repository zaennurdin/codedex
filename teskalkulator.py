print("==================")  # Judul
print("Area Calculator 📐")
print("==================")

print("1. Segitiga")
print("2. Persegi Panjang")
print("3. Kotak")
print("4. Lingkaran")

print("==================")
print("Pilih Bentuk:")
print("==================")

pilihan = int(input("Masukkan pilihan: "))  # Setelah Judul
if pilihan == 1:  # Masuk ke metode IF
    alas = float(input("Masukkan alas: "))  # Input
    tinggi = float(input("Masukkan tinggi: "))  # Input
    segitiga = alas * tinggi / 2  # Rumus di masukan setelah input angka
    print("Luas segitiga:", segitiga)  # print
elif pilihan == 2:
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    persegi_panjang = panjang * lebar
    print("Luas persegi panjang:", persegi_panjang)
elif pilihan == 3:
    sisi = float(input("Masukkan sisi: "))
    kotak = sisi * sisi
    print("Luas kotak:", kotak)
elif pilihan == 4:
    jari_jari = float(input("Masukkan jari-jari: "))
    lingkaran = 3.14 * jari_jari * jari_jari
    print("Luas lingkaran:", lingkaran)
else:
    print("Pilihan tidak valid")

print("==================")
