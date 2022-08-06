def solution(money, stocks):

    DP = [[0 for _ in range(money+1)] for _ in range(len(stocks)+1)]

    for i in range(len(stocks)+1):
        for j in range(money+1):
            if stocks[i-1][1] <= j: 
                DP[i][j] = max(stocks[i-1][0] + DP[i-1][j-stocks[i-1][1]],  DP[i-1][j]) 
            else: 
                DP[i][j] = DP[i-1][j] 


    maxVal = 0

    for i in range(len(DP)):
        maxVal = max(maxVal, DP[i][-1])


    return maxVal
