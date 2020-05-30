def getImportance(employees, id):
    importance_hash = {}
    subordinates = {}
    for employee in employees:
        importance_hash[employee[0]]=  employee[1]
        if employee[0] not in subordinates:
            subordinates[employee[0]] = subordinates.get(employee[0], list()).extend(employee[2])


    return importance_hash, subordinates

if __name__ == '__main__':
    employees= [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
    id = 1
    print(getImportance(employees, id))