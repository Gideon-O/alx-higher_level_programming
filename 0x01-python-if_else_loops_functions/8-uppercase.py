#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('i') >= ord('a') and ord('i') <= ord('z'):
		i = chr(ord(i) - 32)
		if ord('i') > ord('Z'):
			i = chr(ord(i) - ord('A'))
	print("{:s}".format(i))
	print()
