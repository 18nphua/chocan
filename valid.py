"""
File: valid.py
Name: Huan Nguyen 
Desc: This file contains utility functions to validate for a specific
      data type.
      preventing runtime errors

"""

def read_int(prompt = "Please enter an integer"):
    num = 0 
    valid = False

    #Repeatedly prompts the user for input until 
    #they enter an integer.
    while not valid:

        #Attempts to convert the the user input to an integer.
        try:
            num = int(input(prompt))
            valid = True

        #Throws an exception if the user enters a non-integer value.
        except:
            print("Invalid input type. Please enter an integer")

    return num

def read_float(prompt="Please enter a float: ", error="Invalid float."):
  num = 0
  valid = False

  #Repeatedly prompts the user for input until 
  #they enter a floating-point value.
  while not valid:
      try:
          num = float(input(prompt))
          valid = True
      except:
          print(error)

  return num

  
def read_string(prompt="Please enter a string: "):
  valid = False
  chars = ""

  #Repeatedly prompts the user for input until 
  #they enter a character string.
  while not valid:
      chars = input(prompt)
      if chars != "":
          valid = True
      else:
          print("\nInvalid string.")
  return chars


def read_y_or_n(prompt="Please enter 'y' or 'n': "):
  answer = ""
  answer = input(prompt)
  answer = answer.lower()

  #Repeatedly prompts the user for input until 
  #they enter valid response.
  while (answer != "n" and 
         answer != "y" and 
         answer != "no" and 
         answer != "yes"):
      print("Invalid response.")
      answer = input(prompt)
      answer = answer.lower()

  return answer[0]
