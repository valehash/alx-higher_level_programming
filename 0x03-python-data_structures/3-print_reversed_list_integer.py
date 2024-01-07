#!usr/bin/python3
def print_reversed_list_integer(m_list=[]):
	count = 0
	lenght = len(m_list)
	while(lenght > count):
		print('{:d}'.format(m_list[lenght - 1]))
		lenght -= 1

