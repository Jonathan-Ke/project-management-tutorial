# Pythagorean Solver
# Alpha version 1.0
# Coder: Jonathan Kessler
# Date: 2024-10-14
import math as Math
# declares variables 
sideA = 0
sideB = 0
sideC = 0

# equatoin: a*a + b*b = c*c

# declare functions
def solver(a,b):
    c = (Math.pow(a,2)) + (Math.pow(b,2))
    sideC = Math.sqrt(c)
    return sideC

print("Pythagorean Theorem Solver")
print("Written by Jonathan")
print("Version 1.0")
print("---------------------------")
# get user input
sideA = float(input("Enter the length of side A: "))
sideB = float(input("Enter the length of side B: "))

# solve equation
# sideA variable will pass data to the a parameter
# sideB variable will pass data to the b parameter

print("Side C: " +str(solver(sideA,sideB))) #print whatever date is returned from the functution


