import requests
import json

def filmsBot(filmsToShow, type, gener, language):
    
    api_key = '7be72508776961f3948639fbd796bccd'
    page = f'https://api.themoviedb.org/3/movie/{type}?with_genres={gener}&api_key={api_key}&language={language}'
    api = requests.get(page)
    json_data = json.loads(api.content)
    
    for n in range(5):
        
        title = json_data['results'][n]['title']
        votes = json_data['results'][n]['vote_average']
        description = json_data['results'][n]['overview']
        
        message = f'Titulo: {title}\n Votes: {votes}\n Sinopsis: {description}'
        
        requests.post('https://api.telegram.org/bot6921140535:AAGOnaIbzmR6C3o5Bxe5qq1pn_97KOdsGKo/sendMessage',
              data = {'chat_id' : '-1002078661389', 'text' : message})
 
#le decimos que nos de 5 peliculas populares, genero 18 que es drama, en el lenguaje español
#los generos son por numeros y estan en la pagina oficial de themoviedb        
filmsBot(5, 'popular', '18', 'es')