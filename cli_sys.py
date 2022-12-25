import sys
from getpass import getpass

if __name__ == "__main__":
    try:
        # print(sys.argv)
        name = sys.argv[1]
    except:
        name = input("Enter Your Name:\n")
    pw = getpass("Enter ur password:\n")
    print(name, pw)
