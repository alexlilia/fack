from itertools import combinations

class KFax:
    '''
    Class is useless... for now...
    '''

    def fack():
        '''
        User input defines word and k, and k_factors is named as a list of
        non-repeating combinations.
        '''
        word = input("Please enter a word: ")
        k = int(input("Please enter a value for k: "))
        k_factors = list(combinations(word.lower(),k))
        n_length = "This word has %s k-factors" % len(k_factors)
        return (k_factors, n_length)

    for i in fack():
        '''
        For-loop calling iterables of fack() function that prints lists
        of each combination; .join function used to merges items in each list.
        '''
        print(i)
        
