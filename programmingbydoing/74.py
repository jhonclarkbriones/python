def main():
    number = int(input('Number: '))
    
    sum = 0
    
    print()
    
    for number in range(1, number+1):
        sum += number
        print(number, end = ' ')

    print(f'\nThe sum is {sum}')

if __name__ == '__main__':
     main()
