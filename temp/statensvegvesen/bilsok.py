'''
Statens Vegvesen sin API som lar deg søke opp informasjon om bilar vha. 
registreringsnummer eller chassisnummer. NB: Å få informasjon om eigar kostar pengar.
- https://www.vegvesen.no/om-oss/om-organisasjonen/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger/ 
- https://autosys-kjoretoy-api.atlas.vegvesen.no/api-ui/index-enkeltoppslag.html
'''

import requests
import json

apikey = ""

bil = "SX12896"

headers = { 'SVV-Authorization' : 'Apikey XXX' }

sokeurl = f'https://www.vegvesen.no/ws/no/vegvesen/kjoretoy/felles/datautlevering/enkeltoppslag/kjoretoydata?kjennemerke={bil}'

print(sokeurl)

r = requests.get(sokeurl, headers = { 'SVV-Authorization' : 'Apikey XXX' })

print(r.status_code)
print(r.headers)
print(r.encoding)
print(r.json)
print(r.text)
data = r.text
print(type(data))

dataDict = json.loads(data)
print(dataDict)
print(type(dataDict))

print("\nForsøker å skrive ut utvalgt del:")
print(dataDict["kjoretoydataListe"][0]["godkjenning"]["tekniskGodkjenning"]["tekniskeData"]["generelt"])