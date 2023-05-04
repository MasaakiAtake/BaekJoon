origin = int(input())
num = origin
cun = 0

while True:
    cun += 1
    cul_num = (num//10) + (num%10)
    new_num = ((num % 10) * 10) + (cul_num % 10)
    
    if new_num == origin:
        break
    num = new_num
print(cun)
