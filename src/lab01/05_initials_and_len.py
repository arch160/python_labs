an = input('Фамилия:')
sn = input('Имя:')
bn = input('Отчество:')
print('ФИО:', an, sn, bn, 'Инициалы:', f'{an[0]}{sn[0]}{bn[0]} Длина:', len(an)+len(bn)+len(sn) )
