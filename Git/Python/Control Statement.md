# 제어문

## 조건문(Conditional Statement)

* 참/거짓을 판단할 수 있는 조건식과 함께 사용

```python
a = 5
if a > 5:
    print('5초과')
else:
    print('5이하')
print(a)
```

```python
num = int(input())
if num % 2 :
    print('홀수')
else:
    print('짝수')
```

```python
dust = int(intput())
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

print('미세먼지 확인 완료')
```

## 중첩 조건문

* 조건문은 다른 조건문에 중첩되어 사용 가능

```python
dust = 140

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('값이 잘못되었습니다.')
    else:
        print('좋음')
```

## 조건 표현식

* 일반적으로 조건에 따라 값을 정할 때 활용
* 삼항 연산자로 부르기도 함
* 'True인 경우 값' if '조건' else 'False인 경우 값'

```python
value = num if num >= 0 else -num
# 절댓값을 저장하기 위한 코드
```

```python
num = 2
if num % 2:
    result = '홀수입니다.'
else:
    result = '짝수입니다.'
print(result)

# 동일한 조건 표현식 작성하기

num = 2
result = '홀수입니다.' if num % 2 else '짝수입니다.'
print(result)
```

```python
num = -5
value = num if num >= 0 else 0
print(value)

# 동일한 조건문 작성하기

num = -5
if num >= 0:
    value = num
else:
    value = 0
print(value)
```

-----

## 반복문

* 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
* while 문 : 종료조건에 해당하는 코드를 통해 종료
* for 문 : 반복 가능한 객체를 모두 순회하면 종료 (종료조건 필요 없음)
* 반복 제어 : break, continue, for-else

## while문

* 조건식이 참인 경우 반복적으로 코드 실행
* 무한 루프를 하지 않도록 종료 조건이 반드시 필요

```python
a = 0
while a < 5:
    print('a')
    a += 1
print('끝')
```

### 복합 연산자(In-Place Operator)

* 연산과 할당을 합쳐 놓은 것
* ec) 반복문으로 개수를 카운트 하는 경우

```python
cnt = 100
cnt += 1
print(cnt)

cnt = 0
while cnt < 3:
    print(cnt)
    cnt += 1
```

## for문

* 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소를 모두 순회
* 별도의 종료조건 필요 없음
* iterable
  * 순회할 수 있는 자료형 (string, list, dict, tuple, range, set 등)
  * 순회형 함수 (range, enumerate)

```python
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')
```

### for문을 이용한 문자열 순회

```python
#사용자가 입력한 문자를 한 글자씩 출력
chars = 'happy'
for i in chars:
    print(i)

#사용자가 입력한 문자를 range를 활용해 한 글자씩 출력
chars = 'happy'
for i in range(len(chars)):
    print(chars[i])
```

### Dictionary 순회

* 딕셔너리는 기본적으로 `key`를 순회하며, key를 통해 값을 활용
  
  ```python
  grades = {'john': 80, 'eric': 90}
  for i in grades:
    print(i)
  ```

for i in grades:
    print(i, grades[i])

```
* 추가 메서드를 활용하여 순회할 수 있음
  * keys() : key로 구성된 결과
  * values() : value로 구성된 결과
  * items() : (key, value)의 tuple로 구성된 결과

``` python
grades = {'john': 80, 'eric': 90}
print(grades.keys())       # dict_keys {['john', 'eric']}
print(grades.values())     # dict_values {[80, 90]}
print(grades.items())      # dict_items {[('john', 80), ('eric', 90)]}

for student, grade in grades.items():
    print(student, grade)
```

### enumerate 순회

* enumerate()
  * 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
  * (index, value) 형태의 tuple로 구성된 열거 객체를 반환

```python
members = ['민수', '영희', '철수']

for idx, number in enumerate(members):
    print(idx, number)
# 0 민수
# 1 영희
# 2 철수

* list(enumerate(members, start=1))  # [(1, '민수'), (2, '영희'), (3, '철수')]
# 기본값 0, start를 지정하면 해당 값부터 순차적으로 증가
```

### List Comprehension

* 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법
* [code for 변수 in iterable]
* [code for 변수 in iterable if 조건식]

```python
# 1~3의 세제곱 리스트 만들기
cubic_list = []
for i in range(1, 4):
    cubic_list.append(number ** 3)
print(cubic_list)


cubic_list = [number ** 3 for number in range(1, 4)]
print(cubic_list)
```

### Dictionary Comprehension

* 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법
* {key : value for 변수 in iterable}
* {key : value for 변수 in iterable if 조건식}

```python
# 1~2개의 세제곱 딕셔너리 만들기
cubic_dict = {}
for number in range(1, 4):
    cubic_dict[number] = number ** 3
print(cubic_dict)


cubic_dict = {number : number ** 3 for number in range(1, 4)}
print(cubic_dict)
```

## 반복문 제어

### break

* 반복문을 종료
  
  ```python
  n = 0
  while True:
    if n == 3:
        break
    print(n)
    n += 1
  # 0, 1, 2 출력
  ```

for i in range(10):
    if i > 1:
        print('0과 1만 필요해!')
        break
    print(i)

# 0, 1, 0과 1만 필요해! 출력

```
### continue 
* continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
``` python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)
# 1, 3, 5 출력
```

### for-else

* 끝까지 반복문을 실행한 이후에 else문 실행
* break를 통해 중간에 종료되는 경우, else 문은 실행되지 않음
  
  ```python
  for char in 'banana':
    if char == 'b':
        print('b!')
        break
  else:
    print('b가 없습니다')
  # b! 출력
  ```

### pass

* 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)
  
  ```python
  for i in range(4):
    if i == 2:
        pass
    print(i)
  # 0, 1, 2, 3 출력
  ```

------

# 함수

## 함수 기초

* 함수의 필요성 : 재사용성과 가독성, 생산성
  
  1. Decomposition : 기능을 분해하고 재사용 가능하게 만들고
  2. Abstraction : 복잡한 내용을 모르더라도 사용할 수 있도록(블랙박스)

* 함수의 종류
  
  * 내장 함수 : 파이썬에 기본적으로 포함된 함수
  * 외장 함수 : import문을 통해 사용, 외부 라이브러리에서 제공하는 함수
  * 사용자 정의 함수 : 직접 만드는 함수

* 함수
  
  * 특정한 기능을 하는 코드의 조각
  * 특정 코드를 필요시에만 호출하여 간편히 사용

* 기본 구조
  
  * 선언과 호출(define & call)
    * 선언은 `def` 키워드 활용
    * 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성
      * Docstring은 함수 body 앞에 선택적으로 작성 가능
      * 작성시에는 반드시 첫 번째 문장에 """
    * 함수는 parameter를 넘겨줄 수 있음
    * 함수는 동작 후에 return을 통해 결과값 전달

```python
def function_name(parameter):
    # code block
    return returning_value
```

```python
def foo():
    return True

foo()    #함수명()으로 호출하여 사용


def add(x, y):
    return x + y

add(2, 3)    # parameter가 있는 경우, 함수명(값1, 값2, ...)으로 호출
```

## 함수의 결과값(Output)

* 값에 따른 함수의 종류
  
  * Void function
    
    * 명시적인 return 값이 없는 경우, None을 반환하고 종료
  
  * Value returning function
    
    * 함수 실행 후, return 문을 통해 값 반환
    * return을 하게 되면, 값 반환 후 함수가 바로 종료
    * 주의) print vs return
      * print를 사용하면 호출될 때마다 값이 출력됨
      * 데이터 처리를 위해서는 return 사용
      * REPL(Read-Eval-Print Loop) 환경에서는 마지막으로 작성된 코드의 리턴 값을 보여주므로 같은 동작을 하는 것으로 착각할 수 있음
        
        ```python
        def print_function():
        print('야호')
        def return_function():
        return '야호'
        ```
    
    print_result = print_function()     # 야호
    return_result = return_function()
    print(print_result, return_result)  # None 야호
    
    ```
  
  * return은 항상 하나의 값을 반환
  
  * 튜플, 리스트를 활용하여 두 개 이상의 값 반환 가능
    
    ```python
    # tuple
    def minus_and_product(x, y):
      return x - y, x * y
    
    y = minus_and_product(4, 5)
    print(y)      # (-1, 20)
    
    # list
    word_list = ['우영우', '기러기', '별똥별', '파이썬']
    def is_palindrome(word_list):
        palindrome_list = []
        for word in word_list:
            if word == word[::-1]:
                palindrome_list.append(word)
    
        return palindrome_list
    
    print(is_palindrome(word_list))
    ```

## 함수의 입력(Input)

* Parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수

* Argument : 함수를 호출 할 때, 넣어주는 값
  
  * 소괄호 안에 할당 func_name(argument)
  
  * Positional Arguments : 기본적으로 함수 호출 시 위치에 따라 함수 내에 전달
  
  * Keyword Arguments : 직접 변수의 이름으로 Argument를 전달
    
    ```python
    def add(x, y):
    return x + y
    
    add(x=2, y=5)
    add(2, y=5)
    add(x=2, 5)     #에러 발생 : keyword 다음에 positional 사용불가 
    ```
  
  * Default Arguments Values
    
    * 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
      
      ```python
      def add(x, y=0):
      return x + y
      ```

* 가변 인자(*args)
  
  * 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  * 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 사용

```python
def add(*args):
    for arg in args:
        print(arg)
```

* 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
  
  ```python
  numbers = (1, 2, 3, 4, 5)   # 패킹
  print(numbers)
  ```
* 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
  
  ```python
  numbers = (1, 2, 3, 4, 5)
  a, b, c, d, e = numbers     # 언패킹
  print(a, b, c, d, e)
  ```
  
  ```python
  # 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함
  numbers = (1, 2, 3, 4, 5)     # 패킹
  a, b, c, d, e, f = numbers    # 언패킹
  # ValueError : not enough values to unpack (expected 6, got 5)
  ```

# 언패킹시 변수의 왼쪽에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음

numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers      # 1, 2를 제외한 나머지를 rest에 대입
print(a, b, rest)          # 1 2 [3, 4, 5]

```
* Asterisk(*)와 가변 인자
  * 시퀀스 언패킹 연산자라고도 하며, 시퀀스를 풀어 해치는 연산자
  * 주로 튜플이나 리스트를 언패킹, `리스트`로 처리
  * 가변 인자를 만들 수 있음

``` python
# 패킹을 통해 받은 모든 숫자들의 합을 구하는 함수

def sum_all(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(sum_all(1, 2, 3))    # 6


# 반드시 받아야하는 인자와, 추가적인 인자를 구분해서 사용 가능
def print_family_name(father, mother, *pets):
    for name in pets:
        print(f'{name}')
    print(f'{father}, {mother}')

print_family_name('아빠', '엄마', '멍멍이', '냥냥이')
```

* 가변 키워드 인자(**kwargs)
  * 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
  * `딕셔너리`로 묶여서 처리
    
    ```python
    def family(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
    family(father='아부지', mother='어무니', baby='아가')
    ```

def print_family_name(father, mother, **pets):
    for species, name in pets.items():
        print(f'{species} : {name}')
    print(f'{father}, {mother}')

print_family_name('아빠', '엄마', dog='멍멍이', cat='냥냥이')

```
```python
# 가변 인자와 가변 키워드 인자 동시 사용 가능
def print_family_name(*parents, **pets):
    print(parents[0], parents[1])
    if pets:
        for species, name in pets.items():
            print(f'{species}:{name}')

print_family_name('아부지', '어무니', dog='멍뭉', cat='냥냥')
```

## 함수의 범위(Scope)
* 함수는 코드 내부에 local scope를 생성하고 그 외의 공간인 global scope로 구분
* scope 
  * global scope : 코드 어디에서든 참조할 수 있는 공간
  * local scope : 함수가 만든 scope / 함수 내부에서만 참조 가능
* variable 
  * global variable : global scope에 정의된 변수
  * local variable : local scope에 정의된 변수
* 변수 수명주기(lifecycle)
  * built-in scope : 파이썬이 실행된 이후부터 영원히 유지
  * global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  * local scope : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지
  ```python
  def func():
    a = 20
    print('local', a)  # local 20
  
  func()
  print('global', a)   # NameError : name 'a' is not defined
  # a는 local scope에서만 존재
  ```

* 이름 검색 규칙(Name Resolution)
  * 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
  * 아래와 같은 순서로 이름을 찾아나가고, LEGB Rule이라고 부름
    * Local scope : 지역 범위(현재 작업 중인 범위)
    * Enclosed scope : 지역 범위 한 단계 위 범위
    * Global scope : 최상단에 위치한 범위
    * Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)
      * ex) print()
    * 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 할 수 없음
  ``` python
  print(sum)       # <built-in function sum>
  print(sum(range(2)))   # 1
  sum = 5
  print(sum)    # 5
  print(sum(range(2)))    # TypeError : 'int' object is not cllable
  # Global sope 이름공간의 sum 변수에 값 5가 할당
  # 이후 global scope에서 sum은 LEGB에 의해 built-in scope의 내장 함수보다 5가 먼저 탐색
  ```
  ```python
  a = 0
  b = 1
  def enclosed():
    a = 10
    c = 3
    def local(c):
      print(a, b, c)   # 10 1 300
    local(300)         
    print(a, b, c)     # 10 1 3

  enclosed()         
  print(a, b)          # 0 1
  ```

  * glbal 문
    * 현재 코드 블록 전체에 적용되며, 나열된 식별자가 global variable임을 나타냄
    * global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
    * global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
  ```python
  # 함수 내부에서 글로벌 변수 변경하기
  a = 10
  def func1():
    global a
    a = 3

  print(a)    # 10
  func1()
  print(a)    # 3
  # local scope에서 global 변수 값의 변경
  # global 키워드를 사용하지 않으면, local scope에 a변수가 생성됨
  ```
  * global 관련 에러
  ``` python
  a = 10
  def func():
    print(a)     # global a 선언 전에 사용
    global a
    a = 3
  print(3)
  func()
  print(a)
  # SystaxError : name 'a' is used prior to global declaration


  a = 10
  def func(a):    # parameter에 global 사용 불가
    global a
    a = 3
  print(a)
  func(3)
  print(a)
  # SystaxError : name 'a' is parameter and global
  ```

  * nonlocal
    * global을 제외하고 가장 가까운 scope의 변수를 연결하도록 함
      * nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장할 수 없음
      * nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
    * global과 달리 이미 존재하는 이름과의 연결만 가능함
  ``` python
  x = 0
  def func1():
    x = 1
    def func2():
      nonlocal x
      x = 2
    func2()
    print(x)   # 2

  func1()
  print(x)     # 0
  ```
  ``` python
  def func1():
    def func2():
      nonlocal y
      y = 2
    func2()
    print(y)
  func1()

  # SystaxError : no binding for nonlocal 'y' found
  # nonlocal은 이름공간상에 존재하는 변수만 가능
  ```

  * `함수의 범위 주의`
    * 기본적으로 함수에서 선언된 변수는 local scope에 생성되며, 함수 종료 시 사라짐
    * 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색함
      * 변수에 접근은 가능하지만, 해당 변수를 수정할 수는 없음
      * 값을 할당하는 경우 해당 scope의 이름공간에 새롭게 생성되기 때문
      * `단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용할 것`
    * 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
      * 단 코드가 복잡해지면서 변수의 변경을 추적하기 어렵고, 예기치 못한 오류가 발생
      * 가급적 사용하지 않는 것을 권장하며, `함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값을 사용하는 것을 추천`
  

## 함수 응용
* 내장 함수 (Built-in Functions) : 파이썬 인터프리터에는 항상 사용할 수 있는 많은 함수와 형이 내장되어 있음
### map
* map(function, iterable)
* 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
``` python
numbers = [1, 2, 3]
result = map(str, numbers)
print(result. type(result))
# <map object at 0x0000020984097FA0> <class 'map'>
print(list(result))   # ['1', '2', '3']
```
```python
n, m = map(int, input().split())   # 3, 5를 입력하면
print(n, m)                        # 3, 5
print(type(n), type(m))            # <class 'int'> <class 'int'>
```
### filter
* filter(function, iterable)
* 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환
``` python
def odd(n):
  return n % 2
numbers = [1, 2, 3]
result = filter(odd, numbers)
print(result, type(result))
# <filter object at 0x000001FB4B217F40> <class 'filter'>
print(list(result))       # [1, 3]
```

### zip
* zip(*iterables)
* 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
``` python
girls = ['jane', 'ashley']
boys = ['justin', 'eric']
pair = zip(girls, boys)
print(pair, type(pair))
print(pair, type(pair))    
# <zip object at 0x000001A4B3DD0380> <class 'zip'>
print(list(pair))    # [('jane', 'justin'), ('ashley', 'eric')]
```

### lambda
* lambda[parameter]: 표현식
* 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
* 특징
  * return 문을 가질 수 없음
  * 간편 조건문 외 조건문이나 반복문을 가질 수 없음
* 장점
  * 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
  * def를 사용할 수 없는 곳에서도 사용가능

``` python
# 삼각형의 넓이를 구하는 공식 - def
def tri_area(b, h):
  return 0.5 * b * h
print(tri_area(5, 6))  # 15.0

# 삼각형의 넓이를 구하는 공식 - lambda
tri_area = lambda b, h : 0.5 * b * h
print(tri_area(5, 6))   # 15.0
```

### 재귀 함수(recursive function)
* 자기 자신을 호출하는 함수
* 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
* 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
* 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
* 주의 사항
  * base case에 도달할 때까지 함수를 호출함
  * 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 않게 됨
  * 파이썬에서는 최대 재귀 깊이가 1000번으로 호출 횟수가 이를 넘어가게 되면 recursion erro 발생

``` python
# factorial 재귀
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)
print(factorial(4))    # 24

# factoral 반복문
def fact(n):
  result = 1
  while n > 1:
    result *= n
    n -= 1
  return result
print(fact(4))          # 24
```
* 재귀함수 vs 반복문
  * 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용함
  * 재귀 호출은 변수 사용을 줄여줄 수 있음
  * 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림


## 모듈
* 모듈(module) : 다양한 기능을 하나의 파일로
* 패키지(pacakge) : 다양한 파일을 하나의 폴더로
* 라이브러리(library) : 다양한 패키지를 하나의 묶음으로
* pip : 이것을 관리하는 관리자
* 가상환경 : 패키지의 활용 공간
### 모듈과 패키지
* 모듈 
  * 특정 기능을 하는 코드를 파이썬 파일(.py)단위로 작성한 거
   ```python
   import module
   from module import var, function, class
   from module import*
   ```

* 패키지
  * 특정 기능과 관련된 여러 모듈의 집합
  * 패키지 안에는 또 다른 서브 패키지를 포함
   ```python
   from package import module
   from package.module import var, function, class
   ```

### 파이썬 표준 라이브러리

### 사용자 모듈과 패키지

### 가상환경
