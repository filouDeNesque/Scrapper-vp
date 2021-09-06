import requests
import re
from bs4 import BeautifulSoup
from Annonce import Annonce

class scrap:


    def __init__(self):

        self.headers= {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

        self.url = "https://www.paruvendu.fr/mondebarras/listefo/default/default/?fulltext=iPhone&elargrayon=1&ray=50&idtag=1818&r=BMUTT000&libelle_lo=Paris+%2875%29&codeinsee=&lo=75&pa=&ray=50&zvy=&zvt=&px0=&px1=&zmd%5B%5D=VENTE&zmd%5B%5D=TROC&zmd%5B%5D=DON&zmd%5B%5D=RECH&codPro=&filtre=&tri=&ck-part=on&ck-pro=on"
    
    def goScrap(self):
        response = requests.get(self.url, headers=self.headers)
        print(response)

        soup = BeautifulSoup(response.text, 'html.parser')

        annoncesTitle = soup.findAll("h3")
        annoncesPrix = soup.find_all("span", class_="rlmob15_annonceprix")
        annoncesDesc = soup.find_all("p", class_="flol")
        annoncesLink = soup.find_all(["a","div"],href=re.compile("/high-tech/*"))

        print("AnnonceTitle : "+str(len(annoncesTitle)))
        print("AnnoncePrix : "+str(len(annoncesPrix)))
        print("AnnoncesLink length : "+str(len(annoncesLink)))
        print("AnnoncesDesc length : "+str(len(annoncesDesc)))

        annoncelist = []
        index= 0
        while index < len(annoncesTitle):
            annonce = Annonce()
            annonce.title = annoncesTitle[index]
            annonce.price = annoncesPrix[index]
            annonce.desc = annoncesDesc[index]
            annonce.link = annoncesLink[index].get('href')
            annoncelist.append(annonce)
            index = index + 1

        return annoncelist    
