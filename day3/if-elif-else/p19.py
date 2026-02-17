num=int(input("enter a number:"))
if num>0:
	if num % 2==0:
		if num>100:
			print(num,"is larger positive even")
		else:print(num,"is small positive even")
	else:print(num,"is positive odd")
else:print(num,"is not positive")