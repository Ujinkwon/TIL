# 객체지향 프로그래밍(OOP)
## 객체지향 프로그래밍이란?
* 객체지향 프로그래밍이란 
  * 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법
  * 컴퓨터 프로그래밍의 패러다임 중 하나
  * 컴퓨터 프로그램을 여러 개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것
  * 각각의 객체는 메세지를 주고받고, 데이터를 처리할 수 있다.
* 객체지향 프로그래밍이 필요한 이유
  * 현실 세계를 프로그램 설계에 반영 (추상화)
* 장점
  * 클래스 단위로 모듈화시켜 개발 가능하므로 대규모 소프트웨어 개발에 적합
  * 필요한 부분만 수정하기 쉽기 때문에 유지보수 쉬움
* 단점
  * 설계 시 많은 노력과 시간이 필요함 (다양한 객체들의 상호 작용 구조를 만들기 위해)
  * 실행 속도가 상대적으로 느림 (절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷)

## OOP 기초
* 객체(컴퓨터 과학)
  * 객체 or 오브젝트는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것
  * 프로그램에서 사용되는 데이터 or 식별자에 의해 참조되는 공간
  * ex) 변수, 자료 구조, 함수, 메서드 등
  * `속성`과 `행동`으로 구성된 모든 것
  * 속성 ex) 직업, 생년월일, 국적 (정보 - 변수)
  * 행동 ex) 랩하기, 댄스 (동작 - 함수 - 메서드)

* 클래스(설계도) VS 객체(실제 사례)
* 인스턴스 : 클래스로 만든 객체
* 클래스를 만든다 == 타입을 만든다 
* 파이썬은 모든 것이 객제 : 파이썬의 모든 것엔 속성과 행동이 존재
* ex) [3, 2, 1].sort() : 리스트.정렬() / 객체.행동()
* ex) 'banana'.upper() : 문자열.대문자로() / 객체.행동()
* 객체 
  * [1, 2, 3], [1], [], ['hi'] : 리스트 타입(클래스)의 객체
  * '', 'hi', 'hello' : 문자열 타입(클래스)의 객체
* 객체는 특정 타입의 인스턴스
  * 123, 500 : int의 인스턴스
  * 'hi', 'hello' : string의 인스턴스
  * [123, 45], [] : list의 인스턴스
* 객체의 특징
  * 타입(type) : 어떤 연산자와 조작이 가능한가?
  * 속성(attribute) : 어떤 상태(데이터)를 가지는가?
  * 조작법(method) : 어떤 행위(함수)를 할 수 있는가?
  * 객체 = 속성(attribute) + 기능(method)

### 객체와 클래스 문법
* 기본 문법
  * 클래스 정의 : class MyClass:
  * 인스턴스 생성 : my_instance = MyClass()
  * 메서드 호출 : my_instance.my_method()
  * 속성 : my_instance.my_attribute
* 객체의 설계도(클래스)를 가지고 객체(인스턴스)를 생성
* 클래스 : 객체들의 분류 / 설계도(class)
* 인스턴스 : 하나하나의 실체 / 예(instance)
* 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스
```python
class Person:
    pass
print(type(Person))   # <class 'type'>
person1 = Person()
print(isinstance(person1, person))   # True
print(type(person1))            # <class '__main__.Person'>
```
* == : 변수가 참조하는 객체가 `동등한` 경우 True (실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님)
* is : 두 변수가 `동일한` 객체를 가리키는 경우 True

### OOP 속성
* 속성
  * 특정 데이터 타입 / 클래스의 객체들이 가지게 될 상태/데이터를 의미
  * 클래스 변수 / 인스턴스 변수가 존재
  ``` python
  class Person:
    blood_color = 'red'   # 클래스 변수
    population = 100      # 클래스 변수

    def __init__(self, name):
        self.name = name      # 인스턴스 변수
  person1 = Person('지민')
  print(person1.name)         # 지민
  ```
* 인스턴스 변수
  * 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  * 각 인스턴스들의 고유한 변수
  * 생성자 메서드(__init__)에서 self.<name>으로 정의
  * 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

```python
class Person:
    def __init__(self, name):   # 인스턴스 변수 정의
        self.name = name  

john = Person('john')   # 인스턴스
print(john.name)        # john
john.name = 'John Kim'  # 인스턴스 접근  / john.age = 20 (인스턴스 생성의 경우)
print(john.name)        # John Kim
```

* 클래스 변수
  * 한 클래스의 모든 인스턴스가 공유하는 값을 의미
  * 같은 클래스의 인스턴스들은 같은 값을 갖게 됨
  * ex) 특정 사이트의 User 수 등은 클래스 변수를 사용해야 함
  * 클래스 선언 내부에서 정의
  * <classname>.<name>으로 접근 및 할당
```python
class Circle():
    pi = 3.14   # 클래스 변수 정의

    def __init__(self, r):
        self.r = r  # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)    # 3.14
print(c1.pi)        # 3.14
print(c2.pi)        # 3.14

Circle.pi = 5
print(Circle.pi)     # 5
print(c1.pi)         # 5
print(c2.pi)         # 5
```

* 클래스 변수 활용(사용자 수 계산하기)
```python
class Person:
    count = 0

    # 인스턴스 변수 설정
    def __init__(self, name):
        self.name = name
        Person.count += 1   # 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정

person1 = Person('사람1')
person2 = Person('사람2')
```

* 클래스 변수와 인스턴스 변수 
  * 클래스 변수를 변경할 때는 항상 `클래스.클래스변수` 형식으로 변경

```python
class Circle():
    pi = 3.14       # 클래스 변수 정의

    def __init__(self, r):
        self.r = r  # 인스턴스 변수

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi)    # 3.14
print(c1.pi)        # 3.14
print(c2.pi)        # 3.14

Circle.pi = 5        # 클래스 변수 변경
print(Circle.pi)     # 5
print(c1.pi)         # 5
print(c2.pi)         # 5

c2.pi = 5            # 인스턴스 변수 변경
print(Cicle.pi)      # 3.14 (클래스 변수)
print(c1.pi)         # 3.14 (클래스 변수)
print(c2.pi)         # 5 (새로운 인스턴스 변수 생성)
```

### OOP 메서드
* 메서드 : 특정 데이터 타입 / 클래스의 객체에 공통적으로 적용 가능한 행위(함수)
```python
class Person:
    def talk(self):
        print('안녕')
    def eat(self, food):
        print(f'{food}를 냠냠')

person1 = Person()
person1.talk()         # 안녕
person1.eat('치킨')    # 치킨를 냠냠
```

* 인스턴스 메서드
  * 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드
  * 클래스 내부에 정의되는 메서드의 기본
  * 호출 시, 첫번재 인자로 인스턴스 자기자신(self)이 전달됨
```python
class MyClass:
    def instance_method(self, arg1, ...):

my_instance = MyClass()
my_instance.instance_method(...)
```
  * self
    * 인스턴스 자기자신
    * 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계

  * 생성자 메서드
    * 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
    * 인스턴스 변수들의 초기값을 설정
      * 인스턴스 생성
      * __init 메서드 자동 호출
  ``` python
  class Person:
    def __init__(self):
        print(f'인스턴스가 생성되었습니다. {name}')

  person1 = Person('유진')  # 인스턴스가 생성되었습니다. 유진
  ```
  * 매직 메서드
    * Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 메서드 or 매직 메서드라고 불림
    * 특정 상황에 자동으로 불리는 메서드
    * __str__(self), __len__(self), __repr__(self)
    * __lt__(self, other), __le__(self, other), __eq__(self, other)
    * __gt__(self, other), __ge__(self, other), __ne__(self, other)
  ```python
  class Circle:
    def __init__(self, r):
        self.r = r
    def area (self):
        return 3.14 * self.r * self.r
    def __str__(self):
        return f'[원] radius: {self.r}'
    def __gt__(self, other):
        return self.r > other.r
  c1 = Circle(10)
  c2 = Circle(1)

  print(c1)       # [원] radius: 10
  print(c2)       # [원] radius: 1
  print(c1 > c2)  # True
  print(c1 < c2)  # False
  ```


  * 소멸자 메서드
    * 인스턴스 객체가 소멸(파괴)되기 직전에 호출되는 메서드
  ```python
  class Person:
    def __init__(self):
        print('인스턴스가 사라졌습니다.')

  person1 = Person()
  del person1   # 인스턴스가 사라졌습니다.
  ```

* 클래스 메서드 
  * 클래스가 사용할 메서드
  * @classmethod 데코레이터를 사용하여 정의
  * 호출 시, 첫번째 인자로 클래스(cls)가 전달됨
```python
class Person:        
    count = 0                    # 클래스 변수
    def __init__(self, name):    # 인스턴스 변수 설정
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다.')

person1 = Person('사람1')
person2 = Person('사람2')
print(Person.count)    # 2
```

* 데코레이터
  * 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
  * @데코레이터(함수명) 형태로 함수 위에 작성
  * 순서대로 적용 되기 때문에 작성 순서가 중요

* 데코레이터 없이 함수 꾸미기
```python
def hello():
    print('hello')

# 데코레이팅 함수
def add_print(original):      # 파라미터로 함수를 받는다
    def wrapper():            # 함수 내에서 새로운 함수 선언
        print('함수 시작')    # 부가기능 -> original 함수를 꾸민다.
        original()
        print('함수 끝')      # 부가기능 -> original 함수를 꾸민다.
    return wrapper            # 함수를 return 

add_print(hello)()
# '함수 시작'
# 'hello'
# '함수 끝'
print_hello = add_print(hello)
print_hello()
# '함수 시작'
# 'hello'
# '함수 끝'
```

* 데코레이터를 활용하면 쉽게 여러 함수를 원하는대로 변경할 수 있음
```python
def add_print(original):      # 파라미터로 함수를 받는다.
    def wrapper():            # 함수 내에서 새로운 함수 선언
        print('함수 시작')    # 부가기능 -> original을 꾸민다.
        original()
        print('함수 끝')      # 부가기능 -> original을 꾸민다.
    return wrapper            # 함수를 return

@add_print                    # add_print를 사용해서 print_hello()함수를 꾸며주도록 하는 명령어
def print_hello():
    print('hello')

print_hello()
# '함수 시작'
# 'hello'
# '함수 끝'
```

* 클래스 메서드 VS 인스턴스 메서드
  * 클래스 메서드는 클래스 변수 사용 / 인스턴스 메서드는 인스턴스 변수 사용
  * 모두 사용하고 싶다면?
    * 클래스는 인스턴스 변수 사용 불가능
    * 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용 가능




* 정적 메서드

# 객체지향의 핵심 개념
## 추상화

## 상속

## 다형성

## 캡슐화

# 에러와 예외