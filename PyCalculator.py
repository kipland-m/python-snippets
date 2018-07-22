# 02/21/18

import random
import time
import statistics
import sys

print("Welcome to Kip's Python Calculator!\n")

time.sleep(.5)

CalcFunction = input("""Please choose a function\n
1. Addition\n
2. Subtraction\n
3. Multiplication\n
4. Division\n
5. Quit\n
Please enter a number: """)

if CalcFunction == "1":
  AdditionX = int(input("\nPlease enter your first number: "))
  AdditionY = int(input("\nPlease enter your second number: " ))
  print("\nYour answer is: ",AdditionX + AdditionY,"\n")

if CalcFunction == "2":
  SubtractionX = int(input("\nPlease enter your first number: "))
  SubtractionY = int(input("\nPlease enter your second number: " ))
  print("\nYour answer is: ",SubtractionX - SubtractionY,"\n")

if CalcFunction == "3":
  MultiplyX = int(input("\nPlease enter your first number: "))
  MultiplyY = int(input("\nPlease enter your second number: " ))
  print("\nYour answer is: ",MultiplyX * MultiplyY,"\n")

if CalcFunction == "4":
  DivideX = int(input("\nPlease enter your first number: "))
  DivideY = int(input("\nPlease enter your second number: " ))
  print("\nYour answer is: ",DivideX / DivideY,"\n")

if CalcFunction == "5":
  sys.exit()
