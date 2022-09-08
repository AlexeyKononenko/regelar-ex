from ast import pattern
import itertools
from pprint import pprint
import csv
import re
with open('phonebook_raw.csv', 'r', encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

pattern_phone = r'(\+7|8)\s*\(?(\d{3})\)?(\s*|-)(\d{3})(\s*|-*)(\d{2})-?(\d{2})(\s*(\(?(\доб.)?)\s*(\d{4}))?(\))*'
pattern_phone_new = r'+7(\2)\4-\6-\7 \10\11'


name_list = []
for elem in contacts_list:
    name = ' '.join(elem[:3]).split(' ')
    res = [name[0], name[1], name[2], elem[3], elem[4], re.sub(pattern_phone, pattern_phone_new, elem[5]), elem[6]]
    name_list.append(res)



for i in name_list:
        first_name = i[0]
        last_name = i[1]
        for j in name_list:
            new_first_name = j[0]
            new_last_name = j[1]
            if first_name == new_first_name and last_name == new_last_name:
                if i[2] == "": i[2] = j[2]
                if i[3] == "": i[3] = j[3]
                if i[4] == "": i[4] = j[4]
                if i[5] == "": i[5] = j[5]
                if i[6] == "": i[6] = j[6]

result_list = list()
for i in name_list:
  if i not in result_list:
    result_list.append(i)


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)