# Start here to make sure condo works

# Helper functions
def string(x, y):
    num = 3
    if x > y:
        num = num + 1
        print(num)
        return True
    else:
        return False


# Main


def main():
    answer = string(4, 6)
    other_answer = string(1000, 543.5)
    print(answer)
    print(other_answer)


if __name__ == '__main__':
    main()
