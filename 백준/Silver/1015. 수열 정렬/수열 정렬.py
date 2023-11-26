import sys
import math

a_size = int(sys.stdin.readline())
a = sys.stdin.readline().replace("\n", "").split(" ")
a = [int(i) for i in a]

sorted_a = [i for i in a]
sorted_a.sort()

p = []

for i in a:
    p.append(sorted_a.index(i))
    sorted_a[sorted_a.index(i)] = -1

result = [i for i in p]

for result in result:
    sys.stdout.write(str(result)+" ")