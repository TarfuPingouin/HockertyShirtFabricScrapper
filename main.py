#Code written by Tarfu

import requests
import re
from bs4 import BeautifulSoup

page = requests.get("https://www.hockerty.fr/fr/homme/chemise-sur-mesure/personalize?step=fabric")
soup = BeautifulSoup(page.content, 'html.parser')

resultspan = soup.find_all("span", {"class":"fabric select"}) #Retourne tous les span des tissus
resultspanstr = str(resultspan) #Convertit l'HTML en Str
resultspanlist = resultspanstr.split("</span>") #Convertis le string en list, chaque span = 1 element

resultprice = soup.find_all("div", {"class":"price price_part man_shirt general visible"})
resultpricestr = str(resultprice)
resultpricelist = resultpricestr.split("</div>")

prixlistnew = []
autrelistenew = []

for y in resultpricelist:
    try:
        prix = re.search(' visible">(.+?)€',y)
        prixstr = str(prix.group(1))
        pass
    except:
        prix="-"
    prixlistnew.append(prixstr)


for i in resultspanlist:
    try:
        nom = re.search(' name="(.+?)"',i)
        nomstr=str(nom.group(1))
        pass
    except:
        nomstr="-"

    try:
        matiere = re.search(' c="(.+?)"',i)
        matierestr=str(matiere.group(1))
        pass
    except:
        matierestr="-"

    try:
        poids = re.search(' fw="(.+?)"',i)
        poidsstr=str(poids.group(1))
        pass
    except:
        poidsstr="-"

    try:
        season = re.search(' season="(.+?)"',i)
        seasonstr=str(season.group(1))
        pass
    except:
        seasonstr="-"

    try:
        couleur = re.search(' tone="(.+?)"',i)
        couleurstr=str(couleur.group(1))
        pass
    except:
        couleurstr="-"

    try:
        type = re.search(' thread_style="(.+?)"',i)
        typestr=str(type.group(1))
        pass
    except:
        typestr="-"

    try:
        ironing = re.search(' class="ico-easy-wrinkle">(.+?)</div>',i)
        ironingstr=str(ironing.group(1))
        pass
    except:
        ironingstr="-"

    try:
        lienimg = re.search(' data-src="(.+?)"',i)
        lienimgstr=str(lienimg.group(1))
        pass
    except:
        lienimgstr="-"

    temporaire = nomstr+"^"+matierestr+"^"+poidsstr+"^"+seasonstr+"^"+couleurstr+"^"+typestr+"^"+ironingstr+"^"+lienimgstr
    autrelistenew.append(temporaire)

for a, b in zip(autrelistenew, prixlistnew):
    temporaire2 = b+"^"+a
    print(temporaire2)