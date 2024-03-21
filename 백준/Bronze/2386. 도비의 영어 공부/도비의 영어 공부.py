while True:
    li = input()
    if li == "#":
        break
    val = li[0]
    data = li[2::]
    result = data.count(val) + data.count(val.upper())
    print(val, result)