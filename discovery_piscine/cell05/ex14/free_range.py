import sys

def main():
    if len(sys.argv) != 3:
        print("none")
        return

    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
    except ValueError:
        print("none")
        return

    step = 1 if start <= end else -1
    result = list(range(start, end + step, step))
    
    print(result)

if __name__ == "__main__":
    main()