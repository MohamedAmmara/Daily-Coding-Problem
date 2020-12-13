#Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does
# not necessarily have to be contiguous.

#For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing
# subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
lst=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
lst1=[]
lst2=[]
for i in range(len(lst)-1):
    lst1=[lst[i]]
    for j in range(i+1, len(lst)):
        if lst[j]>lst1[-1]:
            lst1.append(lst[j])
    lst2.append(len(lst1))
    print(lst1)
print(max(lst2))