n, s = input().split()
nicks = []
chats = []
isNick = False
for i in range(int(n)):
    nick, chat = input().split()
    if isNick:
        continue
    if nick == s:
        isNick = True
    nicks.append(nick)
    chats.append(chat)
answer = chats[nicks.index(s)]
ans = 0
for i in chats:
    if i == answer:
        ans += 1
print(ans-1)