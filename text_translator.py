import requests
import os

url = "https://api-free.deepl.com/v2/translate"
api_key = '8edcabcf-2501-1d75-f520-82e2684e2611:fx'

# request headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Set up the request payload
payload = {
    "auth_key": api_key,
    "text": "Hello, how are you?",
    "source_lang": "EN",
    "target_lang": "JA"
}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    translated_text = response.json()["translations"][0]["text"]
    print("Translated text:", translated_text)
else:
    print("Translation failed. Status code:", response.status_code)

