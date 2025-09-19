base = int(input('Price: '))
vat_amount = int(input('Discount: '))
total = int(input('vat: '))
print('База после скидки:', base * (1 - vat_amount/100), 'НДС:', \
      base * (1 - vat_amount/100) * (total/100), 'Итого к оплате:', base * (1 - vat_amount/100) + base * (1 - vat_amount/100) * (total/100))