# Algorithm

## [알고리즘 확인](#algorithm)
## [헷갈리는 Python 문법](#python)


## Algorithm
- 에라토스테네스의 체
    - 소수 찾는 알고리즘
    - set과 range를 이용해서 짧게 구현하자.
    
    
    ```python
    n = int(input())
    number = set(range(2, n+1))
    for i in number:
        number -= set(range(i*2, n+1, i))
    print(number)
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
