import re
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

#
# for i in contacts_list[1:]:
#     lfs = re.findall('[А-Я][а-я]+'," ".join(i))
#     print(lfs[0:3])

def fio():
    serch_fio = r'([А-Я][а-я]+)'
    zamena_fio = r' \1'
    for stolb in contacts_list[1:]:
        stroka = stolb[0] + stolb[1] + stolb[2]
        if len((re.sub(serch_fio, zamena_fio, stroka).split())) == 3:
            stolb[0] = re.sub(serch_fio, zamena_fio, stroka).split()[0]
            stolb[1] = re.sub(serch_fio, zamena_fio, stroka).split()[1]
            stolb[2] = re.sub(serch_fio, zamena_fio, stroka).split()[2]
        elif len((re.sub(serch_fio, zamena_fio, stroka).split())) == 2:
            stolb[0] = re.sub(serch_fio, zamena_fio, stroka).split()[0]
            stolb[1] = re.sub(serch_fio, zamena_fio, stroka).split()[1]
            stolb[2] = ''
    return

def phone_format():
    pass

if __name__ == '__main__':
    fio()
    print(contacts_list)


    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)