import random

def Frandom():
	return random.randint(1,20)

x = Frandom()
print x
print "Welcome to Number Generator!"
print "Can you guess the number? Just try it!"
print "You have to enter numbers from one to twenty."

count=0
while count<4:
	count=count+1
	print "You have "+str(5-count)+" attempts."
	try: 
		y= int(raw_input("Please enter a number: "))
		if y==x:
			print "You win!"
			rest=raw_input("Jugar de nuevo y/n ")
			if rest=="y":
				x = Frandom()
				print x
				count = 0 
				pass
			else:
				break
		elif count == 4:
			print "Game Over!"
			restGO=raw_input("Jugar de nuevo y/n ")
			if restGO=="y":
				x = Frandom()
				print x
				count = 0 
				pass
			else:
				print "Gracias"
				break
		elif y>x:
			print "You guessed to high, please try again"
			
		elif y<x:
			print "You guessed to low, please try again"
			
	except:		
		print "Please enter a number. Try again...."
