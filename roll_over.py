# Measure time complexity (n logn ?)

"""
    The slowest version so far. I will be integrating constraints, indexing and memorization (dynamic programming)
    to speed the process
"""
def get_score(decision_variables):
    """The function to return score for given decision variables"""
    # Constant weights
    Ft = 20
    ps1 = 5
    ps2 = 20
    ps3 = 93
    ps4 = 8
    ps5 = 9

    # Scoring
    score = (60 - sum(decision_variables)) * Ft + (
        decision_variables[0] * ps1 + decision_variables[1] * ps2 + 
        decision_variables[2] * ps3 + decision_variables[3] * ps4 + 
        decision_variables[4] * ps5
        )
    return score

def RollOverSlow(decision_variables):
    """Recursive function for solving Roll-over problem"""
    
    score = get_score(decision_variables)
    
    if decision_variables == [10, 10, 10, 10, 10]:
        return score, decision_variables
    
    decision_variables_optimized = decision_variables.copy()

    for i in range(len(decision_variables)):
        if decision_variables[i] != 10:
            decision_variables_copy = decision_variables.copy()
            decision_variables_copy[i] = 10

            score_from_branch, decision_variables_from_branch = RollOverSlow(decision_variables_copy)
            if score <= score_from_branch:
                score = score_from_branch
                decision_variables_optimized = decision_variables_from_branch
            
    return score, decision_variables_optimized


def RollOverIndexing(decision_variables, idxs = [0, 1, 2, 3, 4]):
    """
    I didn't check if this really works faster. I believe it should not be so different. The reason is the use of 
    remove function that actually implements looping.
    """
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
        if score <= score_from_branch:
            score = score_from_branch
            decision_variables_optimized = decision_variables_from_branch
    return score, decision_variables_optimized



if __name__ == "__main__":
    score, variables = RollOverSlow([0, 0, 0, 0, 0])

    print("First version of RollOver solution:")
    print(score, variables)

    score, variables = RollOverIndexing([0, 0, 0, 0, 0])

    print("RollOver solution with Indexing:")
    print(score, variables)

