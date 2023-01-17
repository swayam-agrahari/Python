#factorial
"""a= int(input("Enter the number?"))
x=1
for i in range(1,a+1):
	x=i*x
print ("The fact is"+str(x)) """

#MULTIPLICATION_TABLE 
""" n=int(input("Enter any number: "))
for i in range(1,11):
	print(str(n) +" * "+str(i)+" = "+str(n*i)) """

#pattern
""" row=6
col=6
for i in range(row):
	for j in range(i+1):
		print(j+1,end="")
	print("") """

#palindrome
""" a=str(input("Enter a word: "))
b=a[::-1]
if(a == b):
	print(a +" is palindrome!!!")
else:
	print(a +" is not palindrome!!!") """

#prime_or_composite
""" a=int(input("Enter a number: "))
b=0
for i in range(1,a+1):
	if(a%i == 0):
		b=b+1
if(b == 2):
	print(str(a)+" is prime")
else:
	print(str(a)+" is not prime") """

