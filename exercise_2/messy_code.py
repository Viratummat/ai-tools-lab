def calc(x,y,z):
    a=x+y
    b=a*z
    c=b/z
    return c

def proc(s):
    l=len(s)
    if l>5:
        x=s[0:3]
        y=s[3:l]
        return x+y
    else:
        return s

def findval(lst,v):
    for i in range(len(lst)):
        if lst[i]==v:
            return i
    return -1

result1=calc(10,20,5)
result2=proc("hello world")
result3=findval([1,2,3,4,5],3)
print(result1,result2,result3)