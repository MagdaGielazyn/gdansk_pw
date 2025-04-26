#podobnie jak przy stringach, można otrzymać wycinki list
lista = [1, 't', 56, 'numer', 4.5]
lista[1:3] #-> [‘t’, 56]
lista[:2] #-> [1, ‘t’]
lista[3:] #-> [‘numer’, 4.5]
lista[:] #-> [1, ‘t’, 56, ‘numer’, 4.5]
#• za pomocą wycinków można zmienić kilka elementów na raz
#Przykład:
lista = [1, 't', 56, 'numer', 4.5]
lista[2:4] = ['inne', 'elementy']
lista = [1, 't', 'inne', 'elementy', 4.5]