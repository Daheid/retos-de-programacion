numero = 1
for j in range(100):
    numero = j + 1
    multiplo_3 = numero % 3
    multiplo_5 = numero % 5
    if multiplo_3 == 0 and multiplo_5 !=0:
        print("Fizz")
    elif multiplo_5 == 0 and multiplo_3 != 0:
        print("Buzz")
    elif multiplo_3 == 0 and multiplo_5 == 0:
        print("FizzBuzz")
    else:
        print(numero)