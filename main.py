"""""
nombre = "Irving Cober"
edad = 22
student = True

print("hello")
print(f"My name is {nombre}")
print(f"My age is {edad}")

if student:
    print("\nSoy estudiante de sistemas")
else:
    print("\nNo soy estudiante de sistemas")

#Tipos

nombre = "Irving"
apellido = ""
edad = 22
estatura = 1.68

print(type(apellido))

edad = float(edad)

print(f"Edad en decimal: {edad}")
print(f"String Boleano: {bool(apellido)}")

estatura = str(estatura)
print(f"Estatura en str: {estatura+"1"}")

#Imput
name = input("¿Como te llamas?: ")
age = int(input("¿Cuantos Años tienes?: "))

age = age + 1

print(f"\nHello {name}")
print("Happy Birthday!!!")
print(f"Your age is {age} years old")


LadoA = float(input("Ingresa la Medida del lado mas largo del rectangulo: "))
LadoB = float(input("Ingresa la medida del lado mas corto del rectangulo: "))

area = LadoA * LadoB

print(f"El area del rectangulo es {area}")

from Practicas.words import words
"""""


"""""
import random
import time
"""""
"""""
Funciones matematicas    
round() Redondear    
abs() Absoluto de un número   
pow(a,b) Potencias    
max(a,b,c,...z) El máximo de grupo de números    
min(a,b,c,...z) El entero de grupo de números        
Imports    
math        
Funciones    
math.pi PI   
math.e E (natural)    
math.sqrt Raiz    
math.ceil Redondear hacia arriba 9.1 = 10    
math.floor Redondear hacia abajo 9.999 = 9
"""""

"""""
#exercise 2 Area and circunference
import math

radius = float(input("Enter the radius of a circle: "))
circunference = 2 * math.pi * radius
area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {round(area,2)}cm")

#exercise 3 Hipotenusa

a = float(input("Enter the side a:"))
b = float(input("Enter the side b:"))

c = math.sqrt((pow(a,2)) + (pow(b,2)))

print(f"The hipotenusa is: {c}")

"""""
"""""
#calculadora 
operator = input("enter an operator (+ - / *): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"The sum is: {round(result,3)}")
elif operator == "-":
    result = num1 - num2
    print(f"The difference is: {round(result,3)}")
elif operator == "*":
    result = num1 * num2
    print(f"The product is: {round(result,3)}")
elif operator == "/":
    result = num1 / num2
    print(f"The division is: {round(result,3)}")
else:
    print(f"{operator} is not a valid operator")
"""""
"""""
#exercise 5

weight = float(input("Enter your weight: "))
unit = input("Enter your unit KG or Lb: ")
if unit == "KG":
    weight = weight * 2.205
    unit = "Lb"
    print(f"Your weight is {round(weight,1)}{unit}")

elif unit == "Lb":
    weight = weight / 2.205
    unit = "KG"
    print(f"Your weight is {round(weight,1)}{unit}")
else:
    print(f"{unit} was not valid")
"""""

"""""
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temperature = float(input("Enter the temperature: "))

if unit == "C":
    temperature = round((9 * temperature) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is: {temperature}°F")
elif unit == "F":
    temperature = round((temperature - 32) * 5 / 9, 1)
    print(f"The temperature in Celsius is: {temperature}°C")
else:
    print(f"{unit} is an invalid unit of measurement")
"""""

"""""
#Operacion Ternaria
edad = 15
print("Mayor de edad" if edad > 18 else "Menor de edad")
result = "Par" if edad % 2 == 0 else "Impar"

print(result)
"""""

"""""
Cadenas

len(name)  Cuenta el número de caracteres de la cadena
name.find("letra")  Busca el índice de la primera coincidencia de la letra o subcadena dentro de la cadena. Devuelve -1 si no se encuentra
name.rfind("letra")  Busca el índice de la última coincidencia de la letra o subcadena dentro de la cadena. Devuelve -1 si no se encuentra
name.capitalize()  # Convierte en mayúscula la primera letra de la cadena
name.upper()  # Convierte en mayúsculas toda la cadena
name.lower()  # Convierte en minúsculas toda la cadena
name.isdigit()  # Detecta si la cadena contiene solo dígitos
name.isalpha()  # Detecta si la cadena contiene solo letras
result = phone_number.count("-")  # Cuenta las ocurrencias de la subcadena "-" dentro de la cadena
result = phone_number.replace("-", "")  # Reemplaza todas las ocurrencias de "-" por una cadena vacía



name = input("Enter your name: ")
print(name.count("a"))

"""""
"""""
#Exercise 8
#Validate User inputexercise
# 1. Username is no more than 12 characters
# 2. Username must not contain spaces
# 3. Username must no contain digits
username = input ("Enter your Username: ")

if len(username) > 12:
    print("Username too long, it can´t be more than 12 characters")
elif not username.find(" ") == -1:
    print("Username can't contains spaces")
elif not username.isalpha():
    print("Username can't contain numbers")
else:
    print(f"Welcome {username}")
"""""

"""""
#Video 16
num = int(input("Enter a number between 1 and 10 : "))

while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter a number between 1 and 10 : "))
    
print(f"Your number is {num}")
"""""

"""""
#Video 17
p = 0
r = 0
t = 0


while p <= 0:
    p = float(input("\nDigite su balance: "))
    print(p)
    if p <= 0:
        print("Principle can't be less thanor equal to zero")

while true:
    r = float(input("\nDigite su porcentaje de interes: "))
    if r <= 0:
        print("Interest rate can't be less thanor equal to zero")
    else:
        break

while t <= 0:
    t = float(input("\nDigite el tiempo en años: "))
    if t <= 0:
        print("Time can't be less thanor equal to zero")

total = p * pow((1 + r / 100), t)
print(f"Balance despues {t} años/s: ${t:.2f}")
"""""


"""""
#Ciclo For

credit_card = "1234-5678-9012-3456"

#Iteración normal:
print("\nIteración Normal: ")
for i in range(1,11):
    print(i)

print("\nIteración Modificado: ")

#Iteración Modificada:
for i in range(1,11,2):
    print(i)

print("\nIteracion Invertida: ")
for i in reversed(range(1,11)):
    print(i)

print("\nIteracion contenido en cadena: ")
for i in credit_card:
    print(i)
"""""
"""""
import time
my_time = int(input("enter the time in seconds: "))
for i in range(my_time,0,-1):
    segundos = i % 60
    minutos = int (i / 60) % 60
    hours = int(i /3600)

    print(f"{hours:02}:{minutos:02}:{segundos:02}")
    time.sleep(1)

print("El tiempo se detuvo")
"""""
"""""
#Bucles anidados

filas = int(input("Digite el numero de filas: "))
columnas = int(input("Digite el numero de columnas: "))
simbolo = input("Digite el simbolo a imprimir: ")

for i  in range(filas):
    for j in range(columnas):
        if j != columnas-1:
            print(simbolo, end=" calabacita ")
        else:
            print(simbolo, end=" ")
    print()
"""""
"""
# Colecciones =variable unica usada para establecer multiples variables
#   Listas = [] ordenadas y configurables. Puedes duplicar el contenido
#   Set = {} Desordenadas e inconfigurables, pero puedes añadir/eliminar (add/remove). No acepta valores duplicados
#   Tuple = Ordenadas e inconfigurables. Puedes duplicar contenido. Son más rápidas

fruits1 = ["apple", "orange", "banana", "coconut"]
fruits2 = {"apple", "orange", "banana", "coconut"}
fruits3 = ("apple", "orange", "banana", "coconut")

#Funciones globales
print(dir(fruits1)) #Te dice que funciones puedes realizar con esa colección
print(help(fruits2)) #Te describe a detalle las funciones que puedes utilizar en esa collección
print(len(fruits3)) #Te dice cuantos objetos tiene la colleción
print("pineapple" in fruits1) #Te dice si se encontro una coincidencia

#Funciones para tuple
print("Funciones para tuplas: \n")

print(fruits3.count("coconut"))


print("Lista: \n")
print(fruits3)

for fruit in fruits1:
    print(fruit)

#Funciones para set
print("Funciones para sets: \n")

print(fruits2.add("pineapple")) #Función para añadir elementos
print(fruits2.remove("apple")) #Remueve un elemento en especifico
fruits2.pop() #Elimina un elemento de la lista (no se sea aleatorio o es el último elemento)
fruits2.clear() #Elimina el contenido de la lista

print("Set: \n")
print(fruits2)

for fruit in fruits1:
    print(fruit)

#Funciones para list
fruits1[0] = "pineapple" #Igualar un elemento en una posición en especifico
fruits1.append("pineapple") # Agregar elementos en lista
fruits1.remove("orange") #Remueve el elemento dicho
fruits1.insert(0, "grade") #Inserta el elemento en la posición dicha 
fruits1.sort()
fruits1.reverse() #Invierte la lista
print(fruits1.index("grade")) #Te dice en que posición de la lista se encuentra el elemento
print(fruits1.count("orange")) #Realiza un conteo de las coincidencias

print("List: \n")
print(fruits1)

for fruit in fruits1:
    print(fruit)

fruits1.clear() #Elimina el contenido de la lista
"""
"""
#Shopping Kart Program
foods = []
prices = []
total = 0
cont = 0

while True:
    food = input("Ingrese el alimento a comprar (q to quit): ")

    if food.lower() == "q":
        break
    else:
        cont += 1
        price = float(input(f"Ingrese el valor de {food}: $"))

        foods.append(food)
        prices.append(price)


print("---------Tu carta es----------")
print()
for i in range(0, cont):
    print(f"{foods[i]}:  ${prices[i]}")
    total += prices[i]

print(f"Tu total es: ${total}")
"""
"""
# Listas de Listas (matrices)

fruits = ["Apple", "Orange", "Banana", "Coconut"]
vegetables = ["Celery", "Carrots", "Potatoes"]
meats = ["Chicken", "Fish", "Turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for element in collection:
        print(element)
    print()


#Tupla de Tuplas

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
"""
"""
#Python Quizz Game
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in earth's atmosphere?: ",
             "How many bones are in the human boddy: ",
             "Which Planet in the solar system is the hottest: ")


options = (("A.116 ", "B.117  ", "C.118  ", "D.119  "),
           ("A. Whale ", "B. Crocodile  ", "C. Elephant  ", "D. Ostrich "),
           ("A. Nitrogen ", "B. Oxygen  ", "C. Carbon - Dioxide ", "D. Hydrogen "),
           ("A. 206", "B. 207  ", "C. 208 ", "D. 209 "),
           ("A. Mercury", "B. Venus  ", "C. Earth  ", "D. Mars  "))

answers = ("C", "D", "A", "A", "B")
guesses =[]
score = 0
question_num = 0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Ingrese una opcion (A, B, C, D) : ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        print(f"La respuesta es: {answers[question_num]}")

    question_num += 1

print("-------------------------")
print("--------RESULTADOS-------")
print("-------------------------")

print("Respuestas: ", end = " ")
for answer in answers:
    print(answer, end = " ")
print()

print("Adivinadas:  ", end = " ")
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(answers) * 100)
print(f"Your score is {score}%")
"""
"""
# dictionary = una colección de pares {clave:valor} ({Key:Value}) ordenados y modificables. sin duplicados

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}
# print(dir(capitals)) Te da las funciones que hay para los diccionarios
# print(help(capitals)) despliega el menu de ayuda y describe la funcion
# print(capitals.get("Japan")) a partir de una llave busca el valor correspondiente a esa llave

#if capitals.get("Russia"):
#    print("That Capital Exist")
#else:
#    print("That Capital does not exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detorit"}) Actualiza las llaves
#capitals.pop("China") borra la llave especificada
# capitals.popitem()
# capitals.clear()

keys = capitals.keys()
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)
"""
"""
menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Popcorn": 6.00,
        "Fries": 2.50,
        "Chips": 1.00,
        "Pretzels": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25,}

cart = []
total = 0

print("------Menú------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("-----------------")

while True:
    food = input("Ingrese el alimento a comprar (q para salir): ").lower()
    if food == "q":
        break
    elif menu.get(food.capitalize()) is not None:  #Usar el Capitalize para que detecte las opciones con mayusculas y capitalizar las opciones
        cart.append(food.capitalize())

print("----------Tu Orden:-------------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")

print()
print( f"El total es: ${total:.2f}")
"""
"""
import random

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","As"]

# number = random.radiant(low,high)
# number = random.random()
option = random.choice(options)
#random.shuffle(cards)

print(option)
"""
"""
#Adivina Numeros

import random
num_Menor = 1
num_Mayor = 100
respuesta = random.randint(num_Menor, num_Mayor)
guesses = 0
is_running = True

while is_running:

    guess = input("Ingrese su intento: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < num_Menor and guess > num_Mayor:
            print("Este numero esta fuera del rango")
            print(f"Por favor ingrese un numero entre {num_Menor} y {num_Mayor}")
        elif guess < respuesta:
            print ("¡Muy bajo! Intenta nuevamente con un numero mas alto")
        elif guess > respuesta:
            print("!Muy Alto¡ Intenta nuevamente con un numero mas bajo ")
        else:
            print(f"Correcto! La respuesta es: {respuesta}")
            print(f"Numero de intentos: {guesses}")
            is_running = False

    else:
        print("Intento invalido")
        print(f"Por favor ingrese un numero entre {num_Menor} y {num_Mayor}: ")
"""
"""
import random

opciones = ("piedra", "papel", "tijeras")
running = True

while running:
    player = None
    computer = random.choice(opciones)

    while player not in opciones:
        player = input("Ingrese su opcion: (piedra, papel o tijeras): ").lower()

        print(f"Jugador: {player}")
        print(f"Computador: {computer}")

        print()

        if player == "piedra" and computer == "papel":
            print("Computador gana")
        elif player == "papel" and computer == "tijeras":
            print("computador gana")
        elif player == "tijeras" and computer == "piedra":
            print("Computador gana")
        elif player == computer:
            print("Empate")
        else:
            print(f"Jugador gana")

        play_again = input("Desea jugar nuevamente (s/n): ").lower()
        if not play_again == "s":
            running = False

print("Saliendo...")
"""
"""
import random
# ● ┌ ─ ┐ │ └ ┘
"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art= {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘")
}
dice = []
total = 0
num_of_dice = int(input("Ingrese el numero de dados: "))

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end = " ")
    print()

for die in dice:
    total += die
print(f"Total: {total}")
"""
"""
#funciones

def hello(greeting, title, firts, last):
    print(f"{greeting} {title}{firts} {last}")

hello("Hello", "Mr.", "John", "James")
hello("Hello", "Mr.", last="John", firts="James")

#Parametros como listas o arreglos
def fruits(*args):
    for fruit in args:
        print(fruit, end=" ")

fruits("Orange", "apple", "banana")

#Parametros como diccionarios
print("\n")
def direccion(**kwargs):
    for values in kwargs.values():
        print(values)

    print()

    for key in kwargs.keys():
        print(key)

    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")


direccion(nombre="Selena",
          apartamento="512",
          coche="suru")
"""


"""
# Listas de comprension: una manera consisa de crear una lista compacta  y facil  de leer que los bucles tradicionales en python (Expresiones de valores iterables en condicionales IF)

grades = [85, 42, 79, 90, 56, 61, 30]
pasing_grades = [grade for grade in grades if grade >= 60]

print(pasing_grades)
"""


"""
#Keyword Arguments: Argumentos precedidos por un identificador  ayuda con la redactabilidad y el orden de los argumentos no importa,
#                   1.Posicional 2.Default 3.Keyword 4. Arbitrario

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello","Mr.", "SpongeBob", "Squarepants")
hello( "Hello", title= "Mr.", last="SpongeBob", first="Squarepants")
"""
"""
#Match Case / Switch
def is_weekend(day):
    day= day.capitalize()

    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday "| "Friday":
            return False
print(is_weekend("sunday"))
"""

"""
#Modulos
import math #importación normal
from math import pi #importar algo especifico
import math as m #cambiar el nombre a mi librería
"""

"""
#Python Banking program
import time
def show_balance(balance):
    print("-----------------------")
    print(f"Tu saldo es: $ {balance}")
    print("-----------------------")
def deposit():
    print("-----------------------")
    amount = float(input("Ingrese la cantidad a depositar: $"))
    print("-----------------------")
    if amount < 0:
        print("Ese no es un monto válido")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Ingrese el monto del retiro:$ "))

    if amount > balance:
        print("Fondos Insuficientes")
        return
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("-----------------------")
        print("    Banking Program    ")
        print("-----------------------")
        print("1.Mostrar saldo")
        print("2.Hacer Deposito")
        print("3.Generar retiro")
        print("4.Salir")
        print("-----------------------")

        choice = int(input("Elige la opcion deseada (1-4): "))

        match choice:
            case 1:
                show_balance(balance)
            case 2:
                balance += deposit()
            case 3:
                balance -= withdraw(balance)
            case 4:
                is_running = False
            case _:
                print("-----------------------")
                print("Esta Opción no es válida")
                print("-----------------------")

        print("-----------------------")
        print("Gracias, Ten un  excelente dia")
        print("-----------------------")

        time.sleep(1)

if __name__ == '__main__':
    main()
"""

"""
#Python CASINO

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔' , '⭐']
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("********************************")
    print("  |  ".join(row))
    print("********************************")

def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = int(input("Ingrese el monto para sus apuestas: $ "))
    cont = 0

    print("********************************")
    print("Bienvenido a Lion´s House Casino")
    print("Simbolos: 🍒 🍉 🍋 🔔 ⭐")
    print("********************************")

    while balance > 0:
        cont += 1
        print(f"Ronda {cont}")
        print(f"Saldo de Cuenta: ${balance}")

        bet = input("Ingresa el monto que deseas apostar: $")

        if not bet.isdigit():
            print("Favor de ingresar un numero valido")
            continue

        bet = int(bet)

        if bet > balance:
            print("Saldo insuficiente")
            continue

        if bet <= 0:
            print("La apuesta no puede ser igual o menor a 0")
            continue

        balance -= bet

        row= spin_row()
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Has ganado $ {payout}")
        else:
            print("Lo sentimos, perdiste la ronda")

        balance += payout

if __name__ == '__main__':
    main()
"""

"""
import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"Caracteres: {chars}")
print(f"Llave: {key}")

#ENCRYPT

plain_text = input("Ingresa el mensaje a encriptar: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Mensaje Original: {plain_text}")
print(f"Mensaje Encriptado: {cipher_text}")
"""

"""
#Ahorcado en Python

import random
import words
word = words.wordsitas

hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" ° ",
                   "   ",
                   "   "),
               2: (" ° ",
                   " | ",
                   "   "),
               3: (" ° ",
                   "/| ",
                   "   "),
               4: (" ° ",
                   "/|\\",
                   "   "),
               5: (" ° ",
                   "/|\\",
                   "/  "),
               6: (" ° ",
                   "/|\\",
                   "/ \\")}


def display_man(wrong_guesses):
    print("***************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(answer)


def main():
    answer = random.choice(word)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Ingrese una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Entrada invalida")
            continue

        if guess in guessed_letters:
            print("La letra ya fue utilizada")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if (answer[i]) == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!")
            is_running = False


if __name__ == "__main__":
    main()
"""

