# define x as sentence, replace variable d with 10
x = "There are %d types of people." % 10
# define variable binary as binary
binary = "binary"
# define variable do_not as don't
do_not = "don't"
# define y as sentence, replace variable s with content of binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

#print x (There are...)
print x
#print x (Those who...)
print y

#print and replace r with content of x (There are..)
print "I said: %r." % x
#print and replace s with content of y (those who..)
print "I also said: '%s.'" %y

# define hilariouse to False
hilarious = False
#define joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#print content of joke_evaluation and hilarious
print joke_evaluation % hilarious

#define w and e
w = "This is the left side of..."
e = "a string wich a right side."

#print w+e (sentences)
print w+e