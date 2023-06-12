# 入力を取得
N, A, B = map(int, input().split())
S = input()

# 文字列の一部を逆順にする
reversed_str = S[A-1:B]
reversed_str = reversed_str[::-1]

# 元の文字列と逆順にした文字列を結合する
result_str = S[:A-1] + reversed_str + S[B:]

# 出力する
print(result_str)