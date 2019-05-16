# 0514
# IF 조건문 문제 (easy)


# 문제 1 : 가격과 쿠폰을 입력받아 할인한 가격을 출력하세요
price = int(input("가격을 입력하세요 : "))
coupon = input("쿠폰을 입력하세요 : ")

if coupon == "cash300" :
    print(f"할인된 가격은 {price-300}")
elif coupon == "cash500" :
    print(f"할인된 가격은 {price-500}")
else :
    print("잘못된 입력입니다.")



# 문제 2 : 세 과목의 평균을 구하고 합격 불합격을 출력하세요
s1, s2, s3 = map(int, input("세 과목의 성적을 입력하세요 : ").split())
avg = (s1+s2+s3)/3

if avg >= 50 :
    print("합격!")
else :
    print("불합격!")