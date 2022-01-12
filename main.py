import sys

args = sys.argv
if len(args) < 2:
    print("Please specify first argument.")
    sys.exit()
words = args[1]
print(f"Hello, {words}!")