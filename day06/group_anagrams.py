"""
Prompt:
Given an array of strings, group anagrams together.
"""

# Runs in O(nk log n) time and O(k) space as O(n log n) involves sorting of the individiual string while O(k) is going through the whole list


def group_anagrams(strs):
    anagram_list = []
    anagram_dict = {}
    for cur_str in strs:
        sorted_str = ''.join(sorted(cur_str))
        if sorted_str not in anagram_dict:
            anagram_dict[sorted_str] = [cur_str]
        else:
            anagram_dict[sorted_str].append(cur_str)

    for key in anagram_dict.keys():
        anagram_list.append(anagram_dict[key])
    return anagram_list


# Test Cases
print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Outputs [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
