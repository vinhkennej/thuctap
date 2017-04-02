from sys import argv
from os.path import exists

script ,from_file , to_file=argv

print "Copying from %s to %s " %(from_file,to_file)

in_file=open(from_file)
in_data=in_file.read()

print "the input file is %d bytes long" %len(in_data)

print "Does the output file exist? %r" %exists(to_file)
print "Ready ,hit Return to continue , Ctrl-C to abort. "

raw_input()

out_file=open(to_file,'w')
out_file.write(in_data)

print "Alright, all done"

out_file.close()
in_file.close()

