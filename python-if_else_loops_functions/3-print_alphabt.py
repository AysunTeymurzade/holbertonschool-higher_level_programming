#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 101 and chr(i) != 113:
        print("{}".format(chr(i)), end="")
