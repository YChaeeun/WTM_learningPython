def int_div(a, b) :
    root = a // b
    remainder = a % b
    print("Root: ", root)
    print("Remainder", remainder)

n1 = int(input("A number: "))
n2 = int(input("Divided by: "))
print(int_div(n1, n2))



def bet_sum(c, d) :
    c = int(c)
    d = int(d)
    sum = 0
    for i in range(c+1, d):
        sum += i
    print(sum)
n1 = int(input("Num"))
n2 = int(input("Num2"))

print(bet_sum(n1, n2))
