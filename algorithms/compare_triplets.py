def compareTriplets(a, b):
    a_score = 0
    b_score = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            a_score +=1
        elif b[i] > a[i]:
            b_score += 1
    return [a_score, b_score]