def firstlast(sequence):
    #prende il primo e l'ultimo index tramite metodo slice e concatena con +
    return sequence[:1] + sequence[-1:]

print(firstlast('ahabcd'))