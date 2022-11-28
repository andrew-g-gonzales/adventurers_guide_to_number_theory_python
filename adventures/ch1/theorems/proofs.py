from adventures import utils

group = utils.make_successive_elem_group
summed = utils.summed
perfect_square = utils.perfect_square
perfect_cb = utils.perfect_cube
prime = utils.is_prime
gen_primes = utils.gen_primes


def square_product_problem(range):
    pass


def generate_twin_primes(primes):
    return [(primes[idx - 1], primes[idx]) for idx in range(1, len(primes)) if (primes[idx] - primes[idx - 1] == 2)]


if __name__ == "__main__":
    result_pd_2 = all(
        [(x * y) % 2 == 0 for (x, y) in group(range(1, 21))]
    )
    print(f"The product of two consecutive integers is always even: {result_pd_2}")

    sq_odd = all(
        [(((elem ** 2) - 1) % 8 == 0) for elem in range(3, 12) if elem % 2 == 1]
    )
    print(f"The square of any odd number is 1 more than some multiple of 8: {sq_odd}")

    result_sq_cube_sum = (
        perfect_square(
            sum(
                [(num ** 3) for num in range(1, 4)]
            )
        )
    )
    print(f"The sum of the first so many cubes is a square: {result_sq_cube_sum}")

    two_sq_cube = all(
        [(not perfect_cb((x ** 3) + (y ** 3))) for (x, y) in group(range(2, 100))]
    )
    print(f"The sum of two cubes is never a cube: {result_sq_cube_sum}")

    twin_primes = generate_twin_primes(gen_primes(1000))
    print(twin_primes)
