def add(a,b):
	print "add %d +%d " %(a,b)
	return a+b	
def subtract(a,b):
	print "subtracting %d-%d" %(a,b)
	return a-b
def multiply(a,b):
	print " Multiply %d * %d " %(a,b)
	return a*b
def divide(a,b):
	print "Driving %d /%d" %(a,b)
	return a /b
print "Let's do some math with just function~"

age=add(30,5)
height =subtract(78,4)
weight=multiply(100,2)
iq=divide(100,2)

print "Age: %d ,Height: %d , Weight: %d , IQ: %d" %(age,height,weight,iq)

print "here is a puzzle"

what=add(age,subtract(height,multiply(weight,divide(iq,2))))

#print "THat becomes: ",what,"can you do it by hand?"
