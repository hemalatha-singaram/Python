import numbers
from operator import add
def login(username,password):
	if username=="admin" and password==1234:
		print("access granted")
	else: print("access denied")
login("hema",234)
login("admin",1234)


