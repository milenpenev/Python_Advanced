nums = input().split()

n = int(nums[0])
m = int(nums[1])


n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(input())
for _ in range(m):
    m_set.add(input())
repeat = n_set.intersection(m_set)

print('\n'.join(repeat))