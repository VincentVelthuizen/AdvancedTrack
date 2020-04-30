def readposint():
    read_int = -1
    while read_int < 0:
        try:
            read_int = int(input("Please provide a positive integer"))
            if read_int < 0:
                print("The integer should be positive")
        except ValueError:
            print("That is not a valid integer")

    return read_int


if __name__ == "__main__":
    print(readposint())