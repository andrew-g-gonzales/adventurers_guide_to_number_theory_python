def make_successive_elem_group(elems, grouped=2):
    return [elems[index:index + grouped] for index in range(0, len(elems) - 1)]


def operate_pairs(elems, initial_elem, operation=lambda unused: True):
    acc = initial_elem
    for (first, second) in make_successive_elem_group(elems):
        acc = operation(first, second)
    return acc


def reduce(elems, initial_elem, operation=lambda unused: True):
    acc = initial_elem
    for elem in elems:
        acc = operation(acc, elem)
    return acc


def summed(nums):
    return reduce(nums, 1, lambda x, y: x + y)


def product(nums):
    return reduce(nums, 1, lambda x, y: x * y)


def pow_exp(num, power):
    return num ** power


def squared(num):
    return pow_exp(num, 2)


def cube(num):
    return pow_exp(num, 3)


def square_rt(num):
    return int(num ** (1 / 2))


def perfect_square(num):
    return (int(square_rt(num) + 0.5)) ** 2 == num


def filtered(elems, condition=lambda unused: True):
    return [elem for elem in elems if (condition(elem))]


if __name__ == "__main__":
    print(pow_exp(3, 3))
