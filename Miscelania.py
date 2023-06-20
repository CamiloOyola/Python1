import math

menu=int(input(" Menu principal: \n 1-Operadores \n 2-Condicionales \n 3-Ciclos \n 99-Salir \n "))
if (menu==1):
 print("Eliga una operacion")
     
 opcion=int(input(
    "1.Area de un triangulo\n"
    "2.Suma\n" 
    "3.Numero a la potencia cuadrada\n"
    "4.Conversion de euros a dolares\n"
    "5.Valor del area y perimetro de un cuadrado\n"
    "6.Area y volumen de un cilindro\n" 
    "7.Longitud y Area de una circunferencia\n" 
    "8.Promedio de tres numeros\n"))
 match opcion:
  case 1:
   base=int(input("ingrese la base del triangulo[cm]:"))
   altura=int(input(" ingrese la altura del triangulo[cm]: "))
   resultado= int((base*altura)/2)
   print(" la base del triangulo es: ", resultado)
  case 2: 
   numero1=int(input(" escriba el primer numero: "))
   numero2=int(input(" escriba el segundo numero: "))
   resultado=numero1+numero2
   print(" el resultado de la suma es: ",resultado)
  case 4: 
   tipo_cam=float(0.91)
   dolar=float(input(" ingrese la cantidad de dolares: "))
   conversion= tipo_cam*dolar
   print(" el resultado de su conversion es: ",conversion,"euros")
  case 3 :
   numero1= int( input(" Escriba un numero "))
   print(" El cuadraro de", numero1, "es :", numero1**2 )
  case 5: 
   numero1= int( input(" Escriba el valor de un lado del cuadrado[cm]: "))
   print(" El area del cuadrado es :",numero1**2)
   print(" El perimetreo del cuadradoes :", numero1**4)
  case 6:
   radio= float(input(" Ingrese el radio del cilindro: ")) ; altura=float(input(" Ingrese la altura del cilindro: "))
   print(" El volumen del cilindro es:",(math.pi)*(radio**2)*altura)
   print(" El area del cilindro es:", 2*(math.pi)*radio*(altura+radio))
  case 8:
   numero1=int(input(" Ingrese el primer numero:")); numero2=int(input(" Ingrese el segundo numero:")); numero3=int(input(" Ingrese el tercer numero:"))
   print(" El promedio de los tres numeros es:", numero1+numero2+numero3/3)
  case 7:
   radio=float(input(" Ingrese el radio de la circunferencia:"))
   print(" La longitud de la circunferencia es:", 2*(math.pi)*radio)
   print(" El area de la circunferencia es", ((math.pi)*radio)**2)
elif (menu==2):
 print(" Eliga una opcion ")
 opcion=int(input(" 1. Numero positivo o negativo \n 2. Numero ingresado es mayor o menor \n 3. Cual numero es mayor o menor entre dos numeros \n 4. Dados dos numeros se pueden restar o sumar \n 5. Encontrar el cociente entre dos numeros\n 6. Suma o multiplicacion\n 7. Es un año bisisesto o no \n "))
 match opcion: 
  case 1: 
   numero1=float(input(" Ingrese un numero : "))
   if(numero1>0):
    print(" El numero es positivo ")
   elif(numero1<0):
    print(" El numero es negativo")
  case 2: 
    numero1=int(input(" Ingrese el primer numero ")) ; numero2=int(input(" Ingrese el segundo numero "))
    if(numero1>numero2):
     print(" El primer numero es mayor que el segundo ")
    elif(numero1<numero2):
     print(" El segundo numero es mayor que el primero ")
    else:
     print(" Los numeros son iguales ")
  case 3:
   x = input(' Ingrese el primer numero:')
   z = input(' Ingrese el segundo numero:')
   y = input(' Ingrese el tercer numero')
   a = min(x,z,y)
   b = max(x,z,y)
   print("el numero mayor es: {} y el numero menor es {}".format(b,a))
  case 4:
   a = input(" Ingrese la primer variable: ")
   b = input(" Ingrese la segunda variable: ")
   if a < b:
    suma = int(a) + int(b)
    print(" El resultado de la suma: ", suma)
   elif a > b:
    resta =int(a) - int(b)
    print(" EL resultado de la resta es: ", resta) 
  case 5: 
    a = float(input(" Ingrese el primer numero: "))
    b = float(input(" Ingrese el segundo numero: "))
    if a > 0 and b > 0:
     division = int(a) / int(b)
     print(" El resultado de la division es: ", division)
    else:
     print("No es posible realizar la division por cero")
  case 6:
   numero1=int(input(" Ingrese el primer numero: "))
   numero2=int(input(" Ingrese el segundo numero: "))
   if(numero1<0 or numero2<0):
    print(" El resultado de la suma es:", numero1*numero2)
   elif(numero1 or numero2>0):
    print(" El resultado de la suma es:", numero1+numero2)
  case 7:
   dia=int(input(" Ingrese los dias que tiene febrero en su calendario actual: "))
   if(dia==29):
    print(" Su año es bisiesto ")
   elif(dia<=28):
    print(" Su año no es bisiesto")
            
elif(menu==3):
  print(" Eliga una opcion ")
  opcion=int(input(" 1. Numeros multiplos de 3 que hay entre 1 y 100 \n 2. Numeros impares entre 1 y 100 \n 3. Numeros pares del 1 al 100 \n 4. Cuadrados de los numeros del 1 al 30 \n 5. Suma de los cuadrados de los cien primeros numeros naturales \n 6. Numeros comprendidos entre dos numeros en secuencia ascendente \n 7. Suma de todos los numeros(excepto el cero) \n "))
  match opcion:
   case 3:
    for i in range(2,101,2):
     print(i) 
   case 2: 
    for i in range(2,100,2):
     print(i-1)
   case 1: 
    for i in range(3,100,3):
     print(i)
   case 4: 
    for i in range(1,31):
     print(i**2)
   case 5:
    for i in range(1,100):
     print(i+i**2)
   case 6:
     a=int(input(" Ingrese un numero menor al segundo numero: "));c=int(input(" Ingrese un numero mayor al primero: "))
     b= a+1
     for i in range(b,c):
      print(i)
   case 7:
     a=int(input(" Ingrese un numero: "));b=int(input(" Ingrese el segundo numero: "))
     while (a!=0):
      print(a+b)
      break
elif(menu==99):
    print(" Hata luego ")