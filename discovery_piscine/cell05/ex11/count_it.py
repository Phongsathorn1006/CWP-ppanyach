import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return

    print(f"parameters: {len(sys.argv) - 1}")

    for param in sys.argv[1:]:
        print(f"{param}: {len(param)}")

if __name__ == "__main__":
    main()