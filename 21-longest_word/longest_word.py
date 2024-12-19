import os 

def find_longest_word(filename):
    longest_word = ''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

def find_all_longest_words(dirname):
    return {filename: find_longest_word(os.path.join(dirname, filename))    
    for filename in os.listdir(dirname) 
        if os.path.isfile(os.path.join(dirname, filename))}  

print(find_all_longest_words(r'C:\Users\matteo.sala\Documents\Python Workout\21-longest_word\books'))