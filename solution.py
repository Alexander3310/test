import sys
digit_str = sys.argv[1]
sum = 0
for i in digit_str:
	sum = sum.__add__(int(i))
print(sum)
