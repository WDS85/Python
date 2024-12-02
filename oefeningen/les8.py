#bestand in dir openen, uitlezen

# with open('real_cool_document.txt') as cool_doc:
#     cool_contents = cool_doc.read()
#     print(cool_contents)

#lijn uitlezen uit bestand

# with open('keats_sonnet.txt') as keats_sonnet:
#     for line in keats_sonnet.readlines():
#         print(line)

#lijn per lijn uitlezen

# with open('millay_sonnet.txt') as sonnet_doc:
#     first_line = sonnet_doc.readline()
#     second_line = sonnet_doc.readline()
#     print(second_line)

#bestand maken, line schrijven

# with open('generated_file.txt', 'w') as gen_file:
#     gen_file.write("What an incredible file!")


# with open('generated_file.txt') as gen_file:
#     for line in gen_file.readlines():
#         print(line)

#lijn toevoegen aan bestand, append

# with open('generated_file.txt', 'a') as gen_file:
#     gen_file.write("\n...and it still is")

#csv bestand lezen met komma

# import csv

# list_of_email_addresses = []
# with open('users.csv', newline='') as users_csv:
#     user_reader = csv.DictReader(users_csv)
#     for row in user_reader:
#         list_of_email_addresses.append(row['Email'])

# print(list_of_email_addresses)

#csv bestand lezen met puntkomma

# with open('users2.csv', newline='') as users_csv:
#     user_reader = csv.DictReader(users_csv, delimiter=';')
#     for row in user_reader:
#         print(row['Email'])

#schrijven naar csv file

# big_list = [
#     {'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, 
#     {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, 
#     {'name': 'Greely Plank', 'userid': 15890235, 'is_admin': False},
#     {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}
#     ]

# import csv

# with open('output.csv', 'w') as output_csv:
#     fields = ['name', 'userid', 'is_admin']
#     output_writer = csv.DictWriter(output_csv, fieldnames=fields)

#     output_writer.writeheader()
#     for item in big_list:
#         output_writer.writerow(item)

#json file lezen

import json

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json)

    print(purchase_data['user'])