#Requests http library
import requests
# signed up for Oxford API free access https://developer.oxforddictionaries.com

app_id = '11ece1b6'
app_key = '41bec15756a3c373b86ec0e2443e9580'

language = 'en'
word_id = raw_input("Enter word to lookup in dictionary:")

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
#Accepts the app Id and app key as headers and uses get http method
r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
i=1
print word_id +" means:\n"
# Traverses the response and prints out all meanings of the word
for data in r.json()['results']:
    for item in data['lexicalEntries']:
        for entry in item['entries']:
            for sense in entry['senses']:
                print str(i)+":"+sense['definitions'][0]
                i+=1