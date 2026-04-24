current_balance = 5000

system_2FA_code = "password"

req_amount = int(input("Çekmek istediğiniz tutarı giriniz."))
user_2FA_code = input("Doğrulama kodunu giriniz.")

if user_2FA_code != system_2FA_code:
    print("Güvenlik ihlali: Hatalı doğrulama kodu!")
elif user_2FA_code == system_2FA_code and req_amount > current_balance:
    print("İşlem başarısız: Yetersiz bakiye.")
elif user_2FA_code == system_2FA_code and req_amount <= current_balance:
    print("İşlem Başarılı!")
    new_balance = current_balance - req_amount
    print(f"{req_amount} Başarıyla verildi \n Hesapta Kalan Miktar{new_balance}")