# 제어문
## 조건문(Conditional Statement)
* 참/거짓을 판단할 수 있는 조건식과 함께 사용

``` python
a = 5
if a > 5:
    print('5초과')
else:
    print('5이하')
print(a)
```

``` python
num = int(input())
if num % 2 :
    print('홀수')
else:
    print('짝수')
```

``` python
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

``` python
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

``` python
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

``` python
a = 0
while a < 5:
    print('a')
    a += 1
print('끝')
```

### 복합 연산자(In-Place Operator)
* 연산과 할당을 합쳐 놓은 것
* ec) 반복문으로 개수를 카운트 하는 경우

``` python
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

``` python
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
``` python
grades = {'john': 80, 'eric': 90}
for i in grades:
    print(i)

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

``` python
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

``` python
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

``` python
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
``` python
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
# 0, 1, 2 출력

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
``` python
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
``` python
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

``` python
def function_name(parameter):
    # code block
    return returning_value
```

``` python

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
    ``` python
    def print_function():
        print('야호')
    def return_function():
        return '야호'
    
    print_result = print_function()     # 야호
    return_result = return_function()
    print(print_result, return_result)  # None 야호

    ```
  * return은 항상 하나의 값을 반환
  * 튜플, 리스트를 활용하여 두 개 이상의 값 반환 가능
    ``` python
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
   ``` python
   def add(x, y):
    return x + y

   add(x=2, y=5)
   add(2, y=5)
   add(x=2, 5)     #에러 발생 : keyword 다음에 positional 사용불가 
   ```

  * Default Arguments Values
     * 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
   ``` python
   def add(x, y=0):
    return x + y
    ```
* 가변 인자(*args)
  * 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
  * 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 사용

``` python
def add(*args):
    for arg in args:
        print(arg)
```
* 패킹 : 여러 개의 데이터를 묶어서 변수에 할당하는 것
``` python 
numbers = (1, 2, 3, 4, 5)   # 패킹
print(numbers)
```
* 언패킹 : 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
``` python
numbers = (1, 2, 3, 4, 5)
a, b, c, d, e = numbers     # 언패킹
print(a, b, c, d, e)
```
```python
# 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야함
numbers = (1, 2, 3, 4, 5)     # 패킹
a, b, c, d, e, f = numbers    # 언패킹
# ValueError : not enough values to unpack (expected 6, got 5)

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

## 함수의 문서화(Doc-string)

## 함수 응용
