import pandas as pd
''' 데이터프레임을 for 반복문 돌리기'''  #  https://ponyozzang.tistory.com/609


df = pd.DataFrame({'age': [24, 42], 'state': ['NY', 'CA'], 'point': [64, 92]},
                  index=['Alice', 'Bob'])


# iteritems()를 사용하면 하나의 열씩 컬럼명과 같이 값을 더블 형태로 취득합니다.

    for column_name, item in df.iteritems():
        print(type(column_name))
        print(column_name)
        print('~~~~~~')

        print(type(item))
        print(item)
        print('------')

        print(item['Alice'])
        print(item[0])
        print(item.Alice)
        print('======\n')


# 1행 선택

    # iterrows()
    for index, row in df.iterrows():
        print(type(index))
        print(index)
        print('~~~~~~')

        print(type(row))
        print(row)
        print('------')

        print(row['point'])
        print(row[2])
        print(row.point)
        print('======\n')


# 특정 컬럼 출력

    for age in df['age']:
        print(age)

# 다중 컬럼 for 문

    for age, point in zip(df['age'], df['point']):
        print(age, point)