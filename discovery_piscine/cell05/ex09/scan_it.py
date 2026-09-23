import sys
import re

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    target_string = sys.argv[2]

    matches = re.findall(keyword, target_string)

    if not matches:
        print("none")
    else:
        print(len(matches))

if __name__ == "__main__":
    main()