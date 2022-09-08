import sys

if len(sys.argv) != 2:
    print(f"{sys.argv[0]} expected exactly one argument.")
    sys.exit(1)

password = sys.argv[1]
is_valid = False
# Do all the requirement checks here.

cond1, cond2, cond3, cond4, cond5, cond6 = False, False, False, False, False, False
for c in password:
    if c.isupper(): # Only returns True if all letters in the 
        # argument string are uppercase. Non-letters are ignored.
        cond1 = True # Condition true if at least one of the characters
        # are uppercase. 
for c in password:
    if c.islower():
        cond2 = True
for c in password:
    if c.isnumeric():
        cond3 = True
for c in password:
    if c in '$#@':
        cond4 = True
if len(password) >= 6:
    cond5 = True
if len(password) <= 16:
    cond6 = True

if cond1 == True & cond2 == True & cond3 == True & cond4 == True & cond5 == \
    True & cond6 == True:
    is_valid = True
print(is_valid)
