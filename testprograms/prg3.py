l=[5,3,4,3,7,4,3]
def second_occurance(l,n):
    count=0
    for i in l:
        if i==n:
            count+=1
        if count == 2:
            return i
    return 0
print(second_occurance(l,3))

