# Parametre almayan bir fonksiyon
def say_hello():
    print("Merhaba, hoş geldin!")

# Fonksiyonu çağırmak
say_hello()  # Çıktı: Merhaba, hoş geldin!


# Parametre alan ve geri dönüş değeri olan bir fonksiyon
def sum(a, b):
    return a + b

# Fonksiyonu çağırmak
sonuc = sum(10, 5)
print(sonuc)  # Çıktı: 15
