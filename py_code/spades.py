def spade_print(row_cnt, col_cnt):
    half = list(range(1, int(row_cnt / 2) + 1))
    wirwind = half[:-1] + half[::-1]
    for r in wirwind:
        line = [" " for i in range(col_cnt)]
        mid = col_cnt % 2 == 0 and int(col_cnt / 2) or int(col_cnt/2)+1
        line[mid-r:mid+r] = "+" * r * 2
        print("".join(line))

spade_print(100, 103)
