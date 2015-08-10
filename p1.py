import sys
for lines in sys.stdin:
    if int(lines) == 42:
        break
    else:
        print(lines)