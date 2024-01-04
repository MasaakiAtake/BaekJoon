traials = int(input())

for i in range(traials):
    _ = input()
    print( len(_[:_.index("D")]) if "D" in _ else len(_) )