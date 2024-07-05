import pandas as pd

# 데이터프레임(df) 생성, 딕셔너리의 key는 속성을, value의 배열은 해당 속성의 값들을 의미한다.
df = pd.DataFrame(
    {
        "이름": [
            "김동규",
            "이동규",
            "박동규",
        ],
        "나이": [
            21,
            35,
            58
        ],
        "성별": [
            "남자",
            "남자",
            "남자",
        ],
    }
)

# 특정 값 이상의 데이터만 추출
filter_data = df[df["나이"]>21]
print(filter_data)


# 특정 값들에 속하는 데이터만 추출
filter_data = df[df["나이"].isin([21, 35])] # 10대부터 30대까지
print(filter_data)


# 다중 조건
filter_data = df[(df["나이"]>21) & (df["이름"]=="이동규")] # 각 조건은 괄호로 감싼다.
print(filter_data)


# 속성값이 NaN인 값 제거
filter_data = df[df["나이"].notna()]
print(filter_data)

# 특정 문자열을 포함한 행만 추출
filter_data = df[df["이름"].str.contains("김")]
print(filter_data)