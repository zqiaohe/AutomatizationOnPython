import argparse


def TwiceSum(numbers):
    i = 1
    Sum = 0
    for num in numbers:
        if i % 4 != 0:
            Sum += (num + num)
        elif i % 4 == 0:
            if num != 0:
                Sum /= (num*num)
        i += 1
    return Sum

def Sum(numbers):
    i = 1
    Sum = 0
    for num in numbers:
        if i % 4 != 0:
            Sum += num
        elif i % 4 == 0:
            if num != 0:
                Sum /= num
        i += 1
    return Sum

def main():
    program_description = "Программа суммирования и умножения чисел."

    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument('numbers', type=float, nargs='*',
                        help='Числа, над которыми нужно провести операцию.')
    parser.add_argument('-t', '--twice', action='store_const',
                        const=TwiceSum, default=Sum, dest='process',
                        help='Перемножить числа. Если не указано, то сложить.')
    args = parser.parse_args()
    res = int(args.process(args.numbers))
    print(res)
    return res

main()
