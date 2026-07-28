A = input()
minus_list = A.split("-")
# minus_list = ['100', '40+50+74', '30+29', '45+43+11']

res = 0

for i in range(len(minus_list)):
    tmp = list(map(int, minus_list[i].split("+")))
    # tmp 값 = [100], [40, 50, 74], [30,28], [45, 43, 11]
    sumation = sum(tmp)
    minus_list[i] = sumation
    # minus_list 값 = [100, 164, 58, 99]

res += minus_list[0]
for i in range(1, len(minus_list)):
    res -= minus_list[i]
print(res)
