# ===================================
# FILE WHERE ALL UTILITIES ARE STORED
# ===================================

# Imported modules
import problem_1_to_32


# List containing all resolved problems
problems = [
  "1) Trouver la somme de tous les multiples de 5 ou 7 inférieurs à x"
]

# Dictionnary containing all functions
functions = {
  "1": problem_1_to_32.problem_1
}

# Function to search the correct function for the problem asked
def problem_to_solve(number):

  # Search the function in the dictionnary
  func = functions.get(number, lambda: "No function found.")

  # Execute the function if founded
  func()