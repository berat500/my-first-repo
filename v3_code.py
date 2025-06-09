try:
    sayi = int(input("Bir sayı girin: "))
    print(f"Girdiğiniz sayı: {sayi}")
except ValueError:
    print("Lütfen geçerli bir sayı girin.")