
## 숫자 백단위 콤마 넣기
def put_comma():
    digit = 12345
    digit = format(digit, ',')
    print(digit)

## 문자열 중간에 변수 끼워넣기 (문자열 포맷팅 formatting)

def str_formatting():  # f-string
    _str = '문자'
    a = f"문자 : {_str}:"

    num1 = 1.123
    b = f'f-string example1 : {num1:.0f}'# 소수점 자리수 표현  # 출처: https://blockdmask.tistory.com/534 [개발자 지망생]

    print(a,
          b)

def str_formatting2(): # 문자열 중간에 변수 넣기, 변수 형식 지정 방식
    number = 10.123
    day = '5'
    a = "I ate %d apples. so I was sick for %s days." % (number, day)
    b = "소수점 표현법 : %.1f" % (number)
    print(a, b)


def str_formatting3(): # 변수 이름 지정 방식
    ticker = "BTC"
    profit = ['1번값', '2번값']
    sold = ('익절매도 {0}, {1}, {2}'.format(ticker, profit[0], profit[1])) # 이 방식도 가능하다
    a = '나이: {age},  이름: {name}'.format(name = "이시영", age = 3 )
    b = "format example1 : {:.2f}".format(1.23456789)  # 출처: https: // blockdmask.tistory.com / 534[개발자지망생]
    print(sold, a, b)


## 파이썬 콘솔
    # *'_' 밑줄은 콘솔에서 마지막으로 계산된 값을 저장한다. 마지막 계산값이 2 일 때 .ex) _ + 3 = 5

## Escaping strings
    # * / n 줄바꿈

## 문자열 인덱싱
    # mycoin = "Bitcoin"
    # mycoin[0]
    # 'B'
    # 음수는 뒤에서부터

## 문자열 슬라이싱
    # mycoin[0:3][시작점: 마지막점]

## 문자열 인덱스 생략법
    # [:4] 맨 처음부터 4번째까지
    # [4:] 4번 째부터 맨 끝까지

## 문자열 메서드
    # https: // docs.python.org / ko / 3 / library / stdtypes.html
    # string-methods

## 리스트의 수정
    '''
    hold = ["btc_krw", "xrp_krw", "eth_krw"]
    hold[0] = "bch_krw"
    hold의 0번째 자료가 변경된다
    '''

## 리스트의 슬라이싱은 문자열 슬라이싱과 같다

## 리스트의 삽입

### 1. 리스트의 마지막에 추가하는 방법 append
    '''
    portfolio = []
    portfolio.append("BTC")
    portfolio.append("ETH")
    portfolio.append("XRP")'''

### 2. 리스트의 특정 위치에 추가하는 방법 insert
    ''' 리스트의 중간에 삽입할 때 기존의 자료는 뒤로 밀린다.
    변수명.insert(1, "DASH")'''
def add_list():
    a = list([1, 2, 3, 4])
    a.insert(1, 'BTC')
    print(a)


### 리스트 데이터의 삭제 del
    '''del 변수명[1] 리스트를 지울 때 
    portfolio.del '''

### 최대값 / 최소값 / 평균값
def get_max_min():
    ripple_close = [503, 505, 508, 501, 530]
    print(max(ripple_close))
    print(min(ripple_close))
    # 파이썬에는 평균값을 직접 계산해주는 함수는 없습니다.

def get_avg(): # 평균값
    a = [1, 2, 3, 4]
    average = sum(a) / len(a)
    print(average)

### 튜플  ( )
    '''튜플은 한번 자료를 넣으면 수정 할 수 없다
        튜플은 리스트보다 메모리를 더 적게 사용한다
        튜플은 소괄호를 사용한다
        튜플의 인덱싱과 슬라이싱은 '변수명[]' 대괄호를 사용한다'''

### 딕셔너리 (dict)  {중괄호}
    '''순서가 없는 자료구조 딕셔너리는 두 값의 관계를 저장하는 데 효과적이다
        key와 value로 구성
        prices = {'BTC': 8300000, 'XRP': 514}'''

### 딕셔너리 인덱싱
    ''' key 값을 이용한다 딕변수[key값] '''

### 딕셔너리에 데이터 추가하기
def add_dict():
    prices = {'BTC': 8300000, 'XRP': 514}
    prices['ETH'] = 600000
    print(prices)


### 딕셔너리 데이터 수정
    # 단일 수정은 키로 접근하여 값을 할당하면 됩니다
    """ a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
    a['alice'] = 5
    출력 {'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}"""

    # 여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
    ''' a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30} 
        a.update({'bob':99, 'tony':99, 'kim': 30}) 
        출력값 : {'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}'''

### 딕셔너리 자료 삭제
"""
prices = {'BTC': 8300000, 'XRP': 514}
del prices['XRP']
print(prices)

### 딕셔너리에서 key 값만 얻기

prices = {"BTC": 8300000, "XRP": 514, "ETH": 600000}
prices.keys()

# 리스트 타입으로 변경해서 사용하기

    list(prices.keys())


### 딕셔너리로부터 value 값 얻기

prices = {"BTC": 8300000, "XRP": 514, "ETH": 600000}
prices.values()


### 조건문 if / else

if 조건:
    문장1
else:
    문장2

### 반복문
for new변수 in 자료구조:
    코드

for any in ['가', '나', '다', '라']:
    print(any)

#### for 와 range

for num in range(1, 11):
    print(num)
    * 끝자리수의 - 1까지임으로 10까지 포함

* 오프셋값(범위 건너뛰기) range(시작값, 끝 값, 오프셋)
range(1, 11, 3)
결과값은
1, 4, 7, 10

#### for 와 dict

cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker in cur_price:
    print(ticker)
    * 키
값들만
바인딩

cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker, price in cur_price.items():
    print(ticker, price)
    * key와
value
각각
바인딩

cur_price = {"BTC": 9010000, "XRP": 511, "DASH": 360000}
for ticker in cur_price:
    print(ticker, cur_price[ticker])
    * Line3: 바인딩
된
ticker값들이
key가
되어
value를
불러온다

#### 반복문과 IF

ripple = [511, 516, 508, 505, 503]
for close in ripple:
    if
close >= 510:
print(close)

### while 문
*
for 문은 주로 자료구조와 함께 사용, 반복 횟수가 정해져 있는 경우
*
while 문은 계속 반복해야 하거나 반복할 횟수가 명확하지 않을 때

while 조건문:
    수행문1
    수행문2
    수행문3
------------------------
num = 1
while True:
    print(num)
    num = num + 1

### while 문과 break 문
*while문을
중지하고
싶을
때
'분기문'
과
'break'
구문을
사용
num = 1
while True:
    if num == 100:
        break
    print(num)
    num = num + 1

* continue 문은
반복문의
처음으로
돌아간다

num = 1
while True:
    num = num + 1
    if num < 10:
        continue
    print(num)


### 함수 function 정의

def name(parameter):
    문장1
    문장2
    return


마지막으로
return이라는
키워드를
통해서
함수
내의
값을
함수
외부로
전달할
수
있습니다.


def hap(a, b):
    ret = a + b
    return ret


*함수가 종료될 때 함수 내에서 생성된 모든 변수는 소멸되고 바인딩되지 않는 객체 역시 모두 소멸됩니다

### 모듈 import 방법
1)  import 모듈  # 호출시 모듈명.함수명
2)  import 모듈 as 새이름

3)  from 모듈 import 함수  # 호출시 모듈명 필요없음, 함수명 중복시 오류
4)  from 모듈 import *  # 모든 함수 들여오기

### datetime 모듈
datetime.now: 일자
시간
출력

import datetime

now = datetime.datetime.now()  # datetime모듈의 datetime클래스로부터 now함수 호출
print(now)

datetime.timedelta: 날짜와
시간의
계산

print(now + datetime.timedelta(hours=10))
print(now - datetime.timedelta(minutes=30))

### requests 모듈

import requests

resp = requests.get("https://api.bithumb.com/public/ticker/BTC")
print(resp)  # <Response [200]> 정상 수신했다는 뜻
print(resp.content)  # 내용 다 나옴

### class  클래스

클래스 안의 함수를 method 라 부른다.
클래스 안에 위치하는 함수(메서드)는 첫 번째 인자로 self를 사용합니다.

* 사용법: 클래스를 만들고 클래스 내부 메서드를 정의한다
        클래스 밖에서 클래스를 담을 변수를 만들고 그 안에 클래스를
넣는다
클래스가
담긴
'변수.메서드(인수)'
의
형식으로
사용한다


class 붕어빵틀:
    def 팥소넣기(self, 팥소):
        self.팥소변수 = 팥소  # 붕어빵틀 안에 '팥소'의 변수를 만들어 인수로 팥소를 담는다


붕어빵1 = 붕어빵틀()
붕어빵2 = 붕어빵틀()

붕어빵틀.팥소넣기(붕어빵1, '초코맛팥소')

붕어빵2.팥소넣기('호두팥소')  # 간편한 방법

print(붕어빵1.팥소변수, 붕어빵2.팥소변수)

### initializer 초기화자

클래스
내
메서드의
인수값을
미리
넣어놓을
수
있다
(__init__)
이라는
메서드로
클래스가
객체로(변수의
값으로) 생성된
후
자동으로
호출된다


class 붕어빵틀:
    def __init__(self):
        self.팥소 = "초코맛팥소"


붕어빵1 = 붕어빵틀()
print(붕어빵1.팥소)

### 클래스 속성 참조 순서
클래스에는
데이터와
메서드가
있다
데이터와
메서드를
통틀어
'속성'
이라고
한다

### 변수값 복사 방법
기존의
변수명을
가져와
생성자를
달아준다
변수값이
딕셔너리라면,
 _a = dict(기존변수명)"""

str_formatting3()
