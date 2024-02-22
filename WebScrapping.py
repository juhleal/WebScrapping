import requests
from bs4 import BeautifulSoup

# Send HTTP request and parse HTML
url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract relevant information
# Example: Find all links on the page
links = soup.find_all('a')
for link in links:
    print(link.get('href'))
