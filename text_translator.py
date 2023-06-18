import requests
import os

url = "https://api-free.deepl.com/v2/translate"
api_key = '8edcabcf-2501-1d75-f520-82e2684e2611:fx'
headers = {"Content-Type": "application/x-www-form-urlencoded"}

def translate_text(input_text, source_lang, target_lang):
    payload = {
        "auth_key": api_key,
        "text": input_text,
        "source_lang": source_lang,
        "target_lang": target_lang
    }
    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()["translations"][0]["text"]
    else:
        print("Translation failed. Status code:", response.status_code)
        return None

