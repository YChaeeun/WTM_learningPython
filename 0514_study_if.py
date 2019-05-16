

## 풀고싶은 문제의 번호를 입력하면 해당 문제만 실행됩니다!
# 숫자 이외의 값들을 입력하면 종료


while True :
    
    try :
        print("\n=================================================")
        a = int(input("풀고싶은 문제 번호를 입력하세요 : "))
        print("=================================================\n")
    except :
        print("끝")
        break
    

# 문제 1
    if a == 1 :

        try : 
            num = int(input("정수를 입력하세요 : "))
        except:
            print("잘못된 입력입니다.")
            continue

        if num >= 10 :
            print(f"정수 {num}은 10 이상입니다.")
        else :
            print(f"정수 {num}은 10 이상이 아닙니다.")
        print()

# 문제 2
    elif a == 2 :
        num = int(input("(자리수 판별) 정수를 입력하세요 : "))
        num = abs(num) # 만약 음수일 때
        
        if num // 100 > 0 :
            print("세 자리 이상입니다")
        elif num // 10 :
            print("두 자리 숫자입니다.")
        else :
            print("한 자리 숫자입니다")

    elif a == 21 :
        num = int(input("(자리수 판별) 정수를 입력하세요 : "))
        #a = len([str(i) for i in str(num)])
        a = len(str(num))
        if a >= 3 :
            print("세자리")
        elif a == 2 :
            print("두자리")
        else :
            print("한자리")

# 문제 3
    elif a == 3 :
        string = input("(a가 포함?) 문자열을 입력하세요 : ")
        if 'a' in string :
            print('a가 포함되어 있습니다')
        else :
            print('a가 포함되어 있지 않습니다.')
        print()


# 문제 4
    elif a == 4 :
        pass1 = input("패스워드를 설정하세요 1 : ")
        pass2 = input("패스워드를 설정하세요 2 : ")
        if pass1 == pass2 :
            print("\n패스워드가 일치합니다.")
        else:
            print("\n일치하지 않습니다.")

# 문제 5
    elif a == 5 :
        # 가위 0 바위 1 보 2
        alice = input("Alice (가위0 바위1 보2) : ")
        bob = input("Bob (가위0 바위1 보2) : ")

        if int(alice) > 3 or int(bob) > 3 or int(alice) <0 or int(bob) <0 :
            print("잘못된 입력입니다.")
            continue

        if alice == bob :
            print("draw")
        else :
            if alice == '0' :
                if bob == '1' :
                    print("bob win")
                else :
                    print("alice win")
            elif alice == '1' :
                if bob == '0' :
                    print("alice win")
                else :
                    print('bob win')
            else :
                if bob == '0' :
                    print("bob win")
                else :
                    print("alice win")