fio = input('ФИО:').strip()
a = fio.split()
ini = ''.join(i[0] for i in a)
fioo = ' '.join(i for i in a)
print('ФИО:', fioo, 'Инициалы:', ini, 'Длина:', len(fioo)) 

