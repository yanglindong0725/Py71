def counter(FIRST=0):
    cnt = [FIRST]

    def add_one():
        cnt[0] += 1
        return cnt[0]
    return add_one


num5 = counter(5)
num28 = counter(28)

print(num5())
print(num5())
print(num5())
print(num5())
print(num28())
print(num28())
print(num28())
print(num28())
print(num28())
print(num28())
