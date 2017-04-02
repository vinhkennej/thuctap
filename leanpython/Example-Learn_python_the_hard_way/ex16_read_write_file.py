from sys import argv
script , filename=argv

print "we're going to erase %r. " %filename
print "If you don;t want that,hit Ctrl-c "
print "If you do want that , hit return"

raw_input("?")

print "Open the file .."
target=open(filename,'w')

print "Truncating the file . Goodbye !"
#target.truncate()

print "Now I'm going to ask you for three lines "

line1=raw_input("line1 : ")
line2=raw_input("line 2: ")
line3=raw_input("line 3L ")

print "I'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally , we close it "
target.close()

