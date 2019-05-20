# 0521
# 함수 function

# 문제 1: 입력한 정수 세 개를 함수의 인수에 따라 곱셈(mul) 또는 덧셈(sum)
def mulORsum(n1,n2,n3, todo) :
    if todo == 'mul' :
        return n1*n2*n3
    elif todo == 'sum' :
        return n1+n2+n3



# 문제 2 : 이름과 좋아하는 색, 취미 소개하기
def introduce(name, color, hobby) :
    print(f"저의 이름은 {name}이고, 좋아하는 색은 {color}, 취미는 {hobby}입니다.")



# 문제 3 : 입력받은 문자의 소문자는 대문자 대문자는 소문자로 바꾸는 함수
def upperLowerchar(char) :
    if char.isupper() : return char.lower()
    elif char.islower() : return char.upper()



# 문제 4 : 다른 글자 만들기
def secretCode(string, num) :
    return chr(ord(string)+num)


# 문제 5 : 4개의 정수를 입력받아
def sortList(howto, listofNum) :
    if howto == '오름' :
        listofNum.sort()
        return listofNum
    elif howto == '내림' :
        result = sorted(listofNum, reverse=True)
        return result




while True :
    num = input('\n풀고 싶은 문제 번호를 입력하세요 : ')
    
    try :
        num = int(num)
    except :
        print('끝')
        break

    if num == 1 :
        a,b,c = map(int, input("정수 세 개를 입력하세요 : ").split())
        todo = input("곱셈? 덧셈? : ")
        result = mulORsum(a,b,c,todo)
        print("결과 :", result)

    elif num == 2 :
        name, color, hobby = input('이름과 좋아하는 색, 취미를 입력하세요').split()
        introduce(name, color, hobby)

    elif num == 3 :
        char = input("문자를 입력하세요 : ")
        print(upperLowerchar(char))

    elif num == 4 :
        char, move = input("문자와 정수 한 개 : ").split()
        code = secretCode(char, int(move))
        print(code)

    elif num == 5 :
        
        a,b,c,d = map(int, input("정수 네 개를 입력하세요 : ").split())
        list1 = [a,b,c,d]
        # list1.append(a)

        howto = input("어떻게 정렬할까요? : ")
        print(sortList(howto, list1))

    else :
        print("1~5 사이의 숫자를 입력해주세요")
        continue
