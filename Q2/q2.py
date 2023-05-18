import numpy as np
from numpy import dot
from numpy.linalg import norm

#코싸인 유사도 계산하는 함수
def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

#2차원(3x6) Matrix 형태로 표현된 3개의 문clea서(Docs)
#1차원 Vector 형태의 질의(Query) 사이의 코사인 유사도 계산
Docs = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
Query = np.array([1,1,0,0,1,0])

print('docs1={0:.2f}'.format(cos_sim(Docs[0],Query)))
print('docs2={0:.2f}'.format(cos_sim(Docs[1],Query)))
print('docs3={0:.2f}'.format(cos_sim(Docs[2],Query)))
