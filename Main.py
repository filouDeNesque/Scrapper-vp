from scrap import scrap
from Annonce import Annonce

print('Debut du main')
scrapobj =  scrap()
print(scrapobj)
annoncelist = scrapobj.goScrap()
print(annoncelist[0])
annonce = Annonce();
annonce = annoncelist[0]
print(annonce.price)
