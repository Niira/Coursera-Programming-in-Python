import sys
num_steps = int(sys.argv[1])

n = num_steps
for i in range(n):
    print(" "*(n-i-1) + "#"*(i+1))