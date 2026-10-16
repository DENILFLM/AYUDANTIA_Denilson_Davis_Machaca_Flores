num1=int(input("Ingrese el primer numero:  "))
num2=int(input("Ingrese el segundo numero:  "))

print(f"""

La suma de {num1} + {num2} = {num1+num2}
La resta de {num1} - {num2} = {num1-num2}
La multiplicacion de {num1} x {num2} = {num1*num2}
""")
if num2 != 0:
    print(f"La division de {num1} / {num2} = {num1/num2}")
else:
    print("No se puede dividir entre 0")