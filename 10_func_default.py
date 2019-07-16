#10-1-1
for i in range(3) :
    print(i, i+1, i+2, sep = ', ')

#10-2-1
def add1(s) :
    for i in range(len(s)) :
        s[i] += 1
    return s
st = [1,2,3,4,5]
st2 = add1(st)
print(st2)
