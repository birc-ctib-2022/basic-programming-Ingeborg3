
# Print the pattern

for ln in range(2, 7):
    for n in range(1, ln):
        if n == ln-1:
            print('*')
        else:
            print('*', end=' ')

for ln in range(5, 0, -1):
    for n in range(1, ln): 
        if n==ln-1:
            print('*')
        else:
            print('*', end=' ')
