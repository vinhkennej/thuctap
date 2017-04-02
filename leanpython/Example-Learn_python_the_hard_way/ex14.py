from sys import argv
script,user_name=argv


print "Hi %s,I'm the %s script. " %(user_name,script)
print "Hi'd like to ask you a few question"
print "Do you like me %s?" %user_name
likes=raw_input("Da bong")

print "where do you live %s" %user_name
lives=raw_input()

print "what kind of computer do you have? "
computer =raw_input()

print """

Alright , so you said %r about liking me.
you live in %r . Not sure whare that is .
And you have a %r compouter . Nice .
""" %(likes,lives,computer)
