#Vincent Macri
#CS 175
#World Series

def main():
    run = True
    while run:
        worldSeriesWinners = readList()
        searchList(worldSeriesWinners)
        ask = input("Enter 'quit' or 'q' if you would like to quit: ")
        if ask.lower() == 'quit' or ask.lower() == 'q':
            run = False

def readList():
    worldSeriesWinners = []
    worldSeries = open('WorldSeriesWinners.txt','r')
    for team in worldSeries:
        team = team.rstrip('\n')
        worldSeriesWinners.append(team)
    return worldSeriesWinners

def searchList(worldSeriesWinners):
    searchTeam = input("Enter the name of a team: ")
    sublist = [team for team in worldSeriesWinners if searchTeam.lower() == team.lower()] # or " " + searchTeam.lower() + " " in team.lower()]
    if(len(sublist)==0):
        print("No results found.")
    else:
        print("The", searchTeam, "won the World Series", len(sublist), "times between 1903 and 2009.")
    
if __name__ == '__main__':
    main()
