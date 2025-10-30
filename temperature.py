print("==================")  # Judul
print("Konverter Suhu")
print("==================")

print("1. Konversi Fahrenheit ke Celcius")
print("2. Konversi Celcius ke Fahrenheit")

pilihan = int(input("Masukkan pilihan konversi: "))
if pilihan == 1:
    fahrenheit = int(input("Masukkan suhu dalam Fahrenheit: "))
    celc = (fahrenheit - 32) / 1.8
    print(celc)
elif pilihan == 2:
    celcius = int(input("Masukkan suhu dalam Celcius: "))
    fahrenheit = (celcius * 1.8) + 32
    print(fahrenheit)
else:
    print("Pilihan tidak valid")
