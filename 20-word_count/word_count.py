total_words = 0
total_chars = 0

with open(r'C:\Users\matteo.sala\Documents\Python Workout\20-word_count\wcfile.txt', 'r') as file:
    for line in file:
        wordcount = len(line.split())
        charcount = len(line)
        
        print(line.split())
        
        total_words += wordcount
        total_chars += charcount

# 1
print(f'Total words: {total_words}')
# 2
print(f'Total chars: {total_chars}')
