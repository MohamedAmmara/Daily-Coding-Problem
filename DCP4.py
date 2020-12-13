# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
n=[3, 4, -1, 1]
lst=[]
for i in sorted(n):
	if i > 0:
		lst.append(i)
i=1
while True:
	if not i in lst:
		break
	i+=1
print(i)