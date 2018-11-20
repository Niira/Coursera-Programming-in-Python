import sys
digit_string = sys.argv[1]

str = digit_string
ans = 0
for c in str:
    ans = ans + int(c)
print(ans)