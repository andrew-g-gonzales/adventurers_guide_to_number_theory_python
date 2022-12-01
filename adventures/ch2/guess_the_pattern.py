"""
Ch. 2, pg. 25 - 25
"""


def sum_2_previous(numbers):
    sum_list = []
    for idx in range(0, len(numbers)):
        if idx >= 2:
            sum_list.append(sum(sum_list[-2:]))
        else:
            sum_list.append(numbers[idx])

    return sum_list


def main():
    print(
        "Odd numbers via sequence of each number is 2 more than the one before it",
        [num for num in range(1, 17, 2)],
    )

    print(list(map(lambda x: x + 1 if x % 2 == 1 else x - 1, range(1, 10))))

    print(
        "A list of all numbers leaving out every fourth one",
        [num for idx, num in enumerate(range(1, 18)) if not (idx + 1) % 4 == 0],
    )

    print(
        """Again, you may notice that 3 is the sum of the two numbers
             before it, 1 and 2, and that 5 is the sum of 2 and 3.
             According to this pattern, the next number should be 3 + 5 = 8,
             and the one after should be 5 + 8 = 13\n""",
        sum_2_previous(range(1, 8)),
    )


if __name__ == "__main__":
    main()
