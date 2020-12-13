#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
data=input()
def decode(data):
    if len(data) == 0:
        return 1
    else:
        if len(data) == 1:
            if data[0] == "0":
                return 0
            else:
                return 1
        elif int(data[0:2]) < 27 and int(data[0:1])>0:
            return decode(data[1:])+decode(data[2:])
        elif data[0] != "0":
            return decode(data[1:])
        else:
            return 0
print(decode(data))
