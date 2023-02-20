#Vincent Macri
#CS 175
#Calculate Average and Grade

def main():
    keepGoing = True
    while(keepGoing):
        score1, score2, score3, score4, score5 = enter_scores()
        avg = calc_average(score1, score2, score3, score4, score5)
        grade1,grade2,grade3,grade4,grade5,avgGrade = determine_all_grades(score1, score2, score3, score4, score5, avg)
        print_grade(grade1,grade2,grade3,grade4,grade5,avg, avgGrade, score1, score2, score3, score4, score5)
        reask = input("Enter 'yes' or 'y' to enter another input: ")
        if(reask.lower() == "yes" or reask.lower() == 'y'):
            keepGoing = True
        else:
            keepGoing = False
        
def enter_scores():
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))
    score4 = int(input("Enter score 4: "))
    score5 = int(input("Enter score 5: "))
    return score1, score2, score3, score4, score5

def calc_average(score1, score2, score3, score4, score5):
    avg = (score1+score2+score3+score4+score5)/5
    return avg

def determine_grade(score):
    if(score >= 90):
        grade = "A"
    elif(score >= 80 and score <90):
        grade = "B"
    elif(score >= 70 and score <80):
        grade = "C"
    elif(score >= 60 and score <70):
        grade = "D"
    else:
        grade = "F"
    return grade

def determine_all_grades(score1, score2, score3, score4, score5, avg):
    grade1=determine_grade(score1)
    grade2=determine_grade(score2)
    grade3=determine_grade(score3)
    grade4=determine_grade(score4)
    grade5=determine_grade(score5)
    avgGrade = determine_grade(avg)
    return grade1,grade2,grade3,grade4,grade5,avgGrade

def print_grade(grade1,grade2,grade3,grade4,grade5, avg,avgGrade, score1, score2, score3, score4, score5):
    print()
    print(f'{"Score":<15}',f'{"Numeric Grade":<15}',f'{"Letter Grade":<15}')
    print("---------------------------------------------")
    print(f'{"Score 1:":<15}',f'{score1:<15}',f'{grade1:<15}')
    print(f'{"Score 2:":<15}',f'{score2:<15}',f'{grade2:<15}')
    print(f'{"Score 3:":<15}',f'{score3:<15}',f'{grade3:<15}')
    print(f'{"Score 4:":<15}',f'{score4:<15}',f'{grade4:<15}')
    print(f'{"Score 5:":<15}',f'{score5:<15}',f'{grade5:<15}')
    print(f'{"Average Score:":<15}',f'{avg:<15}',f'{avgGrade:<15}')

main()
