# Author - Nilesh D
# December 14 - A Wordplay with Vowels and Consonants


def subString(s, n):
    vowel = ['a', 'e', 'i', 'o', 'u']
    scoreA = scoreB = 0
    for i in range(n):
        for len in range(i+1, n+1):
            subsStr = s[i: len]
            if subsStr[0] in vowel:
                scoreA += 1
            else:
                scoreB += 1
    if scoreA > scoreB:
        print("The winner is A with", scoreA, "points")
    else:
        print("The winner is B with", scoreB, "points.")


s = input("Enter string: ")
subString(s, len(s))
