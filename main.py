def main():
    
    total = 0
    
    #for loop runs through 5 times
    for i in range(5):
        new_num = int(input('Please enter a number: '))
        total += new_num
        
    print(f'Your total is: {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return total


if __name__ == '__main__':
    main()
