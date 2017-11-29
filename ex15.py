#access the sys library and the argv module
from sys import argv


script, filename = argv

#open file
txt = open(filename)

#prints line
print "Here's your file %r:" %filename
# do txt.read without parameters
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

#open file
txt_again = open(file_again)

print txt_again.read ()