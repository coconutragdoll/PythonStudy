#!/usr/bin/env python
print 'Welcome to the grade conversion tool!'
while True:
	score = int(raw_input("Enter 999 to exit. Please enter score-->"))
	if score == 999:
		print 'Have a nice day!'	
		break
	elif score >  100:
		print 'Invalid score'
	elif score < 0:
		print 'Invalid score'
	elif score>=90:
		print "Grade A"
	elif score>=80:
		print 'Grade B'
	elif score>=70:
		print 'Grade C'
	elif score>=60:
		print 'Grade D'
	else:
		print 'Grade E'
else:
	print 'shouldnot see this'
