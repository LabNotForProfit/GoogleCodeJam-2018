# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1C - Problem C. Ant Stack
# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8
#
# Time:  O(N * K)
# Space: O(K)
#

def get_upper_bound():
    MAX_W = 10**9
    w, accu = 1, 0
    cnt = 0
    while w <= MAX_W:
        if accu <= 6*w:
            accu += w
            cnt += 1
        else:
            w = (accu+5)//6
    return cnt

def ant_stack(K):
    N = input()
    W = map(int, raw_input().strip().split())
    result = 1
    dp = [[float("inf") for _ in xrange(K+1)] for _ in xrange(2)]
    dp[0][0], dp[0][1] = 0, W[0]
    for i in xrange(1, N):
        dp[i%2][0] = 0
        for j in xrange(1, min(i+2, K+1)):
            dp[i%2][j] = dp[(i-1)%2][j]
            if dp[(i-1)%2][j-1] <= 6*W[i]:
                dp[i%2][j] = min(dp[i%2][j], dp[(i-1)%2][j-1]+W[i])
            if dp[i%2][j] != float("inf"):
                result = max(result, j)
    return result

K = 139 #get_upper_bound()
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, ant_stack(K))
