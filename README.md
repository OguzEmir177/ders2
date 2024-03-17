import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
cevap = int(input("şifrenizin kaç karakter olmasını istersiniz?"))
sifre = ""
for i in range(cevap):
    sifre = sifre + random.choice(karakter)
print(sifre)
