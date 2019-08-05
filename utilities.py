# ===================================
# FILE WHERE ALL UTILITIES ARE STORED
# ===================================

# Imported modules
import math
import problem_1_to_32


# List containing all resolved problems
problems = [
  "1) Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x",
  "2) En prenant en compte les termes de la suite de Fibonacci dont les valeurs ne dépassent pas x, trouver la somme des termes impairs",
  "3) Quel est le plus grand facteur premier du nombre x ?",
  "4) Quel est le plus grand palindrome que l'on peut obtenir en multipliant un nombre de x chiffres avec un nombre de y chiffres ?",
  "5) Que vaut la somme des chiffres composant le nombre x^y ?"
]

# Dictionnary containing all functions
functions = {
  1: problem_1_to_32.problem_1,
  2: problem_1_to_32.problem_2,
  3: problem_1_to_32.problem_3,
  4: problem_1_to_32.problem_4,
  5: problem_1_to_32.problem_5
}

# Function to search the correct function for the problem asked
def problem_to_solve(number):

  # Search the function in the dictionnary
  func = functions.get(number, lambda: "Aucun problème sélectionné.")

  # Execute the function if founded
  func()

# Function to check the input for the selection and resolution of a problem
def check_input(text):

  # Value
  is_ok = False

  while is_ok == False:
    max = input(text)

    if not max.isdigit():
      print("Veuillez entrer une valeur correcte.")
    else:
      is_ok = True
      max = int(max)
  
  return max

# Function to find a list of prime numbers in the range of the argument
def list_prime_numbers(max):
  prime_numbers = []

  for prime in range(2, (max)+1):
    isPrime = True
    for num in range(2, int(prime ** 0.5) + 1):
      if prime % num == 0:
        isPrime = False
        break

    if isPrime:
      prime_numbers.append(prime)  

  return prime_numbers

# Function to find the greatest number in the range 
def greatest_number(digit):
  max = "9" * digit
  
  return int(max)

# Function to check if it's a palindrome
def is_palindrome(palindrome):
  number = str(palindrome)
  reversed = number[::-1]
  return number == reversed

# Function to get the factorial from the math module
def factorial(exponent):
  return math.factorial(exponent)
