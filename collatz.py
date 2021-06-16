def main():
    number = int(input('Starting number: '))
    counter = 0

    while number != 1:
        if number % 2 == 0:
            number /= 2
            print(f'{number}\t', end = '')
        else:
            number = number * 3 + 1
            print(f'{number}\t' , end = '')
        counter+=1
    print(f'\nTermanited after {counter} step.')

if __name__ == '__main__':
    main()
