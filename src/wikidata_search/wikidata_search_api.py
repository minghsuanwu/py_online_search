'''
Created on 2018年4月9日

@author: Ming_Wu
'''
from google_search import GoogleSearch
import requests
import json

class WikidataSearch():
    entityName = ''
    pageNum = '0'
    
    
    def __init__(self, entityName):
        self.entityName = entityName
      
    def process(self):
        wiki = 'https://www.wikidata.org/w/api.php?action=wbsearchentities&search='+self.entityName+'&format=json&language=en&uselang=en&type=item&continue='+self.pageNum
        response = requests.get(wiki, headers = {'User-Agent': GoogleSearch.CHROME})
        self.parseJson(response.text)
      
    def parseJson(self, json_string):
        parsed_json = json.loads(json_string)
        for search in parsed_json['search']:
            print(search['id']+': '+search['label'])

        
def main():
    start = GoogleSearch.millis()
    wikidataSearch = WikidataSearch('李小龍')
    wikidataSearch.process()
    print('Process time: '+ str(GoogleSearch.millis() - start) + 'ms')
    
if __name__ == "__main__":
    main()