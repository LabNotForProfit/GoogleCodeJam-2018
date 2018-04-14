# Copyright (c) 2018 kamyu. All rights reserved.
#
# Google Code Jam 2018 Round 1A - Problem A. Waffle Choppers
# https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard
#
# Time:  O(R * C)
# Space: O(R + C)
#

def vertical_cut(counts, count_to_make, count_to_cut, cut_idxs):
    accu = 0
    for i, count in enumerate(counts):
        accu += count
        if accu == count_to_cut:
            cut_idxs.append(i)
            accu = 0
            count_to_make -= 1
    return count_to_make == 0

def horizontal_cut(waffle, counts, count_to_make, count_to_cut, cut_idxs):
    curr_counts = [0]*len(cut_idxs)
    accu = 0
    for r, count in enumerate(counts):
        i = 0
        for c in xrange(len(waffle[0])):
            if waffle[r][c] == '@':
                if c > cut_idxs[i]:
                    i += 1
                curr_counts[i] += 1
        accu += count
        if accu == count_to_cut:
            if any(c != curr_counts[0] for c in curr_counts):
                return False
            curr_counts = [0]*len(cut_idxs)
            accu = 0
            count_to_make -= 1
    return count_to_make == 0

def waffle_hoppers():
    R, C, H, V = map(int, raw_input().strip().split())
    waffle = []
    for r in xrange(R):
        waffle.append(list(raw_input().strip()))

    total_counts, h_counts, v_counts = 0, [0]*R, [0]*C
    for r in xrange(R):
        for c in xrange(C):
            if waffle[r][c] == '@':
                total_counts += 1
                h_counts[r] += 1
                v_counts[c] += 1

    if total_counts != 0:
        cut_idxs = []
        v_count_to_cut, v_remain = divmod(total_counts, V+1)
        if v_remain != 0 or not vertical_cut(v_counts, V+1, v_count_to_cut, cut_idxs):
            return "IMPOSSIBLE"

        h_count_to_cut, h_remain = divmod(total_counts, H+1)
        if h_remain != 0 or not horizontal_cut(waffle, h_counts, H+1, h_count_to_cut, cut_idxs):
            return "IMPOSSIBLE"

    return "POSSIBLE"

for case in xrange(input()):
    print 'Case #%d: %s' % (case+1, waffle_hoppers())
