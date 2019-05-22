# ==================================================
# FILE CONTAINING THE LIST OF PROBLEMS NR 1 TO NR 32
# ==================================================

# Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x
def problem_1():
  print("\nVous avez sélectionné le problème suivant :")
  print("-----------------------------------")
  print("Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x")
  print("===================================\n")

  is_ok = False

  while is_ok == False:
    max = input("Veuillez entrer le nombre maximum pour effectuer la somme : ")

    if not max.isdigit():
      print("Veuillez entrer une valeur correcte.")
    else:
      is_ok = True
      max = int(max)

  # Sum of all the multiples of 5 and 7
  result = sum([x for x in range(max) if x % 5 == 0 or x % 7 == 0])

  print("La somme des multiples de 5 et 7 du nombre que vous avez entré est égale :", result)
  print("===================================\n")
