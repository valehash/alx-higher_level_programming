#!/usr/bin/python3
if __name__ == "__main__":
	import sys

	args = sys.argv
	num = len(sys.argv) - 1
	size = 0
	if num == 0:
		print('{:d} arguments.'.format(num))
	elif num == 1:
		print('{:d} argument:'.format(num))
		print('{:d}: {:s}'.format(num, args[num]))
	else:
		print('{:d} arguments:'.format(num))
		while (size < num):
			size += 1
			print('{:d}: {:s}'.format(size, args[size]))
