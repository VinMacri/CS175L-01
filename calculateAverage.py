#Vincent Macri
#CS 175
#Calculate Average and Grade
import random as r

def main():
    keepGoing = True
    while(keepGoing):
        score = []
        grade = []
        #score = my_random(score)
        score = enter_scores(score)
        avg = calc_average(score)
        grade = determine_grade(score, grade)
        
        print_grade(grade, score)
        keepGoing = repeat()
        
def repeat():
    reask = input("Enter 'yes' or 'y' to enter another input: ")
    if(reask.lower() == "yes" or reask.lower() == 'y'):
        keepGoing = True
    else:
        keepGoing = False
    return keepGoing

def enter_scores(score):
    for x in range(5):
        s = int(input(f'Enter score {x+1}: '))
        score.append(s)
    return score
"""
def my_random(score):
    for x in range(5):
        s = r.randint(1,100)
        score.append(s)
    return score
"""
def calc_average(score):
    avg = (score[0]+score[1]+score[2]+score[3]+score[4])/5
    score.append(avg)
    return avg

def determine_grade(score, grade):
    for x in range(len(score)):
        if(score[x] >= 90):
            g = "A"
            grade.append(g)
        elif(score[x] >= 80 and score[x] <90):
            g = "B"
            grade.append(g)
        elif(score[x] >= 70 and score[x] <80):
            g = "C"
            grade.append(g)
        elif(score[x] >= 60 and score[x] <70):
            g = "D"
            grade.append(g)
        else:
            g = "F"
            grade.append(g)
    return grade

def print_grade(grade, score):
    print()
    print(f'{"Score":<15}',f'{"Numeric Grade":<15}',f'{"Letter Grade":<15}')
    print("---------------------------------------------")
    print(f'{"Score 1:":<15}',f'{score[0]:<15}',f'{grade[0]:<15}')
    print(f'{"Score 2:":<15}',f'{score[1]:<15}',f'{grade[1]:<15}')
    print(f'{"Score 3:":<15}',f'{score[2]:<15}',f'{grade[2]:<15}')
    print(f'{"Score 4:":<15}',f'{score[3]:<15}',f'{grade[3]:<15}')
    print(f'{"Score 5:":<15}',f'{score[4]:<15}',f'{grade[4]:<15}')
    print(f'{"Average Score:":<15}',f'{score[5]:<15}',f'{grade[5]:<15}')

if __name__ == '__main__':
    main()
