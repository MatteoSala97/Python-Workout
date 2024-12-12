import operator 
people = [
    ('Donald', 'Trump', 7.85), 
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)]

def format_sort_records(list_of_tuples):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'  # questo identifica la lunghezza di ogni tupla. es: nome + 10 padding, cognome + 10 padding, tempo + 5 padding 
    for person in sorted(list_of_tuples, key=operator.itemgetter(1, 0)): # key=operator.itemgetter(1, 0) restituisce una tupla invertita rispetto a people[0] per esempio
        output.append(template.format(*person)) 
    # print(output)
    return output

print('\n'.join(format_sort_records(people)))
