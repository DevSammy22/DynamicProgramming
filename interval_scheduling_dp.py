# totally mine
jobs = [
    {"start": 0, "end": 6, "value": 5},
    {"start": 1, "end": 4, "value": 6},
    {"start": 3, "end": 5, "value": 5},
    {"start": 3, "end": 8, "value": 8},
    {"start": 4, "end": 7, "value": 3},
    {"start": 5, "end": 9, "value": 4},
    {"start": 6, "end": 10, "value": 11},
    {"start": 8, "end": 11, "value": 2}
]

jobs.sort(key=lambda job: job["end"])


def interval_scheduling_dp(jobs):
    n = len(jobs)
    p = [-1] * n

    for i in range(n):
        for j in range(i - 1, -1, -1):
            if jobs[j]["end"] <= jobs[i]["start"]:
                p[i] = j
                break

    return p


p = interval_scheduling_dp(jobs)
n = len(jobs)
opt = [0] * (n + 1)
b = ["N"] * (n)

for i in range(1, (n + 1)):
    if p[i - 1] != -1:
        prev_job = opt[p[i - 1] + 1]
    else:
        prev_job = 0
    if opt[i - 1] >= (jobs[i - 1]["value"] + prev_job):
        opt[i] = opt[i - 1]
        b[i - 1] = "N"
    else:
        opt[i] = jobs[i - 1]["value"] + prev_job
        b[i - 1] = "Y"

i = len(jobs)
selected_jobs = []

while i > 0:
    if b[i - 1] == "Y":
        selected_jobs.append(i - 1)
        i = p[i - 1] + 1
    else:
        # b[i - 1] = "N"
        i = i - 1

selected_jobs.reverse()

print("Indices of selected job: ", selected_jobs)
print("Maximum value the job selected: ", opt[len(jobs)])





