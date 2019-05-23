# ===================================
# FILE WHERE ALL UTILITIES ARE STORED
# ===================================

# Imported modules
import problem_1_to_32


# List containing all resolved problems
problems = [
  "1) Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x",
  "2) En prenant en compte les termes de la suite de Fibonacci dont les valeurs ne dépassent pas x, trouver la somme des termes impairs"
]

# Dictionnary containing all functions
functions = {
  1: problem_1_to_32.problem_1,
  2: problem_1_to_32.problem_2
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