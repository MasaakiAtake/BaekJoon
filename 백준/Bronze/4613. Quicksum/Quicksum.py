alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string = input()

while string != '#':
    result = 0
    for i in range(len(string)):
        result += alphabet.index(string[i]) * (i+1)
    print(result)
    string = input()