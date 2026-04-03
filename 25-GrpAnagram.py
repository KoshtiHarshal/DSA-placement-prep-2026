# Group Anagrams
# Given an array of strings, group anagrams together. You can return the answer in any order.

Str1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Str1 = [""]
# Str1 = ["a"]

anagram_map = {}

for s in Str1:
    key = "".join(sorted(s))
    
    if key in anagram_map:
        anagram_map[key].append(s)
    else:
        anagram_map[key] = [s]

print(list(anagram_map.values()))