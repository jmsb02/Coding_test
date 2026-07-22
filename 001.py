n = int(input())  # 5
numbers = list(input())  # 54321 -> ['5','4','3','2','1']
sum = 0

for i in range(len(numbers)):
    sum += int(numbers[i])
print(sum)
