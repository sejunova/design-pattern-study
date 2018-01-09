'''
The objective is to make various duck-type objects by inheriting Duck class.
(including flying feature!!!)
See what happens and how to solve the problems with other approaches.
'''


class Duck:
    def quack(self):
        print('Quack!!!!!!!!')

    def swim(self):
        print('I can swim')

    def display(self):
        pass

    def fly(self):
        print('I can fly!!!!!')


class MallardDuck(Duck):
    def display(self):
        print('Looks like a mallard duck')


class RedHeadDuck(Duck):
    def display(self):
        print('Looks like a redhead duck')

class RubberDuck(Duck):
    def quack(self):
        print('squeak!!!')

    def fly(self):
        pass

    def display(self):
        print('Looks like a rubber duck')


mallard = MallardDuck()
redhead = RedHeadDuck()
rubberduck = RubberDuck()

mallard.quack()
mallard.display()
redhead.quack()
redhead.display()

rubberduck.quack()
rubberduck.fly()

# rubberducks which was supposed not to fly are flying around!

