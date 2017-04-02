def secret_formalu(started):
	jelly_beans=started *5000
	jars=jelly_beans /1000
	crates=jars /100
	return jelly_beans ,jars,crates
start_point=1000

beans ,jars,crates=secret_formalu(start_point)

print "With a starting point of: %d" %start_point
print"we'd have %d beans , %d jars ,and %d crates." %(beans,jars,crates)

start_point=start_point /10

print "we can also do that this way:"
print "We'd have %d beans , %d jars , and %d crates " %secret_formalu(start_point) 
