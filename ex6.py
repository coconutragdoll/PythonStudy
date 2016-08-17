# initialize some string
x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
# pay attention to how paran is used here
y = "Those who know %s and those who %s." % (binary, do_not)

# print x and y string
print x
print y

# print I said in front of strings
print 'I said: %r.' % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# plus is used to join two strings
print w + e