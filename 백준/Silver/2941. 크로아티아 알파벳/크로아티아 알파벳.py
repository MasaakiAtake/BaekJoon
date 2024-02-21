cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
user = input()

for i in cro:
    user = user.replace(i, '*')
print(len(user))