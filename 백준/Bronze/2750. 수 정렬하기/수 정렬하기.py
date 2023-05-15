# 数の個数を入力
N = int(input())

# 数列をリストとして受け取る
numbers = []
for _ in range(N):
    num = int(input())
    numbers.append(num)

# 数列を昇順にソート
sorted_numbers = sorted(numbers)

# 結果を出力
for num in sorted_numbers:
    print(num)