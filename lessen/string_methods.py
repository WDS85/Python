var = "hello world"
var2 = ["Hello", "World"]
var3 = "            Hello world     "
#hoofdletters 
print(var.upper())
#kleine letters
print(var.lower())
#titel maken
print(var.title())
#splitsen
print(var.split())
#samenvoegen 
print(' '.join(var2))
#letter vervangen
print(var.replace('h', "j"))
#witruimte weglaten
print(var3.strip())
#string samenstellen
'{} {}'.format("Hello", "world")