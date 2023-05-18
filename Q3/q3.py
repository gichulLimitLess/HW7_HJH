#특정 컬럼 접근
#형식: 데이터프레임 [컬럼 명]
#마스킹: 불리언 로직(True, False) 결과를 데이터 프레임이 입력

#단가(unit price)와 개수(number)로 이루어진 데이터 프레임 생성 및 출력
#단가와 개수를 곱한 총 가격(total price)이 추가된 데이터 프레임 생성 및 출력
#총 가격이 가장 비싼 가계순으로 2개 출력

import pandas as pd
import numpy as np

data = np.array([[1000,25],[280,120],[900,30]])

df = pd.DataFrame(data, index=['store1', 'store2', 'store3'], columns=['unit price', 'number'])
print(df)

#numpy에서 기준 축을 지정하여 접근 가능
#기준 축을 기준으로 각 행이 numpy array로 취급
#axis 값을 1로 주는 걸 잊지 말자!
df['total price']=df['unit price']*df['number']
print(df)

df_sorted = df.sort_values('total price', ascending=False)
df_sorted_2 = df_sorted.head(2)
print(df_sorted_2)

