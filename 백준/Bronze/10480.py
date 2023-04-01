N = int(input())
for i in range(N):
    inn = int(input())
    if inn%2 == 0:
        print(str(inn) + " is even")
    if inn%2 != 0:
        print(str(inn) + " is odd")