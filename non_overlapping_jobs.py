# Define the list of jobs with their start time, end time, and value
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

# Step 1: Sort jobs by their finishing times in non-decreasing order
jobs.sort(key=lambda job: job["end"])

# Step 2: Compute the p array - for each job i, find the last job j that doesn't overlap with i.
def find_previous_non_overlapping(jobs):
    p = [-1] * len(jobs)  # Initialize the p array with -1
    for i in range(len(jobs)):
        # Find the latest job that ends before the current job's start time
        for j in range(i - 1, -1, -1):
            if jobs[j]["end"] <= jobs[i]["start"]:
                p[i] = j
                break
    return p

# Step 3: Initialize the opt array and the b array (for backtracking)
def compute_opt_and_backtracking(jobs, p):
    n = len(jobs)
    opt = [0] * (n + 1)  # Initialize opt array with an extra slot for easier indexing
    b = ['N'] * n  # Initialize b array to track included jobs

    # Fill in the opt array using the recurrence relation
    for i in range(1, n + 1):
        job_value = jobs[i - 1]["value"]
        previous_opt = opt[p[i - 1] + 1] if p[i - 1] != -1 else 0

        # Check whether to include the current job in the optimal solution
        if opt[i - 1] >= job_value + previous_opt:
            opt[i] = opt[i - 1]
            b[i - 1] = 'N'
        else:
            opt[i] = job_value + previous_opt
            b[i - 1] = 'Y'

    return opt, b

# Step 4: Backtrack to find the selected jobs (recovery function)
def recover_selected_jobs(jobs, p, b):
    selected_jobs = []
    total_value = 0
    i = len(jobs)

    # Traverse the backtracking array to find the selected jobs
    while i > 0:
        if b[i - 1] == 'Y':  # If the job is included, add it to selected_jobs
            selected_jobs.append(jobs[i - 1])  # Append the job's details
            total_value += jobs[i - 1]["value"]  # Add the job's value
            i = p[i - 1] + 1  # Move to the previous non-overlapping job
        else:
            i -= 1  # Move to the previous job

    selected_jobs.reverse()  # Reverse to get jobs in the correct order
    return selected_jobs, total_value

# Combine all parts to solve the problem
p = find_previous_non_overlapping(jobs)  # Find the p array
opt, b = compute_opt_and_backtracking(jobs, p)  # Compute the opt and backtracking arrays
selected_jobs, max_value = recover_selected_jobs(jobs, p, b)  # Recover the selected jobs with values

# Output the results
print("Selected jobs with details:", selected_jobs)
print("Maximum value:", max_value)
