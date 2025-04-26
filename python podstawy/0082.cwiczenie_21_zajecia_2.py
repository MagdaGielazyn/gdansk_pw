#Napisz pętlę while, która zaczyna się od ostatniego znaku w napisie i działa od końca,
# do pierwszego znaku, wypisując każdą literę w osobnej linii, w odwrotnej kolejności.

slowo = 'koteczek'
indeks = len(slowo)-1

while indeks >=0:
    print(slowo[indeks])
    indeks -=1