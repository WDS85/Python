import csv

studenten = [
    {'naam': 'Anna', 'cijfer': 7.5},
    {'naam': 'Boris', 'cijfer': 8.0},
    {'naam': 'Clara', 'cijfer': 6.5},  
    ]

with open('studenten.csv', 'w', newline='') as student_csv:
    fields = ['naam', 'cijfer']
    writer = csv.DictWriter(student_csv, fieldnames=fields)

    writer.writeheader()
    for item in studenten:
        writer.writerow(item)