# Problem Set 0
# Name: kyungil.Bhang
# Collaborators: None
# Time Spent: 0:10
import numpy # 로그 계산을 위한 라이브러리 로드

# 1. 사용자로부터 x와 y 입력받기 (input은 문자열이므로 float형태로 형변환 필수)
x = float(input("Enter number x: "))
y = float(input("Enter number y: "))

# 2. x의 y제곱 계산 후 출력
print("X**y =", x ** y)

# 3. x의 밑이 2인 로그 값 계산 후 출력
print("log(x) =", int(numpy.log2(x)))

