censor = list("CAMBRIDGE")
ans = ""
for i in input():
    if i not in censor:
        ans += i
print(ans,sep="")