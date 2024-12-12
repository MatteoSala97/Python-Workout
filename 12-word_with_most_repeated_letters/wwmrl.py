from collections import Counter
words = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_count(word): 
    return Counter(word).most_common(1)[0][1] # (1) - indica che voglio l'elemento più comune; [0] - accede al primo elemento della tupla generata precedentemente (nonché unica) ovver index[0]; [1] - accede al secondo elemento della tupla generata
def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)

print(most_repeating_word(words))
counter = Counter('elementary')
print(counter.most_common(1))

'''
Output: elementary [('e', 3)]

'''