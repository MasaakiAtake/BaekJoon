on = []
people = 0

for _ in range(10):
    a, b = map(int, input().split())
    people += b
    people -= a
    on.append(people)

print(max(on))