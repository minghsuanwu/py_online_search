'''
Created on 2018年3月20日

@author: Ming_Wu
'''

from bs4 import BeautifulSoup
import requests
import time


CHROME = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
class GoogleSearch:
    
    
    def process(self, text):
        response = requests.get('https://google.com/search?q=' + text, headers = {'User-Agent': CHROME})
        soup = BeautifulSoup(response.text, "html.parser")
    #     print(soup.prettify())
        google_result = self.parseGoogleResult(soup)
        if google_result: 
            print('google_result: '+google_result)
            
        google_suggest = self.parseGoogleSuggest(soup)        
        if google_suggest: 
            print('google_suggest '+google_suggest)
            
        entity_name = self.parseEntityName(soup)
        if entity_name: 
            print('entity_name: ' + entity_name)
            
        definition = self.parseDefinition(soup)
        if definition: 
            print('definition: ' + definition)
            
        description = self.parseDescription(soup)
        if description: 
            print('description: ' + description)
    
    def parseGoogleResult(self, soup):
        items = soup.select('div.Z0LcW')
        if not items:
            items = soup.select('div.kpd-ans.kno-fb-ctx._fbh')
        if not items:
            items = soup.select('div.kpd-ans.kno-fb-ctx.KBXm4e')
    #     股價
        if not items:
            items = soup.select('div._FOc')
        if not items:
            items = soup.select('div.YYyP2')
        for item in items:
            return item.text
    
    def parseGoogleSuggest(self, soup):
        items = soup.select('div._oDd')
        if not items:
            items = soup.select('div.qtR3Y')
        if not items:
            items = soup.select('span.vk_gy.vk_sh')
        for item in items:
            return item.text
    
    def parseEntityName(self, soup):    
        items = soup.select('div.kno-ecr-pt.kno-fb-ctx')
        for item in items:
            return item.text
    
    def parseDefinition(self, soup):
        items = soup.select('div._gdf.kno-fb-ctx._LAf')
        if not items:
            items = soup.select('div.sthby.kno-fb-ctx')
        if not items:
            items = soup.select('span.YhemCb')
        for item in items:
            return item.text
        
    def parseDescription(self, soup):
        items = soup.select('div._cgc.kno-fb-ctx')
        if not items:
            items = soup.select('div.hb8SAc.kno-fb-ctx')        
        for item in items:
            return item.text
    
def millis():
    return round(time.time() * 1000)
  
def main():
    start = millis()
    googleSearch = GoogleSearch()
    googleSearch.process('李小龍兒子')
    print('Process time: '+ str(millis() - start) + 'ms')
    
if __name__ == "__main__":
    main()