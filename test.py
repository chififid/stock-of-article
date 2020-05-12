class Отец():
    def __init__(self, ключ, просмотры):
        self.ключ = ключ
        self.просмотры = просмотры

a0 = Отец(1, 1000)
a1 = Отец(2, 1000)
a2 = Отец(3, 1000)
a3 = Отец(4, 1000)
a4 = Отец(1, 4000)
a5 = Отец(2, 4000)
a6 = Отец(3, 4000)
a7 = Отец(4, 4000)
a8 = Отец(1, 3000)
a9 = Отец(2, 3000)
a10 = Отец(3, 3000)
a11 = Отец(4, 3000)
a12 = Отец(1, 2000)
a13 = Отец(2, 2000)
a14 = Отец(3, 2000)
a15 = Отец(4, 2000)

before = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15]
answer = []
other = []
favorite = [1, 3]
after = []
for i in before:
    if i.ключ in favorite:
        answer.append(i)
    else:
        other.append(i)

for i in range(0, len(before)):
    try:
        if i / 3 == 0:
            after.append(other[i/3])
        else:
            after.append(answer[i - i // 3])
    except:
        after.append(other[i])

print(after)