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
```python
def pre_process(pattern):
    # 전처리를 위한 테이블을 작성 (LPS table longest prefix suffix)
    lps = [0] * len(pattern)
    j = 0   # lps를 만들기 위한 prefix index

    for i in range(1, len(pattern)):    # 0번째 자리는 패턴 확인 필요 X
        # prefix index 위치에 있는 문자와 비교
        if pattern[i] == pattern[j]:
            lps[i] = j + 1   # i 앞에 중복 패턴 존재
            j += 1            # j는 중복 글자 자리 수
        else:
            j = 0
            # 여기서 0으로 이동한 다음 prefix idx 비교를 한 번 더 해야함
            if pattern[i] == pattern[j]:
                lps[i] = j + 1
                j += 1
    
    return lps


def KMP(text, pattern):
    lps = pre_process(pattern)   # 전처리로 lps 테이블 생성

    i, j = 0, 0    # text idx, pattern idx
    while i < len(text):
        if pattern[j] == text[i]:    # 같은 문자라면
            # 다음 문자 비교 
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == len(pattern):    # pattern 전부 일치
            return i - j         # text 위치 리턴

    return -1         # 일치하는 문장 없는 경우

    
text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
print(KMP(text, pattern))
```
  
## 보이어-무어 알고리즘
* 오른쪽에서 왼쪽으로 비교
* 패턴에서 일치하는 문자를 찾아서 그 문자와 비교
* 일치하는 문자가 없으면 길이만큼 이동
```python
def pre_process(pattern):
    m = len(pattern)   # 패턴의 길이
    
    skip_table = dict()
    for i in range(m-1):
        skip_table[pattern[i]] = m - i - 1

    return skip_table


def boyer_moore(text, pattern):
    skip_table = pre_process(pattern)
    m = len(pattern)
    i = 0   # text idx

    while i <= len(text) - m:
        j = m - 1    # 뒤에서 비교
        k = i + (m - 1)  # 비교 시작 idx
        # 비교할 j가 남아있고, text와 pattern이 일치하면 그 다음 앞 글자 비교를 위해 인덱스 감소
        while j >= 0 and pattern[j] == text[k]:
            j -= 1
            k -= 1
        if j == -1:   # 일치
            return i
        
        # 일치X
        else:
            # i 비교할 시작 위치를 skip table에서 가져옴
            i += skip_table.get(text[i+m-1], m)
    return -1   # 일치 패턴 X
    
    
text = 'ABC ABCDAB ABCDABCDABDE'
pattern = 'ABCDABD'
print(boyer_moore(text, pattern))
```