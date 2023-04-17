#Vincent Macri
#CS 175
#Expense Pie Chart

import matplotlib.pyplot as plt

def main():
    expenses, labels = readFile()
    drawChart(expenses, labels)
    
def readFile():
    expenses = []
    labels = []
    try:
        infile = open('expenses.txt','r')
        for line in infile:
            try:
                line = line.rstrip("\n")
                line = line.split("\t")
                expense = int(line[1])
                label = line[0]
                labels.append(str(label))
                expenses.append(expense)
            except:
                print(f'Error converting "{line[1]}" to an integer.')
    except IOError:
        print("There was an error opening the file.")
    
    return expenses, labels

def drawChart(expenses, labels):
    plt.pie(expenses, labels=labels)
    plt.title('Expenses')
    plt.show()
    
if __name__ == '__main__':
    main()
