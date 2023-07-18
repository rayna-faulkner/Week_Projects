iterationsNum = int(input("Enter the number of iterations: "))

approx = 0
sign = 1

for i in range(1, iterationsNum * 2 + 1, 2):
    approx += sign * (1 / i)
    sign *= -1

approxPi = 4 * approx

print("The approximation of π after", iterationsNum, "iterations is: ", approxPi)
