#!/usr/bin/python3.4
from TwitterAPI import TwitterAPI
from streaming import stream
from streaming import track
import os.path

# Termo para ser pesquisado na API
TRACK_TERM = track.getTrack()

# Chaves de autenticação
CONSUMER_KEY = 'XOy76iSIQUOHa0g7HhMuT6Fku'
CONSUMER_SECRET = 'ONTI7KGeCefDYkuC9OV00SUXDdIYeVajQn25ZcNrcKKPIAOi44'
ACCESS_TOKEN_KEY = '589711107-Ui4d2kgolDP7ps95MqMKKuOYjGplQqQTIu8ytmK6'
ACCESS_TOKEN_SECRET = '7BcsLRODJVs6GcFUuEh7kmyiLq1l2fyCpUdjuBGOUtRSo'

# Criação de uma lista com as chaves de autenticação
api = TwitterAPI(CONSUMER_KEY,
                 CONSUMER_SECRET,
                 ACCESS_TOKEN_KEY,
                 ACCESS_TOKEN_SECRET)

# Requisição na API
r = api.request('statuses/filter', {'language': 'pt', 'track': TRACK_TERM})
s = ';'

# Verifica se o arquivo actual.csv existe. Se existir, ele e movido para uma pasta de backup
if os.path.isfile(track.getPath()):
    csv = open(track.getPath(), 'w', encoding="utf-8" )
    stream.manage_csv(csv, 1)
    csv.close()
else:
    csv = stream.create_csv()

# Geração de CSV
#csv = stream.create_csv()

# Criação das linhas
for item in r:
    #Gera as linhas num arquivo .csv
    stream.generate_rows(item, s, csv)
    
    #Caso o arquivo CSV ultrapasse 250MB, o mesmo será copiado para uma nova pasta e um novo arquivo CSV é criado. 
    #Um sendEmail informando a criação do novo arquivo é enviado com outros dados relativos ao arquivo.
    fileLimit = stream.manage_csv(csv, 0)
    if fileLimit is True:
        csv = stream.create_csv()