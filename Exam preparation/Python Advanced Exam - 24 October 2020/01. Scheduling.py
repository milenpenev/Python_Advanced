jobs = [int(el) for el in input().split(", ")]
index = int(input())

wanted_job = jobs[index]

done_jobs = []

for i in range(len(jobs) - 1, -1, -1):
    if i == index:
        continue
    if jobs[i] <= wanted_job:
        current_job = jobs.pop(i)
        done_jobs.append(current_job)
print(sum(done_jobs)+wanted_job)
