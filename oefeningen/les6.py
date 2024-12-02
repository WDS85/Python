# .upper() --> Hello World -> HELLO WORLD
# .lower() --> Hello world -> hello world
# .title() --> Hello world -> Hello World
# .split() --> Hello world --> ['Hello', 'World'] (zal splitten op een waarde, default op spatie)
# .join()
# .replace()
# .strip()
# .format()

# def to_uppercase():
#     input_str = str(input('Geef een string in '))
#     up_str = input_str.upper()
#     print(up_str)

# to_uppercase()

# def to_uppercase(text):
#     return text.upper()

# input_str = "dit is een voorbeeld"
# output_Str = to_uppercase(input_str)

# print(input_str)

# def countdown():
#     t_minus = int(input('Geef de waarde in '))

#     while t_minus >= 1:
#         print(t_minus)
#         t_minus = t_minus - 1
#         if t_minus == 0:
#             print('Lancering!')

# countdown()

# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#     print('Lancering')

# countdown(5)

# def print_even_numbers(n):
#     while n > 0:
#         if n % 2 == 0:
#             print(n)
#         n -= 1
      
# print_even_numbers(151)

# def print_even_numbers(n):
#     number = 2
#     while number <= n:
#         print(number)
#         number += 2

# print_even_numbers(20)

#niet correct, zie slides
# def fizzbuzz():
#     for i in range(1, 51):
#         print(i)
#         if i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         elif i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
    
   
# fizzbuzz()

def calculator():
    x = float(input("Geef getal 1 in "))
    y = float(input("Geef getal 2 in "))
    n = input("Geef een operatie in ")
    if n == '+':
        result = x + y
    elif n == '-':
        result = x - y
    elif n == '*':
        result = x * y
    elif n == '/':
        result = x / y
    else:
        print('Ongeldige operatie')
        return
    print(f"{x} {n} {y} = {result}")

    

calculator()

