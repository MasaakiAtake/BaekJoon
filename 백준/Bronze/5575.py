for i in range(3):
    fh, fm, fs, sh, sm, ss = map(int, input().split())
    first = (fh*3600) + (fm*60) + fs
    second = (sh*3600) + (sm*60) + ss
    time = second - first
    h = (time//3600)
    m = (time%3600) // 60
    s = (time%3600) % 60
    print(h, m, s)