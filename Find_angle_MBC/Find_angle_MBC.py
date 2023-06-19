# Enter your code here. Read input from STDIN. Print output to STDOUT
ab = int(input())
bc = int(input())
pi = 22 / 7
import math

x = math.atan(ab/bc)
x = x* (180/pi)
x = str(round(x))
print(x+chr(176))

#In my opinion, critical point in this problem is that to add degree symbol to your solution.