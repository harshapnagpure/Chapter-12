def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Harsha")#rather than value string we print then its print this statement

a = increment("xswdx")#this increment the number by 1
print(a)