n = int(input())

for _ in range(n):
    nn = int(input())
    prices = list(map(int,input().split()))
    max_price = 0
    answer = 0
    for i in range(len(prices)-1, -1, -1):
        if max_price < prices[i]:
            max_price = prices[i]
        elif max_price > prices[i]:
            answer += (max_price - prices[i])
    print(answer)