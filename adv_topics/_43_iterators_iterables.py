class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current_value = self.value
        self.value += 1
        return current_value


def my_range(start, end):
    current_value = start
    while current_value < end:
        yield current_value
        current_value += 1


def main():
    # num = MyRange(1, 10)
    # print(next(num))
    # print(next(num))
    # print(next(num))
    # print(next(num))
    # print(next(num))
    # print(next(num))

    nums = my_range(1, 10)
    print(next(nums))
    print(next(nums))
    print(next(nums))


if __name__ == "__main__":
    main()
