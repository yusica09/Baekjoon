A = int(input())
B = int(input())
C = int(input())

if (A == 60 and B == 60 and C == 60):
    print('Equilateral')
elif ( A+B+C != 180):
    print('Error')
elif (A == B or B == C or C == A):
    print('Isosceles')
else:
    print('Scalene')