

path = 'C:\\Users\\vdi-student\\Desktop\\Zajecia_Niedziela\\pliki-20221211T073145Z-001\\pliki\\rozliczenie.csv'

with open(path, 'r') as x:
    content = x.readlines()

print(content)

for i in range(1, len(content)):
    content[i] = content[i].split(',')

print(content)

total = 0
for i in range(1, len(content)):
    total += int(content[i][1])
print(total)
