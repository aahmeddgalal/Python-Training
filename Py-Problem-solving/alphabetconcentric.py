n = 4
for i in range(2*n -1):
    for j in range(2*n -1):
        print(chr(64+max(abs(i-n+1), abs(j-n+1))+1), end = ' ')
    print()
# I stole the code from bluesky, still learning it