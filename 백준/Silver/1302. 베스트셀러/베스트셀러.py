import sys
from collections import defaultdict
input = sys.stdin.readline

books = defaultdict(int)
name_list = []
n = int(input())

for _ in range(n):
    book = input().rstrip()
    books[book] += 1

max_num = max(books.values())

for book in books:
    if books[book] == max_num:
        name_list.append(book)

name_list.sort()
print(name_list[0])