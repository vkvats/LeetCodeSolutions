def average(salary):
    if len(salary) < 2:
        return 0
    sum_ = sum(salary)
    min_, max_ = min(salary), max(salary)
    return (sum_ - (min_ + max_))/ (len(salary) - 2)


import numpy as np
def average_np(salary):
    np_array = np.array(salary)
    return np.mean(np.sort(np_array)[1:-1])

if __name__ == '__main__':
    salary = [4000,3000,1000,2000]
    print(average_np(salary))