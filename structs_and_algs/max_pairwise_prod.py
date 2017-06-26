a_upper_bound = 10**5
n = int(input())
a = [int(x) for x in input().split()]

assert(len(a) == n)
assert(n>=2)
assert(n<=(2*(a_upper_bound)))

for elem in a:
    assert(elem>=0)
    assert(elem<=a_upper_bound)

max_index = 0
max1 = 0
for i in range(0, n):
    if a[i] > max1:
        max1 = a[i]
        max_index = i

max2 = 0
for i in range(0, n):
    if a[i] > max2 and max_index != i:
        max2 = a[i]

result = max1*max2


print(result)
