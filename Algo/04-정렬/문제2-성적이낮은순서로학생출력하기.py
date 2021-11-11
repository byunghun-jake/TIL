N = int(input())
students = []

for _ in range(N):
    name, score = input().split()
    score = int(score)
    students.append((name, score))

students.sort(key=lambda student: student[1])
for s in students:
    print(s[0], end=" ")