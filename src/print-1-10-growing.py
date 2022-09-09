
# Print the numbers described in the exercise

for ln in range(2, 12):
    for n in range(1, ln): 
        if n == ln-1:
            print(n, end='\n')
        else: 
            print(n, end=' ')
