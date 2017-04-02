#!/usr/bin/env python
import sys
import random 
ans =True
while ans:
	question= raw_input("ask the magic 8 ball a question : (press enter to quit)")
	answers=random.randint(1,4)
	if question=="":
		sys.exit()
	elif answers==1:
		print "it is certain"
	elif answers==2:
		print "outlook good"
	elif answers==3:
		print "you may reply on it"
	elif answers==4:
		print " ans again later" 
