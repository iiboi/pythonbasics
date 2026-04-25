bank_payload = "   TR123456789012345678901234 |  1250.50 |   BAŞARILI | islem_detayi: yillik_sunucu_masrafi   "

bank_payload = bank_payload.strip().split('|')

iban = bank_payload[0].strip()
has_iban_tr = iban.startswith('TR')


payment = float(bank_payload[1].strip())



index = bank_payload[2].strip().lower()
index_status = 'başarili' in index

transaction_details = bank_payload[3].replace('islem_detayi:', '').replace('_', ' ').strip().title()

receipt = 'ODEME OZETI'
receipt = receipt.center(25, '#')


print(receipt)
print(f'IBAN Ülkesi Türkiye: {has_iban_tr}')
print(f'IBAN Bilgisi: {iban}')
print(f'Ödeme Miktarı: {payment}')
print(f'Ödeme Başarılı mı?: {index_status}')
print(f'Ödeme Açıklaması: {transaction_details}')