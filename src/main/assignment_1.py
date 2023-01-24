import numpy as np
import math

binary = [0,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,0,0,1]
end = len(binary)

# Question 1
s = binary[0]

c = 0
for i in range(1, 12):
    c += binary[i] * pow(2, 11 - i)

f = 0
for i in range(12, end):
    f += binary[i] * pow(0.5, i - 11)

value1 = pow(-1, s) * pow(2, c - 1023) * (1 + f)
print("%.5f" % value1)

# Question 2
value2 = int(value1)
print("%.0f" % value2)

# Question 3
value3 = value2 + 0.5
print("%.0f" % value3)

# Question 4
print(value1 - value3)
print((value1 - value3) / value1)

# Question 5
print(math.ceil(pow(10, 4/3) - 1))

# Question 6
tol = pow(10 ,-4)
a = -4
b = 7
max = 100

iter = 0
while abs(a - b) >= tol and iter < max:
    iter += 1
    x = (a + b) /2
    f = pow(x,3) + 4 * pow(x,2) - 10
    if f > 0:
        b = x
    else:
        a = x
print(iter)

x = 7
iter = 0
while iter < max:
    
    iter += 1
    f = pow(x,3) + 4 * pow(x,2) - 10
    fd = 3 * pow(x,2) + 8 * x
    if fd != 0:
        y = x - (f / fd)
        if(abs(x - y) < tol):
            break
        x = y
print(iter)