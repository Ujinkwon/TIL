# 문법 에러(Syntax Error)
* 정확한 에러 위치를 지정하지 않을 수도 있음

* Syntax Error : invalid syntax    
  * 콜론 누락
* Syntax Error : `EOL` while scanning string listeral
  * 따옴표 오류
* Syntax Error : unexpected `EOF` while parsing
  * 괄호 닫기 오류

# 예외(Exception)
* 문법적으로는 옳지만, 실행 시 발생하는 에러

* ZeroDivisionError : division by zero
  * 어떤 수를 0으로 나누면 발생


* NameError : name 'abc' is not defined
  * 어느 곳에서도 정의되지 않은 변수 호출 시


* TypeError : unsupported operand type(s) for +: 'int' and 'str'  # 숫자 1+ 문자 1
* TypeError : type str doesn't define __round__ method    # round 함수에는 숫자 입력
* TypeError : sample() missing 1 required positional argument: 'k'    # 매개변수 2갠데, 1개만 넣음
* TypeError : choice() takes 2 positional arguments but 3 were given   # 매개변수 1갠데, 2개 넣음
  * 자료형이 올바르지 못한 경우 
  * 함수 호출 과정에서 필수 매개변수가 누락된 경우
  * 함수 호출 과정에서 매개변수 개수가 초과해서 들어온 경우


* ValueError : invalid literal for int() with base 10: '3.5'   # int()가 정수가 아닌 값을 받았을 경우 (문자 3.5 넣음)
* ValueError : 3 is not in list  # 리스트에 없는 값 찾고자 함
  * 자료형은 올바르나 값이 적절하지 않은 경우
  * 존재하지 않는 값을 찾고자 할 경우

* IndexError : list index out of range
  * 존재하지 않는 인덱스로 조회할 경우

* KeyError : 'queen'
  * 존재하지 않는 key로 접근한 경우

* ModuleNotFoundError : No module named 'reque'
  * 존재하지 않는 Module을 불러오는 경우

* ImportError: cannot import name 'sampl' from 'random'
  * 모듈은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우
  * 모듈을 불러와서 함수를 불러오기 => from 모듈 import 함수

* KeyboardInterrupt:
  * 사용자가 임의로 실행을 중단한 경우

* IndentationError: expected an indented block   # 들여 쓰기 안한 경우
* IndentationError: unexpected indent     # 들여 쓰기 한 경우
  * indentation(들여 쓰기)이 적절하지 않은 경우


# 예외 처리
  * 에외가 발생하면 남은 부분을 수행하지 않고 except 실행
  * 에러가 순차적으로 수행되므로 가장 작은 범주부터 시작해야 함
    * `Exception` 은 가장 큰 범주 !!!!

## try - except
  ```python
  try:
    <code block 1>
  except (예외):
    <code block 2>
  ```

  ```python
  try:
    <code block 1>
  except (예외 1, 예외 2):
    <code block 2>


  try:
    <code block 1>
  except 예외 1:
    <code block 2>
  except 예외 2:
    <code block 3>
  ```
## else
* 에러가 발생하지 않는 경우 수행되는 문장은 `else`를 이용
* 모든 except 절 뒤에 와야 함
```python
  try:
    <code block 1>
  except 예외:
    <code block 2>
  else:
    <code block 3>
```

## finally
* 반드시 수행해야 하는 문장은 `finally`를 활용
* 예외의 발생 여부와 관계없이 try 문을 떠날 때 항상 실행
```python
  try:
    <code block 1>
  except 예외:
    <code block 2>
  finally:
    <code block 3>
```

## as
* except 구문에서 발생하는 에러 메세지를 코드 블럭에 넘겨줌
```python
  try:
    <code block 1>
  except 예외 as err:
    <code block 2>   # print(f'{err}')
```

# 예외 발생 시키기(Exception Rasing)
## raise
* 예외를 강제로 발생
* `raise <에러>('메세지')`    # raise ValueError('hi') => ValueError: hi

## assert
* 보통 상태를 검증하는데 사용 
* 무조건 AssertionError 가 발생
* `assert Boolean expression, error message`    # assert len([1, 2]) == 1, '길이가 1이 아닙니다.'