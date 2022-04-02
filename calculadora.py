import turtle

print("Bienvenido a mi calculadora con python \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division \n 5.Division redondeada \n 6.Exponenciacion \n 7.MOD \n 8.Areas")

ind=int((input('Por favor elija una funcion para empezar digitanto el numeral de la operacion ')))
if ind>8:
    print("No tenemos ninguna funcion identificada con ese numeras\n Gracias por usar nuestro programa")
if ind == 1:
    print("**Usted a elejido la suma**")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese el numero con el que lo quiera sumar: ')))
    resultado= num1 + num2
    print(resultado)
if ind == 2:
    print("**Usted a elejido la resta**")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese el numero con el que lo quiera restar: ')))
    resultado= num1 - num2
    print(resultado)
if ind == 3:
    print("**Usted a elejido la multiplicacion**")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese el numero con el que lo quiera multiplicar: ')))
    resultado= num1 * num2
    print(resultado)
if ind == 4:
    print("**Usted a elejido la division**")
    print("¡¡Importante!! 'esta operacion solo dara resultados en numeros enteros'")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese el numero con el que lo quiera dividir: ')))
    resultado= int(num1 / num2)
    print(resultado)
if ind == 5:
    print("**Usted a elejido la operacion modular**")
    print("¡Asegurese de usar numeros cuyo resultado sea un numero decimal")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese el numero con el que lo quiera dividir: ')))
    resultado= num1 // num2
    print(resultado)
if ind == 6:
    print("**Usted a elejido la exponenciacion**")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese el numero con el que lo quiera exponeciar: ')))
    resultado= num1 ** num2
    print(resultado)
if ind == 7:
    print("**Usted a elejido la operacion modular**")
    num1=int((input('Ingrese un numero: ')))
    num2=int((input('Ingrese un segundo numero: ')))
    resultado= num1 % num2
    print(resultado)

option= ""
dibujar=""
if ind == 8:
    print("Eija el tipo de forma de la cual quiere saber su area")
    print("1.Cuadrado")
    print("2.Triangulo")
    print("3.Rectangulo")
    option=int((input('¿Cual es la forma de la cual quiere saber el area? ')))
if option == 1:
    print("**A elegido saber el area de un cuadrado**")
    numeroc=int((input('Ingrese la medida de un lado: ')))
    resultado= numeroc**2
    print(f'su resutado es:{resultado}')
    dibujar= str((input("¿Desea dibujar su figura? ")))
if option == 2:
    print("**A elegido saber el area de un triangulo**")
    baset=int((input('Ingrese la medida de la base: ')))
    alturat=int((input('Ingrese la medida de la altura: ')))
    resultado= baset*alturat/2
    print(f'su resutado es:{resultado}')
    dibujar= str((input("¿Desea dibujar su figura? ")))
if option == 3:
    print("**A elegido el area de un rectangulo")
    baser=int((input('Ingrese la medida de la base: ')))
    alturar=int((input('Ingrese la medida de la altura: ')))
    resultado= baser*alturar
    print(f'su resutado es:{resultado}')
    dibujar= str((input("¿Desea dibujar su figura? ")))
figura=""
if dibujar =="si":
    print("1.Cuadrado")
    print("2.Triangulo")
    print("3.Rectangulo")
    figura= int((input("¿Cual fue su figura anteriormente seleccionada?\n *Digitando el numeral* ")))
    turtle.hideturtle()
    turtle.title("Su forma geometrica dibujada")
if figura == 1:
    turtle.forward(numeroc)
    turtle.left(90)
    turtle.forward(numeroc)
    turtle.left(90)
    turtle.forward(numeroc)
    turtle.left(90)
    turtle.forward(numeroc)
    turtle.exitonclick()
if figura == 2:
    turtle.forward(baset)
    turtle.left(120)
    turtle.forward(baset)
    turtle.left(120)
    turtle.forward(baset)
    turtle.exitonclick()
if figura == 3:
    turtle.forward(baser)
    turtle.left(90)
    turtle.forward(alturar)
    turtle.left(90)
    turtle.forward(baser)
    turtle.left(90)
    turtle.forward(alturar)
    turtle.exitonclick()

final=""

final= str((input("¿Su resultado fue el correcto? ")))
if final == "si":
    print("Gacias por usar nuestra calculadora")
else:
    f= open("feedback.txt", "w")
    feedback = input("Cuentenos el problema y trataremos de solucionarlo ")
    f.write(feedback)
    f.close()
    print("Muchas gracias por su comentario")
