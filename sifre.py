import random
import string

def generate_password(password_length):
    special_characters = string.punctuation
    password = ''.join(random.choices(string.ascii_letters + string.digits + special_characters, k=password_length))
    return password

while True:
    try:
        num_passwords = int(input("Kaç adet şifre oluşturmak istiyorsunuz: "))
        if num_passwords <= 0:
            print("Geçersiz sayı. Pozitif bir tamsayı girin.")
            continue
        length = int(input("Lütfen şifre uzunluğunu girin: "))
        if length <= 0:
            print("Geçersiz uzunluk. Pozitif bir tamsayı girin.")
            continue
        for _ in range(num_passwords):
            password = generate_password(length)
            print("Oluşturulan şifre: ", password)
        break
    except ValueError:
        print("Geçersiz giriş. Lütfen bir tamsayı girin.")
