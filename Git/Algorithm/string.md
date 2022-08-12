# 문자의 표현
* 코드 체계 : 영어가 대소문자 합쳐서 52므로 6비트면 모두 표현 가능
  * 000000 => 'a'
  * 000001 => 'b'
* ASCII : 문자 인코딩 표준
  * 7비트 인코딩으로 128문자 표현
  * 출력 불가능한 제어 문자 33개 + 공백, 출력 가능한 문자 95개
  * 확장 아스키 : 부가적인 문자를 128개 추가할 수 있게 하는 부호
  * 확장 아스키는 서로 다른 프로그램이나 컴퓨터 사이에 교환 X
* 유니코드 : 다국어 처리를 위한 표준
  * UCS-2 (Universal Character Set 2)
  * UCS-4 (Universal Character Set 4)
  * 유니코드를 저장하는 변수의 크기를 정의
  * 유니코드 인코딩
    * UTF-8 (in web) : 1 Byte * 4
    * UTF-16 (in windows, java) : 2 Byte * 2
    * UTF-32 (in unix) : 4 Byte * 1
  * Python 인코딩
    * 2.x version (ASCII) => #-*-coding: utf-8 -*- (첫 줄에 명시)
    * 3.x version (유니코드) => UTF-8 (생략 가능)

# 문자열
* fixed lenght
* variable length
  * lenght controlled : java에서의 문자열
  * delimited : c에서의 문자열

* strlen() 함수 : '\0'을 만나면 '\0'제외 글자수 리턴
```python
def strlen(n):
    cnt = 0
    for i in n:
        if i == '\0':
            break
        cnt += 1
    return cnt

a = ['a', 'b', 'c', '\0']
print(strlen(a))
```

* 문자열 + 문자열 : 이어 붙이는 역할
* 문자열 * n : n만큼 문자열 반복
* 문자열은 `시퀀스 자료형` / `immutable` (값 변경 불가)
* 메소드 : replace() / split() / isalpha() / find()
* 문자열 뒤집기
  * s = s[::-1]
  * s = list(s) => s.reverse() => s = ''.join(s)
  ```python
    s = 'Reverse this strings'
    new = ''
    for i in range(len(s)-1, -1, -1):
        new += s[i]
    print(new)

    list_s = list(s)    # 리스트로 형 변환
    for idx in range(len(s) // 2):
        list_s[idx], list_s[-1-idx] = list_s[-1-idx], list_s[idx]
    print(''.join(list_s))
  ```

* 문자열 비교
  * == 연산자 : __eq__()를 호출 / 값 동일
  * is 연산자 : 값, 주소 동등

```python 
# 정수를 입력 받아 문자열로 변환하는 함수
def itoa(n):
    neg = False    # Flag : 음수면 Ture
    if n < 0:
        neg = True
        n = -n

    result = ''
    while n:
        n, remain = n // 10, n % 10
        result = chr(ord('0') + remain) + result
    
    if neg:
        return '-' + result
    else:
        return result

res = itoa(-1234)
print(res)
```

# 패턴 매칭
## 고지식한 패턴 검색 알고리즘 ( Brute Force)
* 문자열을 순회하면서 하나하나 비교하는 방식
```python
p = 'is'        # 찾는 부분
t = 'this is text'    # 전체 부분
m, n = len(p), len(t)

def bruteforce(p, t):
    i, j = 0, 0
    while j < m and i < n:
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m:       # 성공
        return i-m
    else:            # 실패
        return -1
```
``` python
def bruteforce2(p, t):
    m, n = len(p), len(t)
    for idx in range(n-m+1):
        for jdx in range(m):
            if p[jdx] != t[idx]:
                break
        else:   # 패턴이 매칭된 상태
            return idx
    else:
        return -1
```

## KMP 알고리즘
* 불일치가 발생한 앞 부분에 대해서 다시 비교하지 않고 수행
* 비교 실패한 부분을 반복되는 부분 뒤부터 비교 반복
  
## 보이어-무어 알고리즘
* 오른쪽에서 왼쪽으로 비교
* 패턴에서 일치하는 문자를 찾아서 그 문자와 비교
* 일치하는 문자가 없으면 길이만큼 이동
