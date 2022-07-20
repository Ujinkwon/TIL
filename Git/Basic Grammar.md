# 기초 문법
## 변수(Variable)
 * 데이터를 저장하기 위해서 사용
 * 변수를 사용하면 복잡한 값들을 쉽게 사용할 수 있음(추상화)
 * 동일 변수에 다른 데이터를 언제든 할당(저장)할 수 있기 때문에, 변수라고 불림

## 추상화(변수를 사용해야 하는 이유)

```print(2000)
print(2000 + 2000)
print(3000 * 2 + 3500 * 3 + 4000 * 5)
```

 * 결과는 잘 나오지만, 몇 가지 문제 있음
   * 일일이 값을 넣는 것이 불편함 & 오타 발생 가능
   * 코드를 알아보기 힘듦
   * 고치기 어려운 코드

```americano_price = 2000
mocha_price = 3000
cookie_price = 2000
cake_price = 4000
lemonade_price = 3500

print(americano_price)
print(americano_price + cookie_price)
print(mocha_price * 2 + lemonade_price * 3 + cake_price * 5)
```

## 변수의 할당
* 변수는 할당 연산자 = 를 통해 값을 할당
* 같은 값을 동시에 할당할 수 있음
* 다른 값을 동시에 할당할 수 있음

## 각 변수의 값을 바꿔서 저장하기
1. 임시 변수 활용
 ```x, y = 1., 20
 tmp = x
 x = y
 y = tmp
 print(x, y)
 ```

2. Pythonic!
 ```x, y = 10, 20
 y, x = x, y
 print(x, y)
 ```

## 식별자
* 변수 이름 규칙
  * 식별자의 이름은 영문 알파벳, 언더스코어, 숫자로 구성
  * 첫 글자에 숫자가 올 수 없음
  * 길이 제한이 없고, 대소문자를 구별
  * 다음의 키워드는 예약어로 사용할 수 없음
  * 내장 함수나 모듈 등의 이름도 사용하지 않아야 함

## 산술 연산자
* // : 몫
* ** : 거듭제곱
* 기본적인 사칙연산 및 수식 계산
```
i = 5
j = 3

print(i + j) # 5 + 3 = 8
print(i - j) # 5 - 3 = 2
print(i * j) #5 * 3 = 15
print(i // j) # 5 나누기 3의 몫 = 1
print(i / j) # 5 나누기 3 = 1.66667
print(i ** j) # 5의 3승 = 125
```
## 연산자 우선순위
* 기본적으로 수학에서 우선순위와 같음
* 괄호가 가장 먼저 계산되고, 그 다음에 곱하기와 나누기, 더하기와 빼기 순서

## 자료형(Datetype) 분류
* 프로그래밍에서는 다양한 종류의 값(데이터)를 쓸 수 있음
* 사용할 수 있는 데이터의 종류들을 자료형이라고 함

## 1. 수치형(Numeric Type)
* 정수 자료형(int)
  * 정수를 표현하는 자료형
  * 일반적인 사칙 연산 가능
* 진수 표현
  * 2진수(binary) : 0b
  * 8진수(octal) : 0o
  * 16진수(hex) : 0x
* 실수 연산시 주의할 점(부동 소수점)
  * 실수의 값을 처리할 때 의도하지 않은 값이 나올 수 있음
  * 원인은 부동 소수점 때문
    * 컴퓨터는 2진수를 사용, 사람은 10진법을 사용
    * 이때 10진수 0.1은 2진수로 표현하면 무한대로 반복
    * 무한대 숫자를 그대로 저장할 수 없어서 사람이 사용하는 10진법의 근사값만 표시
    * 이런 과정에서 예상치 못한 결과가 나타남
  * 해결책
    * 값 비교하는 과정에서 정수가 아닌 실수면 주의할 것
    * 매우 작은 수보다 작은지를 확인하거나 math 모듈 활용

## 2. 문자열 (String Type)
* 모든 문자는 str 타입
* 문자열은 따옴표를 활용하여 표기
* Escape sequence
  * backslach 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
  * \n : 줄바꿈
  * \t : 탭
  * \r : 캐리지 리턴
  * \0 : Null
  * \ \ : \
  * \' : 단일인용부호
  * \" : 이중인용부호
* 문자열 연산
  * 덧셈 : 문자열을 연결
  * 곱셈 : 횟수만큼 반복
* Strimg Interpolation(문자열을 변수를 활용하여 만드는 법)
  * %-formatting
    ```
    name = 'kim'
    score = 4.5
    print('Hello, %s' %name)      # Hello, kim
    print('내 성적은 %d', %score)  # 내 성적은 4
    pritn('내 성적은 %f', %score)  # 내 성적은 4.500000
    ```
  * str.format()
    ```
    name = 'kim'
    score = 4.5
    print('Hello, {}! 성적은 {}'.format(name, score))
    # Hello, kim! 성적은 4.5
    ```
  * f-string : python 3.6+
    ```
    name = 'kim'
    score = 4.5
    print(f'Hello, {name}! 성적은 {score}')
    # Hello, kim! 성적은 4.5

    import datetime
    todat = datetime.datetime.now()
    print(today) 
    # 2022-07-18 11:10:15.

    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일')
    # 오늘은 22년 7월 18일

    pi = 3.141592
    print(f'원주율은 {pi:3}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
    # 원주율은 3.14. 반지름이 2일 때 원의 넓이는 12.566368
    ```

## 3. 불리언형 (Boolean Type)
* 논리 자료형으로 참/거짓을 표현하는 자료형
* 비교/논리 연사에서 활용
* True / False
* 비교 연산자
  * 결과는 True/False 값을 리턴
  ```
  print(3 > 6)    # False
  print(3.0 == 3) # True
  print(3 >= 0)   # True
  ```
* 논리 연산자
  * and / or / Not
   ```
   num = 100
   print(num >= 100 and num % 3 == 1)  # True
   ```
  * Falsy : False는 아니지만 같은 취급 되는 다양한 값
    * 0, 0.0, (), [], {}, None, 빈 문자열
  * 논리 연산자도 우선순위가 존재
    * not, and, or 순
  * 논리 연산자의 단축 평가
    * 결과가 확실한 경우 두번째 값을 확인하지 않고 첫번째 값 반환
    * and 연산에서 첫번째 값이 False인 경우 무조건 False
    * or 연산에서 첫번째 값이 True인 경우 무조건 True


## 4. None
* 값이 없음을 표현하기 위해 None 타입이 존재
* 일반적으로 반환 값이 없는 함수에서 사용하기도 함

------
## 컨테이너
* 여러 개의 데이터를 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음
* 컨테이너의 분류
  * 순서가 있는 데이터 (Ordered) vs 순서가 없는 데이터 (Unordered)
  * 순서가 있다 != 정렬되어 있다.
  * 1. 시퀀스형 - 리스트 / 튜플 / 레인지
  * 2. 비시퀀스형 - 세트 / 딕셔너리

## 1. 시퀀스형
### 1-1. 리스트
* 리스트는 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
* 대괄호[] or list()를 통해 생성
  * 파이썬에서는 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
  * 생성된 이후 내용 변경 가능 = `가변 자료형(multable)`
* 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
  * list[i]

예시
```
my_list = []
another_list = list()
print(type(my_list))       # <class 'list'>
print(type(another_list))  # <class 'list'>
location = ['서울', '대전', '구미']
print(location)          # ['서울', '대전', '구미']
print(type(location))    # <class 'list'>
print(location[0])       # 서울

location[0] = '양양'
print(location)          # ['양양', '대전', '구미']
```
Quiz
```
boxes = ['A', 'B', ['apple', 'banana', 'cherry']]
print(len(boxes))          # 3
print(boxes[2])            # ['apple', 'banana', 'cherry']
print(boxes[2][-1])        # cherry
print(boxes[-1][1][0])     # b
```

### 1-2. 튜플
* 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
* 리스트와의 차이점은 생성 후, 담고 있는 값 변경 불가 = `불변 자료형`
* 소괄호(()) or tuple()을 통해 생성
* 튜플은 수정 불가능한 시퀀스로 인덱스로 접근 가능
* 값에 대한 접근은 my_tuple[i]
```
print((1, 2, 3, 1))          #(1, 2, 3, 1)
print(tuple((1, 2, 3, 1)))   #(1, 2, 3, 1)
print(type((1, 2, 3, 1)))    #<class 'tuple'>

a = (1, 2, 3, 1)
print(a[1])       # 2
a[1] = '3'        # TypeError : 'tuple' object does not support item assignment
```
* 단일 항목으로 구성된 튜플은 생성 시 값 뒤에 쉼표 필수
* 복수 항목의 경우, 마지막 항목에 붙은 쉼표는 없어도 되지만, 넣는 것을 권장
* 튜플 대입
  * 우변의 값을 좌변의 변수에 한 번에 할당하는 과정


### 1-3. Range
* 숫자의 시퀀스를 나타내기 위해 사용
* 주로 반복문과 함께 사용됨
* 기본형 : range(n)
  * 0 ~ n-1 까지의 숫자의 시퀀스
* 범위 지정 : range(n, m)
  * n ~ m-1 까지의 숫자의 시퀀스
* 범위 및 스텝 지정 : range(n, m, s)
  * n ~ m-1 까지 s만큼 증가시키며 숫자의 시퀀스

```
print(list(range(3)))           # [0, 1, 2]
print(list(range(1, 5)))        # [1, 2, 3, 4]
print(list(range(1, 5, 2)))     # [1, 3]

print(list(range(6, 1, -1)))    # [6, 5, 4, 3, 2]
print(list(range(6, 1, -2)))    # [6, 4, 2]
print(list(range(6, 1, 1)))     # []
```

## 슬라이싱 연산자
* 시퀀스를 특정 단위로 슬라이싱
  * 인덱스와 콜론을 사용하여 문자열의 특정 부분만 잘라낼 수 있음
  * 슬라이싱을 이용하여 문자열을 나타낼 때 콜론을 기준으로 앞 인덱스에 해당하는 문자는 포함되지만 뒤 인덱스에 해당 문자는 미포함

```
# 리스트
print([1, 2, 3, 5][1:4])      # [2, 3, 4]
# 튜플
print((1, 2, 3)[:2])          # (1, 2)
# range
print(range(10)[5:8])         # range(5, 8)
# 문자열
print('abcd'[2:4])            # cd
```
* 시퀀스를 k간격으로 슬라이싱
```
print([1, 2, 3, 5][0:4:2])      # [1, 3]
# 튜플
print((1, 2, 3, 5)[0:4:2])      # (1, 3)
# range
print(range(10)[1:5:3])         # range(1, 5, 3)
# 문자열
print('abcdefg'[1:3:2])         # b
```
s[::] = s[0:len(s):1]
s[::-1] = s[-1:-(len(s)+1):-1]


## 2 비시퀀스형 
### 2-1. Set
* 중복되는 요소 없이, 순서에 상관없는 데이터들의 묶음
  * 중복되는 원소가 있다면 하나만 저장
  * 순서가 없기 때문에 인덱스를 이용한 접근 불가능
* 수학에서의 집합을 표현한 컨테이너
  * 집합 연산이 가능
* 담고 있는 요소를 삽입 변경, 삭제 가능 = `가변 자료형`
* 중괄호({}) or set() 을 통해 생성
  * 빈 Set을 만들기 위해서는 set() 활용
```
print({1, 2, 3, 1, 2})     # {1, 2, 3}
print(type({1, 2, 3}))     # <class 'set'>

blank = {}                 # 빈 중괄호는 Dictionary
print(type(blank))         # <class 'dict'>
blank_set = set()
print(type(blank_set))     # <class 'set'>

print({1, 2, 3}[0])        # TypeError : 'set' object is not subscriptable (set에는 순서가 없어 특정 값에 접근 불가능)
```
```
# 아래의 리스트에서 고유한 지역의 개수는?
my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
print(len(set(my_list)))         # 4

# 아래의 리스트에서 고유한 지역을 등장한 순서대로 출력
my_list = ['서울', '서울', '대전', '광주', '서울', '대전', '부산', '부산']
print(set(my_list))        # set을 사용하는 순간 순서가 사라져 실행 할 때마다 순서가 변경됨
```
* Set 연산자
```
A_set = {1, 2, 3, 4}
B_set = {1, 2, 3, 'Hello', (1, 2, 3)}
print(A_set | B_set)   # 합집합 {1, 2, 3, 4, (1, 2, 3), 'Hello'}
print(A_set & B_set)   # 교집합 {1, 2, 3}
print(B_set - A_set)   # 차집합 {(1, 2, 3), 'Hello'}
print(A_set ^ B_set)   # 대칭차집합 {'Hello', 4, (1,2,3)}
```

### 2-2. Dictionary
* key-value 쌍으로 이뤄진 자료형
* 3.7 부터는 ordered, 이하는 unordered ????????
* key는 변경 불가능한 데이터만 활용 가능
* value는 어떠한 형태는 관계없음
* 중괄호({}) or dict()를 통해 생성
```
dict_a = {}
print(type(dict_a))      # <class 'dict'>

dict_b = dict()
print(type(dict_b))      # <class 'dict'>

dict_a = {'a' : 'apple', 'b' : 'banana', 'list' : [1, 2, 3]}
print(dict_a['list])         #[1, 2, 3]

dict_b = dict(a='apple', b='banana', list=[1, 2, 3])
print(dict_b)            # {a='apple', b='banana', list=[1, 2, 3]}
```

## 형 변환 (Typecasting)
* 암시적 형 변환(Implicit)
  * 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
    * bool
    * Numeric type (int, float)
  ```
  print(True + 3)   # 4
  print(3 + 4.0)    # 7.0
  ```

* 명시적 형 변환(Explicit)
  * 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
    * 1. str, float => int
    ```
    # 문자열은 암시적 형 변환 불가능
    print('3' + 4)     # TypeError : can only concatenate str (not "int") to str

    # 명시적 타입 변환 필요
    print(int('3') + 4)     # 7

    # 정수 형식이 아닌 경우 타입 변환 불가능
    print(int('3.5') + 5)    # ValueError : invalid literal for int() with base 1.: '3.5' 
    ```

    * 2. str, int => float
    ```
    print('3.5' + 3.5)     # TypeError : can only concatenate str (not "float") to str

    # 정수 형식인 경우 타입 변환
    print(float('3'))       # 3.0

    # float 형식이 아닌 경우 타입 변환 불가능
    print(float('3/4') + 5.3)   # ValueError : could not convert string to float: '3/4'
    ```

    * 3. int, float, list, tuple, dict => str
    ```
    print(str(1))                # int 1
    print(str(1.0))              # float 1.0
    print(str([1, 2, 3]))        # list [1, 2, 3]
    print(str((1, 2, 3)))        # tuple (1, 2, 3)
    print(str({1, 2, 3}))        # dict {1, 2, 3}
    ```
* 컨테이너 형 변환

s![](img/컨테이너%20형%20변환.png)