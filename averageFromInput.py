#Vincent Macri
#CS175L
#averageFromInput

def main():
    try:
        total, count = sumNumbers()
        averageNumbers(total, count)
    except IOError:
        print("The file could not be opened.")
    except ValueError:
        print("Unexpected data. Please only input numbers.")
    except:
        print("An error occured when trying to execute the program.")
    
    
def sumNumbers():
    infile = open('numbers.txt', 'r')
    total = 0
    count = 1
    for line in infile:
        number = float(line)
        total += number
        print(f'I read in {count} number(s)')
        print(f'Current number is: {number:.2f}')
        print(f'Total is: {total:.2f}')
        print()
        count+=1
    return total, count

def averageNumbers(total, count):
    average = total/(count-1)
    print(f'Average: {average:.2f}')
    
if __name__ == '__main__':
    main()
