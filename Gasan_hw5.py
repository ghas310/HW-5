class animal:
    def __init__(self, name):
        self.name = name

    def guesswhoami(self):
        x = 1
        for hint in (Dic[self.name]):
            print ("Hint "+str(x)+". "+hint)
            answer = input ("Who am I?:")
            if answer == self.name:
                print ("you win! Im " +self.name)
                break
            else:
                print (" Try again! ")
                x +=1
            if x > 3:
                print ("you lose! The answer is "+self.name)
            
print ("Weclome to my game")
print ("I will provide you there name of animals and you you have to guess it")
Dic = {"tiger":["I am the biggest cat", "I come in black and white or orange and black", "I am a carnivore"],"elephant":["I have exceptional memory", "I am the largest land-living mammal in the world","I have a trunk"],
"bat":["I use echo-location", "I can fly", "I see well in dark"]}
t = animal("tiger")
e = animal("elephant")
b = animal("bat")


t.guesswhoami()
e.guesswhoami()
b.guesswhoami()
