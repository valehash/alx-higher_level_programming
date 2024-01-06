#!usr/bin/python3
def print_list_integer(m_list=[]):
	count = 0
	lenght = len(m_list)
	while(lenght > count):
		print('{:d}'.format(m_list[count]))
		count += 1

