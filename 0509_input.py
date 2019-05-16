# 0509
# 자료형 이해하기 & 파이썬 입출력 연습하기

# 자료형 
# 문제 1 : 3.14를 문자열, 정수, 실수로 출력하기
num = 3.14

numTostring = str(num)
floatToint = int(num) 
intTofloat = float(floatToint)

print(numTostring, type(numTostring))
print(floatToint, type(floatToint))
print(intTofloat, type(intTofloat))
print()  # 줄 한 칸 띄기


# 입출력
# 문제 1 : 실수를 입력받아 그 제곱 출력하기
num = float(input("실수를 하나 입력하세요: "))
print("제곱할 숫자는?", num)
print(f"제곱한 수는 {num**2}입니다")
print()


# 문제 2 : 이름과 출생 연도를 입력받고 다음과 같이 출력하세요
name = input("이름: ")
birthYear = int(input("출생연도: "))
#print("당신의 이름은", name, "이며", "당신의 나이는", 2019-birthYear, "살 입니다.")
print(f"당신의 이름은 {name}이며, 당신의 나이는 {2019 - birthYear}살 입니다.\n")



# 문제 3 : 정수 3개를 입력받아 그 합과 평균을 출력하세요
#n1, n2, n3 = input("정수 3개를 입력하세요 : ").split()
#n1 = int(n1)
#n2 = int(n2)
#n3 = int(n3)
n1, n2, n3 = map(int, input("정수 3개를 입력하세요 : ").split())

#print("총합은", n1+n2+n3 )
#print("평균은", float((n1+n2+n3)/3))

print(f"총합은 {n1+n2+n3}" )
print(f"평균은 {float((n1+n2+n3)/3)}\n")

# 소수점 아래 자리수 정해서 출력하기
# %.nf -> 소수점아래 n 자리까지 표시하기
print("평균은 %.1f  (소수점 아래 한자리)" % float((n1+n2+n3)/3))
print("평균은 %.2f (소수점 아래 두 자리)" % float((n1+n2+n3)/3))