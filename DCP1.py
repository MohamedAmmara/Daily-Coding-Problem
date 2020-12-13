#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
def fun(lst, k):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i]+lst[j]==k:
                return True
    return False
print(fun([10, 15, 3, 7], 17))