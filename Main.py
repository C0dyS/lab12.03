class Animals:
    def breathe(self):
        print('breathe')
    def move(self):
        print('move')

class Dogs(Animals):
    pass

class cats(Animals):
    pass

my_dog = Dogs()
my_dog.breathe()



