import pandas as pd
import matplotlib.pyplot as plt

# 데이터프레임(df) 생성, 딕셔너리의 key는 속성을, value의 배열은 해당 속성의 값들을 의미한다.
df = pd.DataFrame(
    {
        "age": [
            21,
            35,
            58
        ],
        "weight": [
            67,
            86,
            79
        ],
        "height": [
            172,
            180,
            184
        ],
    }
)

df.plot() # 데이터를 그린다.(그래프)
# plt.show() # 그래프를 화면에 보여준다.(기본적으로 숫자로 된 속성값들만 보여준다)

df.plot.scatter(x="height", y="weight", alpha=0.5) # 데이터를 그린다.(산점도)
# plt.show() # 그래프를 화면에 보여준다.(기본적으로 숫자로 된 속성값들만 보여준다)

df.plot.box() # 데이터를 그린다.(박스 플롯)
# plt.show() # 그래프를 화면에 보여준다.(기본적으로 숫자로 된 속성값들만 보여준다)

df.plot.area(figsize=(12, 4), subplots=True) # 여러개로 나눠서 보여주기
plt.show()