#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
	number = number * -1
last_digit = number % 10
