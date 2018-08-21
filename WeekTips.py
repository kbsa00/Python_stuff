import random as rand

class Weeklybets: 

    ##Private fields
    __myWeeklybets = []
    __weeklyAnswers = []
    __correctAnswers = 0

    def __init__(self):
        print('Welcome to the WeeklyTips')
        self.__myWeeklybets = []
        self.__weeklyAnswers = []
        self.__correctAnswers = 0
        

    def generateYourWeeklyTips(self):
        print('You are now generating your own Weekly bets \n', 
        'Be sure to only write h,b or u.')
        index = 0
        while(len(self.__myWeeklybets) != 5):
            betAnswer = input('Input your answer: ' + str(index+1))
            
            if(betAnswer is 'h' or betAnswer is 'b' or betAnswer is 'u'):
                self.__myWeeklybets.append(betAnswer)
                index +=1
            else:
                print('Invalid input')
        
    def getYourWeeklybets(self): 
        return self.__myWeeklybets

    def getWeeklyAnswers(self):
        return self.__weeklyAnswers

    def printYourWeeklybets(self): 
        print(self.__myWeeklybets)
    
    def generateWeeklyAnswers(self):
        index = 0
        while(index < 5):
            self.__weeklyAnswers.append(rand.choice(['h', 'b', 'u']))
            index += 1

    def checkCorrectAnswers(self):
        
        for x in range(len(self.__weeklyAnswers)):
            if(self.__weeklyAnswers[x] is self.__myWeeklybets):
                self.__correctAnswers += 1


    def getCorrectAnswers(self):
        print(self.__correctAnswers)
