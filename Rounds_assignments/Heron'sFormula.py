# Jace R
# Python II
# Period 3
import math
a = input("input 1\n")
while(int(a) == 0 or "-" in str(a)):
  a = input("That is not a valid number, negatives and zeros are not accepted")
b = input("input 2\n")
while(int(b) == 0 or "-" in str(b)):
  b = input("That is not a valid number, negatives and zeros are not accepted")
c = input("input 3\n")
while(int(c) == 0 or "-" in str(c)):
  c = input("That is not a valid number, negatives and zeros are not accepted")
a = int(a)
b = int(b)
c = int(c)

x = (a + b + c)/2
output = (math.sqrt(x*(x-a)*(x-b)*(x-c)))
print(output)
