# 0514
# IF 조건문 문제

# 문제 1 : 정수 하나를 입력받아 양수음수/홀수짝수 여부 판단하기
num = int(input("정수 하나를 입력하세요 : "))

if num > 0:
   print(f"{num} : 양수") 
else:
    print(f"{num} : 음수")

if num % 2 == 0 :
    print(f"{num} : 짝수\n")
else :
    print(f"{num} : 홀수\n")



# 문제 2 : 성적 입력하기
score = int(input("한 명의 성적을 입력하세요 :"))
if score >= 85 :
    print("성적 : A")
elif score >= 70 :
    print("성적 : B")
elif score >= 50 :
    print("성적 : C")
else :
    print("성적 : F")




# 문제 3 : if 를 사용해서 오름차순으로 출력하기
n1, n2 = map(int, input("두 개의 정수를 입력하세요 : ").split())

if n1 < n2 :
    print("오름차순 정렬 :", n1, n2)
else :
    print("오름차순 정렬 :", n2, n1)


# 문제 3 심화
n1, n2, n3 = map(int, input("세 개의 정수를 입력하세요 : ").split())

if n1 < n2 :
    if n2 < n3 :
        print("오름차순 정렬 :", n1, n2, n3)
    elif n3 < n1 :
        print("오름차순 정렬 :", n3, n1, n2)
    else :
        print("오름차순 정렬 :", n1, n3, n2)
elif n2 < n1 :
    if n1 < n3 :
        print("오름차순 정렬 :", n2,n1, n3)
    elif n2 > n3 :
        print("오름차순 정렬 :", n3, n2, n1)
    else :
        print("오름차순 정렬 :", n2, n3, n1 )


 
# 문제 4 : 연도를 입력받아 해당 연도가 윤년인지
year = int(input("연도를 입력하세요(윤년) : "))

if year % 400 == 0 :
    print(f"{year} : 윤년")
elif year % 4 == 0 and year % 100 != 0 :
    print(f"{year} : 윤년")
else :
    print(f"{year} : 윤년이 아닙니다")



# 문제 5 : 두 자리의 서로 다른 정수 두 개를 입력받아 각 자리수의 숫자들이 일치하는지 비교하기
num1, num2 = map(int, input("두 자리 정수 두 개를 입력하세요 : ").split())

one1 = num1  % 10
one2 = num2  % 10
ten1 = num1 // 10
ten2 = num2 // 10

if one1 == ten2 and one2 == ten1 :
    print(f"{num1}, {num2} : 두개의 숫자가 일치하고, 자리 값만 다른 정수입니다.")
elif one1 == one2 or ten1 == ten2 :
    print(f"{num1}, {num2} : 하나의 숫자가 일치합니다. (자리 값 같음)")
elif one1 == ten2 or one2 == ten1 :
    print(f"{num1}, {num2} : 하나의 숫자가 일치합니다. (자리 값 다름)")   
else :
    print(f"{num1}, {num2} : 일치하는 숫자가 없습니다.")
print()


# 문제 6 : 양의 정수 하나를 입력받아 이 정수가 2의 배수인지 3의 배수인지? nested if 사용하기
num = int(input("정수를 하나 입력하세요 : "))

if num % 2 == 0 :
    if num % 3 == 0 :
        print(f"{num} : 2와 3으로 나누어 집니다.")
    else :
        print(f"{num} : 2로 나누어 집니다.")
elif num % 3 == 0 :
    print(f"{num} : 3으로 나누어 집니다.")
else :
    print(f"{num} : 어느 것으로도 나누어지지 않습니다.")
print()


# 문제 7 : 연도를 입력받아 해당 연도의 띠를 출력하세요
year = int(input("연도를 입력하세요(띠) : "))
zodiacSign = year % 12

if zodiacSign == 0 :
    print('원숭이')
elif zodiacSign == 1 :
    print('닭')
elif zodiacSign == 2 :
    print('개')
elif zodiacSign == 3 :
    print('돼지')
elif zodiacSign == 4 :
    print('쥐')
elif zodiacSign == 5 :
    print('소')
elif zodiacSign == 6 :
    print('호랑이')
elif zodiacSign == 7 :
    print('토끼')
elif zodiacSign == 8 :
    print('용')
elif zodiacSign == 9 :
    print('뱀')
elif zodiacSign == 10 :
    print('말')
else :
    print('양')
print()

