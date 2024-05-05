import veryfi
import pprint

# Sử dụng Keys của veryfi
client_id = ''
client_secret = ''
username = ''
api_key = ''

categories = ['Grocery', 'Utilities', 'Travel']
file_path = 'images/images.jpg'

client = veryfi.Client(client_id, client_secret, username, api_key)

response = client.process_document(file_path, categories)

pprint.pprint(response['ocr_text'])
with open("text.txt","w+",encoding='utf-8') as f:
    f.write(response['ocr_text'])
