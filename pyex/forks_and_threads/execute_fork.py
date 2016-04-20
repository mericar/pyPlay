# introduction to os.execlp
# We are starting new python programs from inside this program. 
# os.execlp has parameters that represent command line arguments.

import os

#This program keeps creating new programs, as specified in processor.py
p = 0
while True:
	p += 1
	pid = os.fork()
	if pid == 0:
		os.execlp('python','python','processor.py',str(p))
		assert False, 'error starting program'
	else:
		print('the child is: ', pid)
		if input() == 'Q': break
