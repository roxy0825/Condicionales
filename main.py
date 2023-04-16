#1.EJERCICIO: Hacer un algoritmo que lea el nombre de una persona y la edad. Si la edad es mayor
#o igual a 18 años, imprimar “Puede ingresar” de lo contrario “Eres menor de edad,
#no puedes ingresar”


("""nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("¡Puede ingresar!")
else:
    print("Eres menor de edad, no puedes ingresar.")
print('-'*30)""")


#2.EJERCICIO: Hacer un algoritmo que lea el nombre de un animal, la comida preferida, el precio
#de la comida y cuantas veces come de ese alimento en la semana. Si El valor del
#alimento en la semana es menor o igual de 50 mil pesos. Imprima, “Eres un animal
#económico” de lo contrario “Tus gastos Animales son muy altos”

(""" nombre_animal = input("Ingrese el nombre del animal: ")
comida_preferida = input("Ingrese la comida preferida del animal: ")
precio_comida = float(input("Ingrese el precio de la comida preferida: "))
veces_semana = int(input("Ingrese cuantas veces come el animal a la semana: "))

gasto_semanal = precio_comida * veces_semana

if gasto_semanal <= 50000:
    print("Eres un animal económico")
else:
    print("Tus gastos animales son muy altos")
print('-'*30)""")

#3. EJERCICIO: Leer dos números DIFERENTES e imprimir cuál es el mayor.

("""nro1=int(input("Ingrese el primer numero: "))
nro2=int(input("Ingrese el segundo numero: "))

if nro1 > nro2:
     print("El numero mayor es el primero:  " + str (nro1))
else:
    print("El numero mayor es el segundo: " + str (nro2))
print('-'*30)""")

#4.EJERCICIO:Se debe crear un algoritmo que imprima el nombre del estudiante, el valor de la
#matrícula y su estrato. Si el estrato es menor de 4 se le realizará un descuento del
#40% de lo contrario el descuento será del 5%. Imprima nombre, valor de la
#matricular, estrato, el valor del descuento y el total a pagar

("""nom_estudiante = input("Ingrese el nombre del estudiante: ")
valor_matricula=float(input("Ingrese valor de matricula: "))
estado= int(input("Ingrese estrato del estudiante: "))


if estado < 4:
    descuento= valor_matricula * 0.4
else:
    descuento= valor_matricula * 0.05

total = valor_matricula - descuento

print('-'*30)

print("Nombre del estudiante: " + nom_estudiante)
print("El valor de la matricula es de : " + str (valor_matricula))
print("El estrato del estudiante es: " + str(estado))
print("El valor del descuento es de:  " + str(descuento))
print("Valor total a pagar de matricula es de : " +str(total))
print('-'*30)""")

#5.EJERCICIO: El administrador de un parqueadero de motos, cobra a 2.800 la hora de parqueo.
#Cuando ingresa un usuario se debe saber la placa y el numero de horas que estará la
#moto en el parqueadero. Si la cantidad de horas es mayor 5 se le cobrará 10.000 de
#lo contrario se le cobra el valor de las horas. Se debe imprimir la placa, el numero de
#horas y el valor a pagar.

nom_cliente = input("Ingrese nombre del usuario: ")
placa = input("Ingrese la placa de la moto: ")
horas = int(input("Ingrese el número de horas que estará la moto en el parqueadero: "))


if horas < 5:
    valor_pagar = 10000
else:
    valor_pagar = horas * 2800
print('-'*30)
print("Nombre cliente: ", nom_cliente)
print("Placa: ", placa)
print("Horas: ", horas)
print("Valor a pagar: ", valor_pagar)


print('-'*30)