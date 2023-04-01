my_dict = {}

while True:
    try:
        key_and_value = input('key and value: ')
    except EOFError:
        break

    key, value = key_and_value.split()
    my_dict[key] = value

print(my_dict)