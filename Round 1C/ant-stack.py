# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1C - Problem A. A Whole New Word
# https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard
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
    INF = 10**14
    result = 1
    dp = [INF for _ in xrange(2*K)]
    dp[0], dp[1] = 0, W[0]
    for i in xrange(1, N):
        dp[(i%2)*K] = 0
        for j in xrange(1, min(i+2, K+1)):
            dp[(i%2)*K+j] = dp[((i-1)%2)*K+j]
            if dp[((i-1)%2)*K+j-1] <= 6*W[i]:
                dp[(i%2)*K+j] = min(dp[(i%2)*K+j], dp[((i-1)%2)*K+j-1]+W[i])
            if dp[(i%2)*K+j] != INF:
                result = max(result, j)
    return result

K = 139 # get_upper_bound()
for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, ant_stack(K))
