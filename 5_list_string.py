# 05-1-1
st = [1,2,3,4]
print(st[0], st[1], st[2], st[3])

# 05-1-2
st = [1,2,3,4]
print(st[-4], st[-3], st[-2], st[-1])

# 05-1-3
st = [1,2,3,4]
st[0] += 1
st[1] += 1
st[2] += 1
st[3] += 1
print(st)

# 05-1-4
st = [1,2,3,4,5,6,7,8,9,10]
for i in range(10) :
    st[i] += 1
print(st)

# 05-1-5
st = [1,2,3,4,5,6]
st[0], st[5] = st[5], st[0]
print(st)

# 05-2-1
st = [1,2,3,4,5]
st[1:4] = [3,3,3]
print(st)

# 05-2-2
st = [1,2,3,4,5]
st[3:4] = [3.5,4]
print(st)

# 05-2-3
st = [1,2,3,4,5]
st[1:4] = []
print(st)

# 05-2-4
st = [1,2,3,4,5]
st[0:5] = []
print(st)

# 05-2-5
st = [1,2,3,4,5,6,7,8,9,10]
nt = st[0:10:2]
print(nt)

# 05-2-6
st = [1,2,3,4,5,6,7,8,9,10]
nt = st[1:10:2]
print(nt)

# 05-3-1
str = "Hello"
str += "Python!"
print(str)

# 05-4-1
def sum_all(st) :
    sum = 0
    for i in range(len(st)) :
        sum += st[i]
    print(sum)
result = sum_all([1,2,3,4,5])
print(result)

# 05-4-2
def show_reverse(st) :
    for i in range(len(st)) :
        print(st[(i+1)*-1], end=' ')
print(show_reverse([1,2,3,4,5]))
print(show_reverse("SINGandDANCE"))
