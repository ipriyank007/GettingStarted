import sys

# print(sys.copyright)
# print(dir(sys))
# print(sys.getrecursionlimit())
# print(sys.platform)
# print(sys.getwindowsversion())
sys.stderr.write("This is an error!\n")
sys.stdout.write("This is a standard text\n")
sys.stdin.readlines()

print(sys.argv)