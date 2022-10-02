#Importing randome module
import random

# Initiating an white loop to keep the program execting
while True:
  print("Rolling Dice...")
  
  #using random.randint(1,6)) to generate a random value between 1 & 6
  print(f"The value is ", random.randint(1,6))
  
  # Asking user to roll the dice again or quit
  repeat = input("Roll Dice again? 'y' for yes & 'n' for no: ")
        
  # if the user answers negative the loop will break and program execution stops otherwise the program will continue executing
  if repeat == 'n':
      break
