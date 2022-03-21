import requests
import json

class GoogleTranslate:

    API_URL = "https://translate.google.com"
    
    def __init__(self, text: str, from_lang: str, to_lang: str):
        self.text = text
        self.from_lang = from_lang
        self.to_lang = to_lang
    
    def translate(self):
        headers = {
            'accept': '*/*',
            'user-agent': 'GoogleTranslate/6.31.59289 (iPhone; iOS 14.4; id; iPhone10,4)',
        }
        
        response = requests.get(self.API_URL + "/translate_a/single?client=it&dt=qca&dt=t&dt=rmt&dt=bd&dt=rms&dt=sos&dt=md&dt=gt&dt=ld&dt=ss&dt=ex&otf=3&dj=1&q="
        + self.text + "&hl=id&ie=UTF-8&oe=UTF-8&sl="
        + self.from_lang + "&tl="
        + self.to_lang, headers=headers);
        
        return self.parseResult(response.text)
    
    def parseResult(self, result):
        data = json.loads(result)
        return data['sentences'][0]['trans']