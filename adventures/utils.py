def reduce(operation, nums, initializer):
    value = initializer
    for elem in nums:
        value = operation(value, elem)
    return value


def make_successive_elem_group(elems, grouped=2):
    return [elems[index:index + grouped] for index in range(0, len(elems) - 1)]


def summed(nums):
    return reduce(lambda x, y: x + y, nums, 1)


def product(nums):
    return reduce(lambda x, y: x * y, nums, 1)


def pow_exp(num, power):
    return num ** power


def square_rt(num):
    return int(num ** (1 / 2))


def perfect_square(num):
    return (int(square_rt(num) + 0.5)) ** 2 == num


def perfect_cube(num):
    return round(abs(num) ** (1 / 3)) ** 3 == num


def is_prime(num):
    return False if num < 2 else all([num % x != 0 for x in range(2, num)])


def gen_primes(num):
    return list([x for x in range(2, num) if is_prime(x)])


