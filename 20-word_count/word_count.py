total_words = 0
total_chars = 0
unique_words = set()

with open(r'C:\Users\matteo.sala\Documents\Python Workout\20-word_count\wcfile.txt', 'r') as file:
    for line in file:
        words = line.split()
        wordcount = len(line.split())
        charcount = len(line)
        
        total_words += wordcount
        total_chars += charcount
        unique_words.update(words)

# 1
print(f'Total words: {total_words}')
# 2
print(f'Total chars: {total_chars}')
# 3 
print(f'Unique words: {len(unique_words)}')