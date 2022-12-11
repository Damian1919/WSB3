# ZADANIE 2

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
avarage = total / (len(content)-1)
print (round(avarage,3))

# ZADANIE 3

x = 0
for i in range(1, len(content)):
    content[i][4] = content[i][4].replace('\n', '')
    if content[i][3] == 'k' and content[i][4] == 't':
            x += 1
def fizzBuzz (x):
    if (x%5 == 0):

