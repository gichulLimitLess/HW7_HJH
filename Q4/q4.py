#gender2.csv를 pd.read_csv()로 읽어오기
#총 인구수(Total), 남성 총 인구수(Male), 여성 총 인구수(Female) columns을 선택하여 new DataFrame을 생성
#columns의 이름을 다음과 같이 변경
#(->총 인구수: Total, 남 총 인구수: Male, 여 총 인구수: Female)
#최종 DataFrame을 전체 출력

#총 인구수: 1/ 남 총 인구수: 6 /여 총 인구수: 11

import pandas as pd
import numpy as np

specific_col = ['2022년_계_총인구수','2022년_남_총인구수','2022년_여_총인구수']

df = pd.read_csv('gender2.csv', index_col='행정구역', encoding='EUC-KR')
selected_df = df[specific_col]


selected_df.columns = ['Total', 'Male', 'Female']
print(selected_df)
