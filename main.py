# =======================================
# FILE WHERE THE PROBLEM WILL BE EXECUTED
# =======================================

# Imported modules
import sys
import utilities

# Main function : Where the choice of the exercise will happen
def main():

  print("List of all resolved problems (list is in french) : ")
  print("---------------------------------------------------\n")

  # Print the list of all resolved problems
  for problem in utilities.problems:
    print("\t{}".format(problem))
  
  print("\n---------------------------------------------------")
  print("Select the problem you want to see resolved :")

  # Prompt for the number 
  number = input()

  # Function that will look into the list of problems to solve
  utilities.problem_to_solve(number)

# Required condition to execute function "main()"
if __name__ == "__main__":
    main()