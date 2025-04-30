# Measure time complexity (n logn ?)

"""
    The slowest version so far. I will be integrating constraints, indexing and memorization (dynamic programming)
    to speed the process
"""
def get_score(decision_variables):
    """The function to return score for given decision variables"""
    # Constant weights
    Ft = 20
    ps1 = 50
    ps2 = 20
    ps3 = 39
    ps4 = 8
    ps5 = 4

    # Scoring
    score = (60 - sum(decision_variables)) * Ft + (
        decision_variables[0] * ps1 + decision_variables[1] * ps2 + 
        decision_variables[2] * ps3 + decision_variables[3] * ps4 + 
        decision_variables[4] * ps5
        )
    return score

def RollOver(decision_variables):
    """Recursive function for solving Roll-over problem"""
    
    score = get_score(decision_variables)
    
    if decision_variables == [10, 10, 10, 10, 10]:
        return score, decision_variables
    
    decision_variables_optimized = decision_variables.copy()

    for i in range(len(decision_variables)):
        if decision_variables[i] != 10:
            decision_variables_copy = decision_variables.copy()
            decision_variables_copy[i] = 10

            score_from_branch, decision_variables_from_branch = RollOver(decision_variables_copy)
            if score <= score_from_branch:
                score = score_from_branch
                decision_variables_optimized = decision_variables_from_branch
    return score, decision_variables_optimized

score, variables = RollOver([0, 0, 0, 0, 0])

print("Final")
print(score, variables)
