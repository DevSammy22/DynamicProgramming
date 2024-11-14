#totally mine
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

jobs.sort(key=lambda job:job["end"])
def compute_non_overlapping_jobs(jobs):
    n = len(jobs)
    p = [-1] * n

    for i in range(n):
        for j in range(i-1, -1, -1):
            if jobs[j]["end"] <= jobs[i]["start"]:
                p[i] = j
                break
    return p

def find_optimal(jobs, p):
    n = len(jobs)
    opt = [0] * (n + 1)
    b = ["N"] * (n)

    for i in range(1, (n+1)):
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

    return opt, b
def recover_optimal_solution(jobs, p, b):
    i = len(jobs)
    selected_jobs = []
    selected_jobs_value = []

    while i > 0:
        if b[i - 1] == "Y":
            selected_jobs.append(i - 1)
            selected_jobs_value.append(jobs[i - 1]["value"])
            i = p[i - 1] + 1
        else:
            #b[i - 1] = "N"
            i = i - 1
    selected_jobs.reverse()
    selected_jobs_value.reverse()
    return selected_jobs, selected_jobs_value

def interval_scheduling(jobs):
    p = compute_non_overlapping_jobs(jobs)
    opt, b = find_optimal(jobs, p)
    select_jobs_index, selected_jobs_value = recover_optimal_solution(jobs, p, b)
    max_value = opt[len(jobs)]

    return select_jobs_index, selected_jobs_value, max_value

p = compute_non_overlapping_jobs(jobs)
opt, b = find_optimal(jobs, p)
select_jobs_index, selected_jobs_value = recover_optimal_solution(jobs, p, b)
max_value = opt[len(jobs)]

print("Indices of selected job: ", select_jobs_index)
print("values of selected job: ", selected_jobs_value)
print("Maximum value the job selected:, ", max_value)





