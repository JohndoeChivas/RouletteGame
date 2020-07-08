import Settings
import time 
import numpy as np

class Generator :
    """ Generator is a class for generate sample of value which are determine in Settings.py. Each values have a probability associated """
    def __init__(self):
        self.sample = None
        self.multimonial = None
        self.size = None

        self.repeatParam = None

        
        self.elapsedTime = None
        
        self.dict = Settings.repeatSequency
        

    def showSample(self):
        """ Show result of sample of numpy module """
        print("Sample generated: ")
        print(self.sample)
        print()

    def showMultimonial(self):
        """ Show result of multimonial numpy module """
        print(self.multimonial)

    def showSequency(self):
        """ Show result of repeating sequency for each N values """
        print("Sample lenght is "+str(self.size))
        print("Observable repeating number start from "+str(self.repeatParam))
        print()
        print("Sequency repeated consecutively for "+str(Settings.N0)+": ")
        print(self.dict[str(Settings.N0)])
        print()
        print("Sequency repeated consecutively for "+str(Settings.N1)+": ")
        print(self.dict[str(Settings.N1)])
        print()
        print("Sequency repeated consecutively for "+str(Settings.N2)+": ")
        print(self.dict[str(Settings.N2)])
        print()

    
    
    
    def multinomialSample(self,n):
        """ Count the number of time each N appear in multinomial sample """
        self.multimonial = np.random.multinomial(n,[Settings.P0,Settings.P1,Settings.P2])
        return self.multimonial

    def generator(self,n):
        """ Generate sample with N0,N1,N2 (0,1,2) values with probabilities P0,P1,P2 associated  """
        self.size = n
        self.sample = np.random.choice([Settings.N0,Settings.N1,Settings.N2], n ,p=[Settings.P0,Settings.P1,Settings.P2]) 
        return self.sample


    def scanSequency(self,repeater):
        """ Scan the number of succeeding for each N values in sample """
        repeatDigit = 1
        temp = self.sample[0]
        for n in self.sample[1:] :
            #print("n:"+str(n)+" and temp: "+str(temp))
            if temp == n :
                repeatDigit += 1
            else :
                if repeatDigit >= repeater :
                    self.dict[str(temp)].append(repeatDigit)
                repeatDigit = 1
                temp = n
        

    def timeElapsed(self,start,end):
        """ Return time elapsed during period """
        self.elapsedTime = end - start 
        return self.elapsedTime

    def resume(self):
        """ Resume of generator sample """
        self.showSample()
        self.showSequency()
        print("Time elapsed: "+str(self.elapsedTime)+" seconds.")


    def run(self,n,repeatDigits=2):
        """ Main function for run """
        print("####### BEGIN PROGRAM #######")
        print()
        self.repeatParam = repeatDigits
        start = time.time()
        self.generator(n)
        self.scanSequency(repeatDigits)
        end = time.time()
        self.timeElapsed(start,end)
        self.resume()
        print()
        print("####### END PROGRAM #######")
        print()


    
        



