from random import randrange

print("Hi enter an integer")

try:
	playagain = "yes"
	while (playagain == "yes"):
		x = randrange(15)
		y = randrange(15)
		answer = x // y 
		print ( str(x)+"/" + str(y))
		guess = input ("")
		if answer == int(guess):
			print ("\n correct!")
			
		else:
			print("\n correct!")
		playagain = input("Do you want to claculate again?: ")
	else:
		print("Good bye!")
		

except ValueError:
    print(" Please enter an integer!")
    

except ZeroDivisionError:
    print("You cannot devide by zero")
