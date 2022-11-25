from adventures import utils

group = utils.make_successive_elem_group
pair = utils.operate_pairs
cube = utils.cube
summed = utils.summed
perfect_square = utils.perfect_square
filtered = utils.filtered
sq = utils.squared


if __name__ == "__main__":
    result_pd_2 = all(
        [pair(grp, lambda x, y: x * y) % 2 == 0 for grp in group(range(1, 21))]
    )
    print(f"The product of two consecutive integers is always even: {result_pd_2}")

    sq_odd = all(
        [((sq(elem)-1) % 8 == 0) for elem in range(3, 12) if elem % 2 == 1]
    )
    print(f"The square of any odd number is 1 more than some multiple of 8: {sq_odd}")

    result_sq_cube_sum = (
        perfect_square(
            sum(
                [cube(num) for num in range(1, 4)]
            )
        )
    )
    print(f"The sum of the first so many cubes is a square: {result_sq_cube_sum}")
