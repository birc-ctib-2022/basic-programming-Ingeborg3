import sys

# This program should take two arguments, a command--either "encode" or "decode"--
# and then a string.

if len(sys.argv) != 3:
    print("Incorrect number of arguments.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} command string\n", file=sys.stderr)
    # Usage: tells which arguments the program given by sys.argv[0]
    # requires. 
    sys.exit(1) # ?

# sys.argv = [filename, encode or decode, string]
# sys.argv[1] = encode or decode. As strings?
# sys.argv[2] = string. 

command, x = sys.argv[1:3]  

match command: 
    case "encode":
        # Implement the encoding here
        encoding = ""
        y = []
        for c in x:
            y.append(hex(ord(c)))
            encoding = ''.join(y)
        print(encoding)

    case "decode":
        # Implement the decoding here
        decoding = ""
        y = x.split('0x')
        y = y[1:]
        for c in y: # c is a python string with a number.
            decoding += chr(int(c, base=16))
        print(decoding)
