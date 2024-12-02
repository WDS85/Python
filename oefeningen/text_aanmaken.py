with open('mijn_notities.txt', 'w') as gen_file:
    gen_file.write("Wow, geweldig\n")
    gen_file.write("Formidabel\n")
    gen_file.write("Fantastisch\n")

with open('mijn_notities.txt', 'a') as gen_file:
    gen_file.write("Er komt nog een zin bij\n")

# with open('mijn_notities.txt') as gen_file:
#     for line in gen_file:
#         print(line)

with open('mijn_notities.txt', 'r') as gen_file:
    inhoud = gen_file.read()
    print("inhoud van het bestand:")
    print(inhoud)

