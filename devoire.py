import requests
from bs4 import BeautifulSoup
import csv

def scraper_lenouvellistelg():
    url = "https://lenouvelliste.com/"
    reponse = requests.get(url)

    if reponse.ok:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        divs_articles_en_vedette = soup.find_all('div', class_='lnv-featured-article-lg')

        with open('Donneryo.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
            entetes = ['Article', 'Grand titre', 'Lien Image', 'Description']
            redacteur_csv = csv.DictWriter(fichier_csv, fieldnames=entetes)
            redacteur_csv.writeheader()

            for numero_article, div_article in enumerate(divs_articles_en_vedette, start=1):
                elements_h1_article = [h1 for h1 in div_article.find_all('h1') if h1]

                for h1_element in elements_h1_article:
                    texte_h1 = h1_element.text.strip()

                    liens_images_article = [img['src'] for img in div_article.find_all('img')]

                    elements_description = div_article.select('div.lnv-featured-article-lg p')
                    texte_description = ' '.join([p.text.strip() for p in elements_description])
                    redacteur_csv.writerow({'Article': f'Article {numero_article}\n',
                                           'Grand titre': f'Grand Titre: {texte_h1}\n',
                                           'Lien Image': f'Lien Image: {", ".join(liens_images_article)}\n',
                                           'Description': f'Description: {texte_description}\n\n'})

        print("Succes grand titre")
    else:
        print(f"Erreur")

def scraper_lenouvellistesm():
    url = "https://lenouvelliste.com/"
    reponse = requests.get(url)

    if reponse.status_code == 200:
        soup = BeautifulSoup(reponse.text, 'html.parser')

        divs_articles_en_vedette = soup.find_all('div', class_='lnv-featured-article-sm')

        with open('len.csv', 'w', newline='', encoding='utf-8') as fichier_csv:
            entetes = ['Article', 'Grand titre', 'Lien Image', 'Description']
            redacteur_csv = csv.DictWriter(fichier_csv, fieldnames=entetes)
            redacteur_csv.writeheader()

            for numero_article, div_article in enumerate(divs_articles_en_vedette, start=1):
                elements_h1_article = [h1 for h1 in div_article.find_all('h1') if h1]

                for h1_element in elements_h1_article:
                    texte_h1 = h1_element.text.strip()

                    liens_images_article = [img['src'] for img in div_article.find_all('img')]

                    elements_description = div_article.select('div.lnv-featured-article-sm p')
                    texte_description = ' '.join([p.text.strip() for p in elements_description])
                    redacteur_csv.writerow({'Article': f'Article {numero_article}\n',
                                           'Grand titre': f'Grand Titre: {texte_h1}\n',
                                           'Lien Image': f'Lien Image: {", ".join(liens_images_article)}\n',
                                           'Description': f'Description: {texte_description}\n\n'})

        print("Succes")
    else:
        print(f"Erreur")
if __name__ == "__main__":
    
    scraper_lenouvellistelg()
    scraper_lenouvellistesm()
