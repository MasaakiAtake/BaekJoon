text = input()
split_str = [text[x:x+10] for x in range(0, len(text), 10)]
print(*split_str)