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

print(df) # 엑셀처럼 표 형태로 출력된다


# series 생성
s = pd.Series([22, 35, 58], name="나이")
print(s) # series는 단일 열이기에 열 레이블이 출력되지않는다.