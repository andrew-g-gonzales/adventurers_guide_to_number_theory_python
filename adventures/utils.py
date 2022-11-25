def reduce(operation, nums, initializer):
    value = initializer
    for elem in nums:
        value = operation(value, elem)
    return value


def make_successive_elem_group(elems, grouped=2):
    return [elems[index:index + grouped] for index in range(0, len(elems) - 1)]


def operate_pairs(elems, operation=lambda unused: True):
    (first, second) = elems
    return operation(first, second)


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
