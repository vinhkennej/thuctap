print "vi du ve doc file"

tenfile=raw_input(">")
txt_file= open(tenfile,'a+')

print txt_file.read()
content=raw_input("Noi dung file : ")
txt_file.write(content)
#print txt_file.read()




