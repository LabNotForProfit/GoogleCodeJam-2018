// Copyright (c) 2018 kamyu. All rights reserved.

/*
 * Google Code Jam 2018 Round 1B - Problem C. Ant Stack
 * https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8
 *
 * Time  : O(N * K)
 * Space : O(K)
 *
 */

#include <iostream>
#include <vector>
#include <numeric>
#include <limits>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::numeric_limits;
using std::min;
using std::max;

int ant_stack() {
    const int K = 139;
    int N;
    cin >> N;
    vector<double> W(N, 0);
    for (int i = 0; i < N; ++i) {
        cin >> W[i];
    }
    int result = 1;
    vector<vector<double>> dp(2,
        vector<double>(K + 1, numeric_limits<double>::max()));
    dp[0][0] = 0.0f;
    dp[0][1] = W[0];
    for (int i = 1; i < N; ++i) {
        dp[i % 2][0] = 0.0f;
        for (int j = 1; j <= min(i+1, K); ++j) {
            dp[i % 2][j] = dp[(i - 1) % 2][j];
            if (dp[(i - 1) % 2][j - 1] <= 6.0f * W[i]) {
                dp[i % 2][j] = min(dp[i % 2][j], dp[(i - 1) % 2][j - 1] + W[i]);
            }
            if (dp[i % 2][j] != numeric_limits<double>::max()) {
                result = max(result, j);
            }
        }
    }
    return result;
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << ant_stack() << endl;
    }
    return 0;
}