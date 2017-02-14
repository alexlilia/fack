def fack(word, k):
    #Function that takes a string and a value for k, and outputs its k-factors
    k_factors = set([])
    if len(word) < k:
        k_factors = set([word])
        return k_factors
    else:
        n = 0
        while n <= len(word) - k:
            k_factors = k_factors.union(set([word[n:(n+k)]]))
            n += 1
        return k_factors

#print(fack("abcdefg", 4))

def fack_list(words, k):
    #Function that takes a list of strings and a value for k, and outputs the combined set of k-factors
    k_factors_list = set([])
    for word in words:
        k_factors_list = k_factors_list.union(fack(word, k))
    return k_factors_list

#print(fack_list(['abc', 'def', 'ghijklm', 'xyz'], 2))