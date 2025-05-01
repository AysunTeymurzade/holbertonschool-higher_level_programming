#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1  # argv[0] proqramın adı olduğuna görə -1
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        print(f"{num_args} arguments:")
        for i in range(1, num_args + 1):
            print(f"{i}: {sys.argv[i]}")
