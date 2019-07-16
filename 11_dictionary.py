# 12-1-1
dc = {'새우깡' : 700, '콘치즈' : 850, '꼬깔콘' : 750}
dc['홈런볼'] = 900
print(dc)

# 12-1-2
for i in dc :
    dc[i] += 100
print(dc)

# 12-1-3
del dc['콘치즈']
dc['치즈콘'] = 950
print(dc)
