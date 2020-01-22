from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from main.models import Game

def extraerDatosURL():
    
    #PC Games -------------------------------------------------------------------------------------------------------------

    pc = urlopen('https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/').read()
    soup = BeautifulSoup(pc, 'lxml')

    gamesPc=soup.find_all('li', class_=["search-results-row"])
        
    for game in gamesPc:
        name = game.find('h2').get_text()
        price = game.find('div',class_=["search-results-row-price"]).get_text()
        rate = game.find('div',class_=["metacritic d-none d-xl-block"]).get_text()
        if(rate == ' —'):
            rate = 0.0
        category = game.find('div',class_=["search-results-row-game-infos"]).get_text().split("-")[1]
        link2 = game.find('a',class_=["search-results-row-link"]).get('href')
        pc = urlopen(link2).read()
        soup = BeautifulSoup(pc, 'lxml')
        link = soup.find('div', class_=["offers-table-row-cell buy-btn-cell"]).find('a').get('href')
        picture = soup.find('div', class_=["content-box"]).find('img').get('src')
        comment = soup.find_all('h3', class_=["content-box-title"])
        comments = comment[0].get_text().split()[0]
        if(comments == 'Be'):
            comments = 0
        
        nq = name.replace(" ", "+")
        enlace = 'https://www.amazon.es/s?k=' + nq +"&i=videogames&__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1"
        linkGame = Request(enlace , headers={'User-Agent': 'Mozilla/5.0'})
        game = urlopen(linkGame).read() 
        soup = BeautifulSoup(game, 'lxml')
        
        priceG = soup.find_all('span', class_=["a-price-whole"])
        priceG = priceG[0].get_text()
        priceG = priceG.replace(",", ".")
        Game.objects.create(title=name,price=float(price.split('€')[0]),category=category,comments=int(comments),rate=float(rate),plataform='PC',link=link,picture=picture,gamePrice=float(priceG))
    
    #XBox Games --------------------------------------------------------------------------------------------------------------
    
    xbox = urlopen('https://www.allkeyshop.com/blog/catalogue/category-xbox-all/').read()
    soup = BeautifulSoup(xbox, 'lxml')

    gamesXbox=soup.find_all('li', class_=["search-results-row"])
    
    for game in gamesXbox:
        name = game.find('h2').get_text()
        price = game.find('div',class_=["search-results-row-price"]).get_text()
        rate = game.find('div',class_=["metacritic d-none d-xl-block"]).get_text()
        if(rate == ' —'):
            rate = 0.0
        plataform = game.find('div',class_=["search-results-row-game-infos"]).get_text().split("-")[1]
        link2 = game.find('a',class_=["search-results-row-link"]).get('href')
        pc = urlopen(link2).read()
        soup = BeautifulSoup(pc, 'lxml')
        link = soup.find('div', class_=["offers-table-row-cell buy-btn-cell"]).find('a').get('href')
        picture = soup.find('div', class_=["content-box"]).find('img').get('src')
        comment = soup.find_all('h3', class_=["content-box-title"])
        comments = comment[0].get_text().split()[0]
        if(comments == 'Be'):
            comments = 0
        category = soup.find_all('a', rel=['noopener noreferrer'])
        if(len(category) == 0):
           category = 'Sin categoria'
        else:
           category = category[0].get_text()
        Game.objects.create(title=name,price=float(price.split('€')[0]),category=category,comments=int(comments),rate=float(rate),plataform=plataform,link=link,picture=picture,gamePrice=0)
   
    #PSX Games -------------------------------------------------------------------------------------------------------------------

    psx = urlopen('https://www.allkeyshop.com/blog/catalogue/category-playstation-all/').read()
    soup = BeautifulSoup(psx, 'lxml')

    gamesPsx=soup.find_all('li', class_=["search-results-row"])
    
    for game in gamesPsx:
        name = game.find('h2').get_text()
        price = game.find('div',class_=["search-results-row-price"]).get_text()
        rate = game.find('div',class_=["metacritic d-none d-xl-block"]).get_text()
        if(rate == ' —'):
            rate = 0.0
        plataform = game.find('div',class_=["search-results-row-game-infos"]).get_text().split("-")[1]
        link2 = game.find('a',class_=["search-results-row-link"]).get('href')
        pc = urlopen(link2).read()
        soup = BeautifulSoup(pc, 'lxml')
        link = soup.find('div', class_=["offers-table-row-cell buy-btn-cell"]).find('a').get('href')
        picture = soup.find('div', class_=["content-box"]).find('img').get('src')
        comment = soup.find_all('h3', class_=["content-box-title"])
        comments = comment[0].get_text().split()[0]
        category = soup.find_all('a', rel=['noopener noreferrer'])
        if(comments == 'Be'):
           comments = 0
        if(len(category) == 0):
           category = 'Sin categoria'
        else:
           category = category[0].get_text()
        Game.objects.create(title=name,price=float(price.split('€')[0]),category=category,comments=int(comments),rate=float(rate),plataform=plataform,link=link,picture=picture,gamePrice=0)
    
    #Nintendo Games-----------------------------------------------------------------------------------------------------------------
    
    nintendo = urlopen('https://www.allkeyshop.com/blog/catalogue/category-nintendo-all/').read()
    soup = BeautifulSoup(nintendo, 'lxml')

    gamesNintendo=soup.find_all('li', class_=["search-results-row"])
    
    for game in gamesNintendo:
        link2 = game.find('a',class_=["search-results-row-link"]).get('href')
        name = game.find('h2').get_text()
        price = game.find('div',class_=["search-results-row-price"]).get_text()
        rate = game.find('div',class_=["metacritic d-none d-xl-block"]).get_text()
        if(rate == ' —'):
            rate = 0.0
        plataform = game.find('div',class_=["search-results-row-game-infos"]).get_text().split("-")[1]
        pc = urlopen(link2).read()
        soup = BeautifulSoup(pc, 'lxml')
        link = soup.find('div', class_=["offers-table-row-cell buy-btn-cell"]).find('a').get('href')
        picture = soup.find('div', class_=["content-box"]).find('img').get('src')
        comment = soup.find_all('h3', class_=["content-box-title"])
        category = soup.find_all('a', rel=['noopener noreferrer'])
        comments = comment[0].get_text().split()[0]
        if(comments == 'Be'):
           comments = 0
        if(len(category) == 0):
           category = 'Sin categoria'
        else:
           category = category[0].get_text()
        Game.objects.create(title=name,price=float(price.split('€')[0]),category=category,comments=int(comments),rate=float(rate),plataform=plataform,link=link,picture=picture,gamePrice=0)
