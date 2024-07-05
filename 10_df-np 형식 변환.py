import pandas as pd

# df > np 1
## df의 values 속성은 얕은 복사를 수행합니다.(array 값을 변경하면 원본(df)도 변경됩니다.)
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['A', 'B', 'C']) # DataFrame 생성
array = df.values # 2차원 NumPy 배열로 변환
print(array)

# df > np 2
## df의 to_numpy는 기본적으로 얕은 복사를 수행하지만 속성값(copy=True) 설정 시 깊은 복사를 수행합니다.
## 얕은 복사 : array 값을 변경하면 원본(df)도 변경됩니다.)
## 깊은 복사 : array 값을 변경해도 원본(df)은 변경되지 않습니다.

# array = df.to_numpy() # 얕은 복사(array 값을 변경하면 원본(df)도 변경됩니다.)
array = df.to_numpy(copy=True) # 깊은 복사(array 값을 변경해도 원본(df)은 변경되지 않습니다.)
print(array)

# np > df 1
# NumPy 배열을 DataFrame으로 변환
df = pd.DataFrame(array)
