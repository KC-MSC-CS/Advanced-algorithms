# A class to store job details. Each job has an identifier,
# a deadline, and profit associated with it.
class Job:
    def __init__(self, taskID, deadline, profit):
        self.taskID = taskID
        self.deadline = deadline
        self.profit = profit
 
 
# Function to schedule jobs to maximize profit
def scheduleJobs(jobs, T):
 
    # stores the maximum profit that can be earned by scheduling jobs
    profit = 0
 
    # list to store used and unused slots info
    slot = [-1] * T
 
    # arrange the jobs in decreasing order of their profits
    jobs.sort(key=lambda x: x.profit, reverse=True)
 
    # consider each job in decreasing order of their profits
    for job in jobs:
        # search for the next free slot and map the task to that slot
        for j in reversed(range(job.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = job.taskID
                profit += job.profit
                break
 
    # print the scheduled jobs
    print("The scheduled jobs are", list(filter(lambda x: x != -1, slot)))
 
    # print total profit that can be earned
    print("The total profit earned is", profit)
 
 
if __name__ == '__main__':
    # List of given jobs. Each job has an identifier, a deadline, and
    # profit associated with it
    
    jobs = []
    n = int(input("Number of Jobs : "))
    for i in range(n):
        jobName = (input(f"Enter {i + 1} job name : "))
        jobDeadLine = int(input(f"Enter {i + 1} job Deadline : "))
        jobProfit = int(input(f"Enter {i + 1} job Profit : "))
        jobs.append(Job(jobName, jobDeadLine, jobProfit))
        print("")
 
    # stores the maximum deadline that can be associated with a job
    T = int(input(f"Maximum deadline that can be associated with a job : "))
 
    # schedule jobs and calculate the maximum profit
    scheduleJobs(jobs, T)