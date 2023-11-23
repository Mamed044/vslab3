import random

def printList(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print(lst[i][j], end='    ')
        print()

p = 1
n = 4
m = 4
a = []

for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(-8, -1))  
print("Oluşturulan Matris:")
printList(a)
print()

for j in range(m): 
    product = 1
    for i in range(n): 
        if a[i][j] < 0:  
            product *= a[i][j]
    print(f"Sütun {j + 1} Negatif Elemanlar Çarp: {product}")