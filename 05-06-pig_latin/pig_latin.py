user_input = input("Let's speak in Pig Latin. Enter a word or a phrase: ")
stripped_input = list(user_input)

vowels = ['a', 'e', 'i', 'o', 'u']
#modo molto figo di fare un for loop rispetto al metodo classico
pig_latin = [i + 'us' if i.lower() in vowels else i for i in stripped_input]

# for i in stripped_input:
#     if i.lower() in list:
#         pig_latin.append(i + 'us')
#     else:
#         pig_latin.append(i)

result = ''.join(pig_latin)
print(result)

'''
example: 

    Let's speak in Pig Latin. Enter a word or a phrase: Ciao mi chiamo Matteo!
    Ciusausous mius chiusausmous Maustteusous!
    
'''