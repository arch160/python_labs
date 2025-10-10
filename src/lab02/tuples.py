def format_record(rec: tuple[str, str, float]) -> str:
    try:
        fio, gr, gpa = rec
        fio2 = ' '.join(fio.split()).split()
        fam = fio2[0]

        ini = []
        for i in range(1, len(fio2)):
            if i <= 2:
                ini.append(f"{fio2[i][0]}.")
        res = f"{fam} {''.join(ini)}, гр. {gr}, GPA {gpa:.2f}"
        return res
    except:
       return 'ValueError'
t = ("Иванов Иван Иванович", "BIVT-25", 4.6)
a = ("Петров Пётр", "IKBO-12", 5.0)
b = ("Петров Пётр Петрович", "IKBO-12", 5.0)
c = ("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
d = (" ", "ABB-01", 3.999)
print(format_record(t))
print(format_record(a))
print(format_record(b))
print(format_record(c))
print(format_record(d))
