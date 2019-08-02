# ==================================================
# FILE CONTAINING THE LIST OF PROBLEMS NR 1 TO NR 32
# ==================================================

# Imported module
import utilities

# Problème no 1 :
# ---------------
# Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x
def problem_1():
  print("\nVous avez sélectionné le problème suivant :")
  print("-----------------------------------")
  print("Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x")
  print("===================================\n")

  # Return a correct input
  max = utilities.check_input("Veuillez entrer le nombre maximum pour effectuer la somme : ")

  # Sum of all the multiples of 5 and 7
  result = sum([x for x in range(max) if x % 5 == 0 or x % 7 == 0])

  print("\nLa somme des multiples de 5 et 7 du nombre que vous avez entré est égale à :", result)
  print("===================================\n")

# -----------------------------------------------------------------------------------------------
# ===============================================================================================

# Problème no 2 :
# ---------------
# En prenant en compte les termes de la suite de Fibonacci dont les valeurs ne dépassent pas x, trouver la somme des termes impairs.
def problem_2():
  print("\nVous avez sélectionné le problème suivant :")
  print("-----------------------------------")
  print("En prenant en compte les termes de la suite de Fibonacci dont les valeurs ne dépassent pas x, trouver la somme des termes impairs")
  print("===================================\n")

  # Return a correct input
  max = utilities.check_input("Veuillez entrer le nombre maximum pour les valeurs contenues dans la suite de Fibonacci : ")

  # Declaration of the table containing the Fibonacci suite
  fibonacci = [1, 1]

  # Fibonacci calculation
  while fibonacci[-1]+fibonacci[-2] < max:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

  print("\nVoici la suite de Fibonacci pour le nombre maximum renseigné : ", fibonacci)

  # Sum of all the odd numbers
  result = sum([x for x in fibonacci if x % 2 == 1])

  print("La somme des termes impairs de la suite de Fibonacci suivante est égale à :", result)
  print("===================================\n")
    
# -----------------------------------------------------------------------------------------------
# ===============================================================================================

# Problème no 3 :
# ---------------
# Quel est le plus grand facteur premier du nombre x ?
def problem_3():
  print("\nVous avez sélectionné le problème suivant :")
  print("-----------------------------------")
  print("Quel est le plus grand facteur premier du nombre x ?")
  print("===================================\n")

  # Return a correct input
  number = utilities.check_input("Veuillez entrer le nombre dont vous voulez trouver les facteurs premiers : ")
  
  # List of all the prime numbers found in the range max divided by 2
  prime_numbers = utilities.list_prime_numbers(number//2)
  
  # List for the prime factors that will be found
  prime_factors = []

  # Loop to check all the prime factors
  for prime in prime_numbers:
    while number%prime == 0:
      number //= prime
      prime_factors.append(prime)
  
  # If no prime factor, the number entered is its own
  if len(prime_factors) == 0:
    prime_factors.append(number)

  print("\nVoici la liste des facteurs premiers pour le nombre renseigné : ", prime_factors)
  print("\nVoici le plus grand facteur premier pour le nombre renseigné : {}".format(max(prime_factors)))
  print("===================================\n")

# -----------------------------------------------------------------------------------------------
# ===============================================================================================


# Problème no 4 :
# ---------------
# Quel est le plus grand palindrome que l'on peut obtenir en multipliant un nombre de x chiffres avec un nombre de y chiffres ?
def problem_4():
  print("\nVous avez sélectionné le problème suivant :")
  print("-----------------------------------")
  print("Quel est le plus grand palindrome que l'on peut obtenir en multipliant un nombre de x chiffres avec un nombre de y chiffres ?")
  print("===================================\n")
  
  digit1 = utilities.check_input("Veuillez entrer le premier nombre de chiffres : ")
  digit2 = utilities.check_input("Veuillez entrer le deuxième nombre de chiffres : ")

  # Get the greatest number in the range of the digit (example : if digit = 3, max = 999)
  greatest1 = utilities.greatest_number(digit1)
  greatest2 = utilities.greatest_number(digit2)

  palindrome = 0

  # Multiplication till a palindrome is found
  for number1 in range(greatest1, -1, -1):
    for number2 in range(greatest2, -1, -1):
      resultat = number1*number2

      # Check if it's a palindrome
      if(utilities.is_palindrome(resultat)):
        if(resultat > palindrome):
          palindrome = resultat

  print("Le nombre suivant est un palindrome : {}".format(palindrome))

# -----------------------------------------------------------------------------------------------
# ===============================================================================================
