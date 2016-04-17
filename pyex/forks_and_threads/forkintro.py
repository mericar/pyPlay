"""
#Process introduction, forks processes and exits children processes

import os

def child_process():
	print('this is the child : ', os.getpid())
	os._exit(0)

def parent_process():
	while True:
		newprocessid = os.fork()
		if newprocessid == 0:
			child_process()
		else:
			print('This is the parent process, ', os.getpid(), ' of ', newprocessid)
		if input() == 'T': break

parent_process()

"""


#Maintains a specified number of processes for a given time period

import os, time

N = 1000000
NUM = 1000000

# defines a function that produces the square of the input 
def squarer(i):
	return i*i

# defines a counter function
def count_keeper(count):
	for i in range(count):
		time.sleep(1)
		print('[%s] is on iteration %s of %s ...' % (os.getpid(), i, count))

# defines a function which takes a function and executes the function n times.
def do_n_times(func, n, *args):
	for i in range(n):
		func(*args)

# defines a process generator and executes a computation inside func
def process_generator(times):
	for i in range(times):
		pid = os.fork()
		if pid == 0:
			print('The process %d has been generated. ' % pid)
		else:
			count_keeper(5)
			do_n_times(squarer, NUM, N)
			os._exit(0)

# defines a localized running context for process generation
def forker(pcount):
	process_generator(pcount)
	print('The primary process has completed.')

forker(100)




























