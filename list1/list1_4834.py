# swea - 숫자카드 - D2

T = int(input())

for i in range(T):
    N = int(input())
    card = input()
    
    lst = [0] * 10              #리스트 초기화시켜주기
    for index in range(N):
        lst[int(card[index])] += 1  #입력받은 카드 번호의 값 하나씩 더해주기
    # lst = [index for index in ]
    many_card = [0, 0]               #가장 많은 수 찾기
    for num in range(10):
        if many_card[1] <= lst[num]:    #count()라는 함수로 리스트 안에 어떤 값이 몇 개있는지 알 수 있음
            many_card[0] = num          #예를 들어 lst = [1,2,3,2,3,3] 이면 lst.count(3) = 3
            many_card[1] = lst[num]
    print(f'#{i+1}', many_card[0], many_card[1])