import numpy as np

class Game :
    def __init__(self,case,mise):


        """ SETTINGS BASE GAME"""
        self.case = case
        self.redNumber = list()
        self.blackNumber = list()
        self.greenNumber = list()


        """ GAME HISTORIC """
        self.historicPlayer = list()
        self.historicGame = list()
        self.step = 0
        self.gain = 0
        self.loss = 0

        """ FILL LIST """

        self.greenNumber.append(str(0))
        for number in range(1,11) :
            # impair number
            if number % 2 != 0 :
                self.redNumber.append(str(number))
            else : 
                self.blackNumber.append(str(number))
        for number in range(11,19):
            if number % 2 != 0 :
                self.blackNumber.append(str(number))
            else:
                self.redNumber.append(str(number))

        for number in range(19,29):
            if number % 2 != 0 :
                self.redNumber.append(str(number))
            else:
                self.blackNumber.append(str(number))
        
        for number in range(29,37):
            if number % 2 != 0 :
                self.blackNumber.append(str(number))
            else:
                self.redNumber.append(str(number))

    

    def randSample(self):
        rand = np.random.randint(self.case+1, size=1)
        print("Random sample process... Fall on: "+str(rand[0]))
        self.historicGame.append(rand[0])
        return str(rand[0])
        

    def checkColor(self,number):
        if str(number) in self.redNumber :
            print(str(number) + " is red")
        if str(number) in self.blackNumber :
            print(str(number) + " is black")
        if str(number) in self.greenNumber :
            print(str(number) + " is green")

    


    def showGame(self):
        print("Number of case in game: "+str(self.case))
        print("Red number :")
        print(*self.redNumber)
        print("Black number :")
        print(*self.blackNumber)
        print("Green number :")
        print(*self.greenNumber)

    

        






jeu = Game(37,2)
jeu.showGame()
jeu.checkColor(jeu.randSample())