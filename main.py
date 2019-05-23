# =======================================
# FILE WHERE THE PROBLEM WILL BE EXECUTED
# =======================================

# Imported modules
import sys
import utilities

# Main function : Where the choice of the exercise will happen
def main():

  print("\t-----------------")
  print("\t-- Défi Turing --")
  print("\t-----------------\n")
  
  # Program
  must_be_stopped = False

  # Loop to keep going on the problem resolving
  while must_be_stopped == False:

    print("Liste des problèmes résolus :")
    print("-----------------------------")

    # Print the list of all resolved problems
    for problem in utilities.problems:
      print("\n\t{}".format(problem))
      
    print("\n=============================\n")
    
    # Check if the value of the input is correct
    number = utilities.check_input("Sélectionnez le problème que vous souhaitez résoudre : ")

    # Function that will look into the list of problems to solve
    utilities.problem_to_solve(number)

    # Value
    is_ok = False

    # Condition to end the program
    while is_ok == False:  
      stop = input("Voulez-vous arrêter le programme ? (y/n) ")
      
      # Check if the value of the input is correct
      if stop.isdigit() or (stop != 'y' and stop != 'n'):
        print("Veuillez rentrer une valeur correcte.")
        continue
      elif stop == 'n':
        is_ok = True
      else:
        is_ok = True
        must_be_stopped = True

    print("===============================\n")

# Required condition to execute function "main()"
if __name__ == "__main__":
    main()