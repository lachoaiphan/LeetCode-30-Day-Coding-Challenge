"""
Prompt:
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) 
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""


# Runs in O(m * n) time and space. Used dynamic programming to find the longest subsequence between the two strings


def longestCommonSubsequence(text1, text2):
    text1_len = len(text1)
    text2_len = len(text2)
    seq_list = [[0 for j in range(0, text2_len)] for i in range(0, text1_len)]
    max_num = 1 if text1[0] == text2[0] else 0
    seq_list[0][0] = max_num
    for i in range(1, text2_len):
        if text1[0] == text2[i] or seq_list[0][i - 1] == 1:
            seq_list[0][i] = 1
            max_num = 1
    for j in range(1, text1_len):
        if text1[j] == text2[0] or seq_list[j - 1][0] == 1:
            seq_list[j][0] = 1
            max_num = 1
    for i in range(1, text1_len):
        for j in range(1, text2_len):
            if text1[i] == text2[j]:
                seq_list[i][j] = seq_list[i - 1][j - 1] + 1
            else:
                seq_list[i][j] = max(seq_list[i - 1][j], seq_list[i][j - 1])
            max_num = max(seq_list[i][j], max_num)
    return max_num


# Test Case
print(longestCommonSubsequence("abcde", "abc"))  # Returns 3
print(longestCommonSubsequence("abcde", "aec"))  # Returns 2
print(longestCommonSubsequence("zfe", "aec"))  # Returns 1
print(longestCommonSubsequence("zfeasdfe", "faecbzgdsaerfgc"))  # Returns 4
