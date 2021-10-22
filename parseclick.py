import click
@click.command('numbers')
@click.option('-t', '--twice', is_flag=True, default=False)
@click.argument('numbers', type=float, nargs=-1)

def function_with_click(numbers, twice):
    i = 1
    Sum = 0
    for num in numbers:
        #print('step ' + str(i))
        #print(i)
        #print(i%4)
        if i % 4 != 0 and twice:
            Sum += (num + num)
        elif i % 4 == 0 and twice:
            if num != 0:
                Sum /= (num*num)
        elif i % 4 != 0 and not twice:
            Sum += num
        elif i % 4 == 0 and not twice:
            if num != 0:
                Sum /= num
        i += 1
    return int(Sum)

def main():
    output = function_with_click.main(standalone_mode=False)
    print(int(output))
    return int(output)

main()