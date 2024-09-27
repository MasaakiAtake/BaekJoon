# readline을 사용하기 위해 import합니다.
from sys import stdin


# 키보드에 있는 자판들을 저장하는 변수를 선언합니다.
keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./"

# 모든 줄을 읽기 위해 계속 반복합니다.
while True:
    # 한 줄을 입력합니다.
    # 숫자, 공백, 알파벳 대문자, 문장 부호로 이루어져 있습니다.
    # Q, A, Z, `(back-quote), 단어로 이루어진 키는 제외입니다.
    # 맨 끝의 \n은 떼어줍니다.
    sentence = stdin.readline().rstrip()

    # 아무런 입력이 없는 줄이라면
    if sentence == '':
        # 반복문을 탈출합니다.
        break

    # 입력한 줄의 길이를 저장하는 변수를 선언합니다.
    sentence_len = len(sentence)
    # 오류를 고친 결과를 저장할 변수를 선언합니다.
    result = ''

    # 입력한 줄의 한 글자씩 반복해봅니다.
    for idx in range(sentence_len):
        # 현재 글자가 공백이 아니라면
        if sentence[idx] != ' ':
            # 현재 글자 값의 keyboard에서의 인덱스를 저장하는 변수를 선언합니다. 
            keyboard_idx = keyboard.index(sentence[idx])

            # keyboard에서 keyboard_idx의 바로 뒤에 있는 글자를 result에 넣어줍니다. 
            result += keyboard[keyboard_idx - 1]
        # 현재 글자가 공백이라면
        else:
            # 공백을 result에 넣어줍니다.
            result += ' '
    
    # 오류를 고친 결과를 출력합니다.
    print(result)