# Algorithm

## [알고리즘 확인](#algorithm)
## [헷갈리는 Python 문법](#python)


## Algorithm
- 에라토스테네스의 체
    - 소수 찾는 알고리즘
    - set과 range를 이용해서 짧게 구현하자.
    
    
    ```python
    n = int(input())
    numbers = set(range(2, n+1))
    for i in range(n):
        if i in numbers:
            numbers -= set(range(i*2, n+1, i))
    print(numbers)
    ```


- 이진탐색 (Bynary Search)
    
    
    ```python
    while start <= end:
        mid = (start + end)//2
        if mid == target:
            return mid
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1
    ```
    
    
    [x] [2805 나무자르기](https://www.acmicpc.net/problem/2805)    

- 최대공약수와 최대공배수
    - 유클리드 호제법
        - 두 양의 정수 a, b (a>b)에 대해 a = bq + r (0 <= r < b)일 때
        - a, b의 최대공약수는 b, r의 최대 공약수와 같다.
        - 즉, gcd(a, b) = gcd(b, r)
        - r = 0이라면 a, b의 최대공약수는 b이다.
        
        
        ```python
        def get_gcd(a, b):
            while min(a,b):
                a, b = max(a, b) % min(a, b), min(a, b)
        
        a, b = map(int, input().split()
        gcd = get_gcd(a, b)
        lcm = a*b // gcd
        print(gcd, lcm)
        ```
        

## Python
- print의 옵션
    - separation: 구분자
        - 특정 문자로 구분하여 출력한다.
    
    
        ```python
        print('H','i', sep=':)')
        # H:)i 출력됨
        ```
    
    
    - end
        - print문의 마지막 글자를 설정한다.
        - 기본 값은 '\n'이다. 이를 바꾸는 방법이다.
        
        
        ```python
        print("Hello", end=" World")
        print(" Python")
        #Hello World Python으로 출력됨
        ```
        
        
    - format
        - 특정 서식에 따라 문자를 출력할 수 있다.
        - print()보다 실행속도면에 좋은 성능을 보인다.
        - f.format은 python 3.6 이상에서 지원한다.
        - 이외에는 str.format으로 사용한다.
        - [블로그](https://zest1923.tistory.com/17)
        
        
        ```python
        name = input()
        print (f'Hello {name}')
        ```

- object 값 출력하기
    - [1259번 팰린드롬수](https://github.com/JIWON1923/Algorithm/blob/master/BasicLevel/Class2/1259_palindrome.py) 를 풀며, reversed object와 str을 비교해야했다. 이를 해결하기 위해 join()을 이용하여 object를 str로 변경하여 풀 수 있었다.

- int형 리스트 출력하기
    - 대문자, 쉼표 없이 숫자만 출력하고 싶을 때
    - join과 repr을 사용한다.
    
    
    ```python
    result = [1, 2, 3, 4]
    print(' '.join(repr(i) for i in result))
    ```
    
    - repr : 문자열로 변환해줌
    - join : 해당 문자열을 붙여 출력
    - 즉, result의 원소를 문자열로 바꾼 후 ' '로 연결해서 출력하라는 명령!!
