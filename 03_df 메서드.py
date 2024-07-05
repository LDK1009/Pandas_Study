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
# series 생성
s = pd.Series([22, 35, 58], name="나이")


# 메서드
# df의 series 별 최대값
print("# 데이터프레임의 시리즈 별 최대값")
print(df.max())

# series의 최대값
print("# series의 최대값")
a = df["나이"].max()
print(a)
a = s.max()
print(a)


# df의 기본 통계값
print("# 데이터 프레임의 기본 통계값")
print(df.describe())


# df의 출력할 행 제한하기
print("# df의 출력할 행 제한하기")
h = df.head(2) # 첫 2행만 가져온다
t = df.head(2) # 마지막 2행만 가져온다
print(h)
print(t)

# df의 행 개수 알아내기
print("# 행 개수 알아내기")
print(df.shape) # >> (3,3) / 3행 3열을 나타낸다

# series의 행 개수 알아내기
print("# series의 행 개수 알아내기")
print(df["나이"].shape) # >> (3,) / 3행 1열을 나타낸다.
