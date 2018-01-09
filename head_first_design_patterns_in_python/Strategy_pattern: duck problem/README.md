# Strategy Pattern: 오리 문제로 알아보자

#### 과제: 날 수 있는 오리, 다양한 소리를 내는 오리 등을 코드 재사용성을 고려해서 짜보자

---

1. 가장 간단한 생각 : 메소드 오버라이드 하기

   ```python
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
   ```

   > Duck 클래스를 비대하게 만들고 상속을 시켰더니 오히려 SubClass에서 조정해야 할 것들이 너무 많아진다. 
   >
   > RubberDuck은 quack을 가지면 안되기 때문에 squeak라는 소리를 내도록 quack method를 override 하였고, 날 수 없는 오리이기 때문에 fly method도 아무 역할을 하지 않게 할 수밖에 없었다.

   ​

   #### 문제 해결을 위한 단서

   > 디자인 원칙
   >
   > 1. 항상 같아야 하는 부분을 그렇지 않은 부분과 구분시켜라
   > 2. 즉, 가변하는 부분은 떼내서 추상화시켜서 가변하지 않는 부분에 영향을 주지 않도록 하라

   위의 예에서 display, swim 메소드는 변하지 않는 부분이고, fly, quack은 오리마다 변할 수 있는 부분임에 유의한다

2. Interface를 만든다

   1. > Flexible하게 만들면 좋다. 예를 들어 MallardDuck의 객체를 생성하면서 그 객체의 행동 타입을 runtime으로 조절할 수 있도록 하자. Interface를 사용해서 문제를 해결할 수 있는데, 이 방식의 장점은 위의 예처럼 implentation이 클래스에 종속되지 않아도 된다는 점이다.

   위의 사항에 주의하면서 파이썬 클래스를 구현해보았다. 자바와 다른 점은 자바는 Interface 클래스를 제공해주는데 파이썬은 그렇게 할 필요가 없을뿐더러, 단순히 구현부만 제공해주는 클래스를 만들기 때문에 매직메소드를 사용하였다.

   ```python
   class Duck:
       def __init__(self, cls_quack, cls_fly):
           #생성자를 통해 어떠한 행동을 할 것인지 설정할 수 있다.
           self.quack_behavior = cls_quack()
           self.fly_behavior = cls_fly()
       #아래의 set 메소드로 동작변경도 자유로이 가능하다.
       def set_quack_behavior(self, cls_quack):
           self.quack_behavior = cls_quack()

       def set_fly_behavior(self, cls_fly):
           self.fly_behavior = cls_fly()

       def swim(self):
           print('I can swim')

       def display(self):
           pass


   class Quack:
       def __call__(self):
           print('Quack!!!')


   class Squeak:
       def __call__(self):
           print('Squaek!!')


   class FlyWithWings:
       def __call__(self):
           print('I am flying!!')


   class NoFly:
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
           
   # 실행 부분
   mallard = MallardDuck(Quack, FlyWithWings)
   redhead = RedHeadDuck(Quack, FlyWithWings)
   rubberduck = RubberDuck(Squeak, NoFly)

   mallard.quack_behavior()
   mallard.fly_behavior()
   mallard.display()
   print('----mallard lost his wings T.T ------')
   mallard.set_fly_behavior(NoFly)
   mallard.fly_behavior()
   print('-----------------')


   redhead.quack_behavior()
   redhead.fly_behavior()
   redhead.display()

   rubberduck.quack_behavior()
   rubberduck.fly_behavior()
   rubberduck.display()
   ```

다음과 같이 코드를 바꾸고 나서 다음과 같은 기존의 문제를 해결할 수 있었다.

- 코드의 재사용성 높이기 (fly, quack 행동과 관련된 클래스만 추가해주면 새로운 오리를 만들어도 중복된 코드의 사용을 피할 수 있다.)
- 기존의 방식에 비해 사용성이 간편해졌다. 특정 오리의 fly, quack을 변경할 수도 있게 되었다.



3. 파이썬에 어울리는 코드로 고쳐보기

> 위의 예제는 Java의 코드를 파이썬에 맞게 구현하려고 하다보니, 언어적으로 어울리지 않는 부분이 생겼다. Strategy Pattern은 여러 OO 언어에서 유용하지만 python에는 적합하지 않다고 한다. '행동'을 정하는 클래스에 붙는 추가적인 데이터가 없기 때문에 파이썬에서는 직접적으로 함수를 사용해도 무방하기 때문이다. (함수가 일급 객체!)

```python
class Duck:
    def __init__(self, func_quack, func_fly):
        #클래스의 quack 혹은 fly와 관련된 행동 속성에 접근할 때 해당하는 함수가 호출된다.
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
```



