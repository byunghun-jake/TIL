# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램 작성

def solution():
    n = int(input())
    answer = 0

    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if '3' in f"{h}{m}{s}":
                    answer += 1
    print(answer)

solution()