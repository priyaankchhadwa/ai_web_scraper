import requests
from bs4 import BeautifulSoup

CONTEXT_LENGTH = 127000     # context length for Llama3.2 (128K) - template

def extract_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive'
    }
    
    r = requests.get(url)

    content = BeautifulSoup(r.text, "html.parser")

    body = BeautifulSoup(str(content.body), "html.parser")
    
    body.extract('script')
    body.extract('style')

    cleaned_body = body.get_text(separator='\n', strip=True)
    cleaned_body = '\n'.join(line.strip() for line in cleaned_body.splitlines() if line.strip())
    
    return cleaned_body

def chunkify(text, chunk_size):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
