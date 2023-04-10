
import deepl
from api import api

import requests

# Define the DeepL API endpoint for text translation
url = 'https://api.deepl.com/v2/translate'

print("Please use this link to find the correct target language case use")
target_lg = input("Enter target language:\n", )
filename = input("Enter filename you wish to translate:", )
# Define the parameters for the request
params = {
    'auth_key': api,
    'text': '',
    'target_lang': target_lg
}

# Open the input file and read the text content
with open(filename, 'r') as f:
    text = f.read()

# Set the 'text' parameter to the input text
params['text'] = text

# Send a POST request to the DeepL API endpoint with the parameters
response = requests.post(url, data=params)

# Check if the request was successful
if response.status_code == 200:
    # Get the translated text from the response
    translated_text = response.json()['translations'][0]['text']

    # Open the output file and write the translated text
    with open('outputProcessed.txt', 'w') as f:
        f.write(translated_text)
else:
    print('Error:', response.status_code)

