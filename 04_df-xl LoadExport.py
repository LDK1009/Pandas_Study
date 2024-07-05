import pandas as pd

# 엑셀 파일 불러오기(데이터프레임 형식으로 대입)
df = pd.read_csv("./assets/predictive_maintenance.csv")

# 
print(df)

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
# 엑셀 파일 내보내기(데이터프레임 형식으로 대입)
df.to_excel("./assets/df.xlsx", sheet_name="sheet1", index=False)
