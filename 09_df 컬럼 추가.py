import pandas as pd

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

# BMI 컬럼 추가(몸무게/키(m))
df["BMI"] = df["weight"]/(df["height"]/100)

print(df)