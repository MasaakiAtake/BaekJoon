def exponentiation(N):
    answer = "%.300f" % (1 / pow(2, N))
    
#     answer = "{:.300f}".format((1 / pow(2, N))
    
    slice_idx = len(answer)
    
    for idx in range(len(answer)-1, 1, -1):
        if answer[idx] != '0':
            slice_idx = idx + 1
            break
    
    return answer[:slice_idx]

if __name__ == "__main__":
    N = int(input())
    print(exponentiation(N))