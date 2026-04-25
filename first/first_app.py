def tax_calculate():
    tax_rate = 0.20

    product_price = int(input("Urun Fiyatı giriniz:"))

    total_tax = product_price * tax_rate
    taxfree_price = product_price - total_tax

    print("Urunun vergisiz fiyatı:", taxfree_price)
    print(total_tax, " TL Vergi İadenizi alabilirsiniz.")

tax_calculate()
