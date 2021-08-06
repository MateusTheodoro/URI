palavra_um = input()
palavra_dois = input()
palavra_tres = input()

if palavra_um == 'vertebrado' and palavra_dois == 'ave' and palavra_tres == 'carnivoro':
    print('aguia')
if palavra_um == 'vertebrado' and palavra_dois == 'ave' and palavra_tres == 'onivoro':
    print('pomba')

if palavra_um == 'vertebrado' and palavra_dois == 'mamifero' and palavra_tres == 'onivoro':
    print('homem')
if palavra_um == 'vertebrado' and palavra_dois == 'mamifero' and palavra_tres == 'herbivoro':
    print('vaca')

if palavra_um == 'invertebrado' and palavra_dois == 'inseto' and palavra_tres == 'hematofago':
    print('pulga')
if palavra_um == 'invertebrado' and palavra_dois == 'inseto' and palavra_tres == 'herbivoro':
    print('lagarta')

if palavra_um == 'invertebrado' and palavra_dois == 'anelideo' and palavra_tres == 'hematofago':
    print('sanguessuga')
if palavra_um == 'invertebrado' and palavra_dois == 'anelideo' and palavra_tres == 'onivoro':
    print('minhoca')
