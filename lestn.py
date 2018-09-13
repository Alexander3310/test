import sys
num = int(sys.argv[1])
str = ''
for i in range(1, num+1):
	str = " "*(num-i) + "#"*i
	print(str)
	str = ''
