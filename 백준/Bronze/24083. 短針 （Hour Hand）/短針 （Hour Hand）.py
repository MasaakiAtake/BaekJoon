A = int(input())  # Aの入力
B = int(input())  # Bの入力

# 目盛りの計算
new_position = (A + B) % 12

# 0の場合は12にする
if new_position == 0:
    new_position = 12

print(new_position)