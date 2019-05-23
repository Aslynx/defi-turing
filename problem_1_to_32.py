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
