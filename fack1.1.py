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
        k_factors = list(combinations(word.lower(),k)) ##this part can be changed to itertools.permutations for prek
        n_length = "This word has a length of %s and \
%s k-factors." % (len(word),len(k_factors))
        return (k_factors, n_length)

    while True:
        for i in fack():
            '''
            For-loop calling iterables of fack() function that prints lists
            of each combination; .join function cannot be used; return 
            function in fack() returned tuple.
            '''
            print(i)
        
        
