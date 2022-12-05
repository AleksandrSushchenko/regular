import re
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # new_list = []
# print(contacts_list[1])

for i in contacts_list:
    lfs = re.findall('[А-Я][а-я]+'," ".join(i))
    print(lfs[0:3])



