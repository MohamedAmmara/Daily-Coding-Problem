#Given an array of integers, return a new array such that each element at index i of the new array
# is the product of all the numbers in the original array except the one at i.
def fun(lst):
    lt=[]
    for i in range(len(lst)):
        fact=1
        for j in range(len(lst)):
            if i==j:
                continue
            fact *= lst[j]
        lt.append(fact)
    return lt
print(fun([1, 2, 3, 4, 5]))