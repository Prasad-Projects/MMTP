from subprocess import call
from random import randint
#for _ in range(100):
u = 1642
for i in range(101):
	x = randint(0,u)
	y = randint(0,u)
	z = call(["python","CSA_v3.py",str(x),str(y)])
	print z
	