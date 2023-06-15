l1 = [1, 2, 3, 4, 5]

l2 = [n+1 for n in l1]

print(l1)
print(l2)

l3 = [n*2 for n in range(1, 5)]
print(l3)

l4 = [n*2 for n in range(1, 5) if n%2==0]
print(l4)