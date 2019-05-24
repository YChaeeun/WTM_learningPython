# 0528
# 반복문 for while


### 문제 1 : 문자열
def upperLowerString() :
    string = input("문자열을 입력하세요: ")
    list1 = []
    for i in string :
        if not(i.isalpha()) : list1.append(i)
        elif i.isupper() : list1.append(i.lower())
        elif i.islower() : list1.append(i.upper())

    return ''.join(list1)


### 문제 2 : 2단 ~ 9단의 구구단을 모두 출력하세요
def multipleTable() :
    for i in range(2,10) :
        print(f"{i}단 :", end=' ')
        for j in range(1,10) :
            print(i*j, end=' ')
        print()


### 문제 3 : 문자열을 입력하면 n만큼 이동해서 암호 만들기
def secretString() :
    string, num = input("문자열과 정수 한 개 : ").split(', ')
    
    codeList = []
    for char in string :  # 공백일 경우
        if not(char.isalpha()) : codeList.append(char) 
        else :
            makeCode = chr(ord(char)+int(num))
            codeList.append(makeCode)
    print("".join(codeList))


### 문제 4 : 임의의 정수들을 입력받아 합계를 계산하여 출력하세요
def sumAll() :
    listofNum = []

    while 1 :
        try :
            num = int(input("정수를 입력하세요 (0을 입력하면 종료) : "))
        except :
            print("잘못된 입력입니다.")
            continue
        if num == 0 : break

        listofNum.append(num)

    print("입력한 정수 :", listofNum)
    print(f"합계 : {sum(listofNum)}, 평균 : {int(sum(listofNum)/len(listofNum))}")


### 문제 5 : UP DOWN 게임 만들기
def updownGame() :
    import random
    guessNum = random.randint(0,100)
    print(guessNum)
    count = 5
    while count > 0 :
        try :
            num = int(input("\n숫자를 입력하세요 : "))
        except :
            print("잘못된 입력입니다")
            continue
        if num > 100 or num < 0 :
            print("0~100 사이의 숫자를 입력하세요")
            continue

        count -= 1
        if count == 0 and num != guessNum:
            break
        if num > guessNum :
            print(f"DOWN! (남은 기회 : {count}번)")
        elif num < guessNum :
            print(f"UP! (남은 기회 : {count}번)")
        else :
            print("정답입니다!")
            return


    print("땡! 틀렸습니다")
    print("\n(종료)")


# 문제를 풀고싶으면 주석을 해제해 주세요! 

# 문제 1
#upperLowerString()

# 문제 2
#multipleTable()

# 문제 3
# secretString()

# 문제 4
#sumAll()

# 문제 5
#updownGame()

