"""
Ch. 2, pg. 25 - 25
"""
from adventures import utils

flatten = utils.flatten
odd_nums = utils.odd_seq
summed = utils.summed
average = utils.average


def sum_2_previous(numbers):
    sum_list = []
    for idx in range(0, len(numbers)):
        if idx >= 2:
            sum_list.append(sum(sum_list[-2:]))
        else:
            sum_list.append(numbers[idx])

    return sum_list


def progressive_step_sequence(limit):
    start = 1

    for step in range(start, limit):
        stepped = list(range(start, ((start + step) ** 2), step)[:3])
        start = stepped.pop()
        yield stepped


def progressive_step_jump_twice_as_big(limit):
    start = 1
    step = 1
    for idx in range(start, limit):
        stepped = list(range(start, ((start + step) ** 2), step)[:3])
        start = stepped.pop()
        step = step * 2
        yield stepped


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
        """p. 26
        Again, you may notice that 3 is the sum of the two numbers
             before it, 1 and 2, and that 5 is the sum of 2 and 3.
             According to this pattern, the next number should be 3 + 5 = 8,
             and the one after should be 5 + 8 = 13\n""",
        sum_2_previous(range(1, 8)),
    )

    print("""p. 26
    (c4)    1, 2, 3, 5, 7, 10, 13, 17, 21, etc.
    ...with 2 jumps of 1, two jumps of 3, and so on.
          """, flatten(progressive_step_sequence(6)))

    print("""p. 26
    ...pairs of jumps each twice as big as the previous pair, thus
    (c5)  1, 2, 3, 5, 7, 11, 15, 23, 31, etc. 
        """, flatten(progressive_step_jump_twice_as_big(6)))

    print("1:", (2 * 1) - 1)
    print("2:", (2 * 2) - 1)
    print("3:", (2 * 3) - 1)
    print("41:", (2 * 41) - 1)

    print("ordinal squares:      ", [num ** 2 for num in range(1, 11)])

    odd_seq = odd_nums(22)
    progressive_squares = []
    num = 0
    for idx in range(0, 10):
        num += odd_seq[idx]
        progressive_squares.append(num)

    print("progressive_squares:  ", progressive_squares)

    progressive_squares_2 = [1, 4]
    for idx in range(1, 9):
        progressive_squares_2.append(
            ((progressive_squares_2[-1] + 1) * 2) - progressive_squares_2[-2]
        )

    print("progressive_squares_2:", progressive_squares_2)

    print("""p. 26
             ...the sum of the first n odd numbers is n^2.
             ...note that 1 + 9 = 5 + 5""")
    for num in range(1, 8):
        odds_n = odd_nums(num)
        print(f"{num} sq: {summed(odds_n), num ** 2}")
        print(f"{num} add: {odds_n[-1] + 1, num * 2}\n")

    print("""p. 32
             If we take the first n numbers, the average is 
             0.5 * (n + 1), which means half of n + 1.
             So the sum is n times that, or (0.5 * n) * (n + 1)   
         """)
    for idx in range(1, 5):
        num = 1 + idx
        print(f"{num, int((0.5 * num)*2)}")


if __name__ == "__main__":
    main()
