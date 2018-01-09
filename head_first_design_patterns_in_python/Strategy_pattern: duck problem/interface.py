class Duck:
    def __init__(self, func_quack, func_fly):
        self.quack_behavior = func_quack()
        self.fly_behavior = func_fly()

    def set_quack_behavior(self, func_quack):
        self.quack_behavior = func_quack()

    def set_fly_behavior(self, func_fly):
        self.fly_behavior = func_fly()

    def swim(self):
        print('I can swim')

    def display(self):
        pass


def quack():
    print('Quack!!!')


class squeak():
    def __call__(self):
        print('Squaek!!')


class fly_with_wings():
    def __call__(self):
        print('I am flying!!')


class no_fly:
    def __call__(self):
        print("Can't fly")


class MallardDuck(Duck):
    def display(self):
        print('Looks like a mallard duck')


class RedHeadDuck(Duck):
    def display(self):
        print('Looks like a redhead duck')


class RubberDuck(Duck):
    def display(self):
        print('Looks like a rubber duck')


mallard = MallardDuck(quack, fly_with_wings)
# redhead = RedHeadDuck(Quack, FlyWithWings)
# rubberduck = RubberDuck(Squeak, NoFly)
#
# mallard.quack_behavior()
# mallard.fly_behavior()
# mallard.display()
# print('----mallard lost his wings T.T ------')
# mallard.set_fly_behavior(NoFly)
# mallard.fly_behavior()
# print('-----------------')
#
#
# redhead.quack_behavior()
# redhead.fly_behavior()
# redhead.display()
#
# rubberduck.quack_behavior()
# rubberduck.fly_behavior()
# rubberduck.display()
