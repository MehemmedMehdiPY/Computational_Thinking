"""
---------- DESCRIPTION ----------

The code to check the performance of 4 variants of Roll-over solutions.

Results:
    Roll-over slow: 7.471227007999914
    Roll-over indexing: 6.754745763000301
    Roll-over memorization V1: 1.6611088949998702
    Roll-over memorization V2: 1.4664391030000843
"""



from timeit import timeit

rolloverslow = """def get_score(decision_variables):
    Ft = 20
    ps1 = 5
    ps2 = 2
    ps3 = 5
    ps4 = 839
    ps5 = 9
    score = (60 - sum(decision_variables)) * Ft + (
        decision_variables[0] * ps1 + decision_variables[1] * ps2 + 
        decision_variables[2] * ps3 + decision_variables[3] * ps4 + 
        decision_variables[4] * ps5
        )
    return score

def RollOverSlow(decision_variables):
    score = get_score(decision_variables)
    
    if decision_variables == [10, 10, 10, 10, 10]:
        return score, decision_variables
    
    decision_variables_optimized = decision_variables.copy()

    for i in range(len(decision_variables)):
        if decision_variables[i] != 10:
            decision_variables_copy = decision_variables.copy()
            decision_variables_copy[i] = 10

            score_from_branch, decision_variables_from_branch = RollOverSlow(decision_variables_copy)
            if sum(decision_variables_optimized) < 20 or score <= score_from_branch:
                score = score_from_branch
                decision_variables_optimized = decision_variables_from_branch
            
    return score, decision_variables_optimized

RollOverSlow([0, 0, 0, 0, 0])"""

rolloverindexing = """def get_score(decision_variables):
    Ft = 20
    ps1 = 5
    ps2 = 2
    ps3 = 5
    ps4 = 839
    ps5 = 9
    score = (60 - sum(decision_variables)) * Ft + (
        decision_variables[0] * ps1 + decision_variables[1] * ps2 + 
        decision_variables[2] * ps3 + decision_variables[3] * ps4 + 
        decision_variables[4] * ps5
        )
    return score

def RollOverIndexing(decision_variables, idxs = [0, 1, 2, 3, 4], count = 0):
    score = get_score(decision_variables)
    
    if decision_variables == [10, 10, 10, 10, 10]:
        return score, decision_variables
    
    decision_variables_optimized = decision_variables.copy()

    for idx in idxs:
        decision_variables_copy = decision_variables.copy()
        decision_variables_copy[idx] = 10

        idxs_copy = idxs.copy()
        idxs_copy.remove(idx)

        score_from_branch, decision_variables_from_branch = RollOverIndexing(decision_variables_copy, idxs_copy)
        if sum(decision_variables_optimized) < 20 or score <= score_from_branch:
            score = score_from_branch
            decision_variables_optimized = decision_variables_from_branch
    return score, decision_variables_optimized

RollOverIndexing([0, 0, 0, 0, 0])
"""

rollovermemov1 = """def get_score(decision_variables):
    Ft = 20
    ps1 = 5
    ps2 = 2
    ps3 = 5
    ps4 = 839
    ps5 = 9
    score = (60 - sum(decision_variables)) * Ft + (
        decision_variables[0] * ps1 + decision_variables[1] * ps2 + 
        decision_variables[2] * ps3 + decision_variables[3] * ps4 + 
        decision_variables[4] * ps5
        )
    return score

def RollOverMemoV1(decision_variables, idxs = [0, 1, 2, 3, 4], memo = {}):
    decision_variables_tuple = tuple(decision_variables)
    if decision_variables_tuple in memo.keys():
        return memo[decision_variables_tuple], decision_variables

    score = get_score(decision_variables)
    
    if decision_variables_tuple == (10, 10, 10, 10, 10):
        memo[decision_variables_tuple] = score
        return score, decision_variables
    
    decision_variables_optimized = decision_variables.copy()
    memo[decision_variables_tuple] = score

    for idx in idxs:
        decision_variables_copy = decision_variables.copy()
        decision_variables_copy[idx] = 10

        idxs_copy = idxs.copy()
        idxs_copy.remove(idx)

        score_from_branch, decision_variables_from_branch = RollOverMemoV1(decision_variables_copy, idxs_copy, memo=memo)

        if sum(decision_variables_optimized) < 20 or score <= score_from_branch:
            score = score_from_branch
            decision_variables_optimized = decision_variables_from_branch
    return score, decision_variables_optimized

RollOverMemoV1([0, 0, 0, 0, 0])    
"""

rollovermemov2 = """def get_score(decision_variables):
    Ft = 20
    ps1 = 5
    ps2 = 2
    ps3 = 5
    ps4 = 839
    ps5 = 9
    score = (60 - sum(decision_variables)) * Ft + (
        decision_variables[0] * ps1 + decision_variables[1] * ps2 + 
        decision_variables[2] * ps3 + decision_variables[3] * ps4 + 
        decision_variables[4] * ps5
        )
    return score

def RollOverMemoV2(decision_variables, idxs = [0, 1, 2, 3, 4], memo = {}):
    score = get_score(decision_variables)
    
    decision_variables_tuple = tuple(decision_variables)
    if decision_variables_tuple == (10, 10, 10, 10, 10):
        memo[decision_variables_tuple] = score
        return score, decision_variables
    
    decision_variables_optimized = decision_variables.copy()
    memo[decision_variables_tuple] = score

    for idx in idxs:
        decision_variables_copy = decision_variables.copy()
        decision_variables_copy[idx] = 10
        decision_variables_copy_tuple = tuple(decision_variables_copy)

        idxs_copy = idxs.copy()
        idxs_copy.remove(idx)

        if decision_variables_copy_tuple not in memo.keys():
            score_from_branch, decision_variables_from_branch = RollOverMemoV2(decision_variables_copy, idxs_copy, memo=memo)
        
        else:
            score_from_branch, decision_variables_from_branch = memo[decision_variables_copy_tuple], decision_variables_copy

        if sum(decision_variables_optimized) < 20 or score <= score_from_branch:
            score = score_from_branch
            decision_variables_optimized = decision_variables_from_branch
    return score, decision_variables_optimized

RollOverMemoV2([0, 0, 0, 0, 0])
"""

number = 10000
print("Roll-over slow:", timeit(rolloverslow, number=number))
print("Roll-over indexing:", timeit(rolloverindexing, number=number))
print("Roll-over memorization V1:", timeit(rollovermemov1, number=number))
print("Roll-over memorization V2:", timeit(rollovermemov2, number=number))