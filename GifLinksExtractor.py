import requests
from bs4 import BeautifulSoup
import re

# Replace 'Your Website Link' with your website URL
url = 'Your Website Link'

# Send a GET request to the website and get the HTML content
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all elements that might contain GIF links
gif_links = []

# Find image tags that contain GIFs
for img_tag in soup.find_all('img', src=re.compile('.gif$')):
    gif_links.append(img_tag['src'])

# Write links to a text file
with open('gif_links.txt', 'w') as file:
    for link in gif_links:
        file.write(link + '\n')

print(f"Extracted {len(gif_links)} GIF links to 'gif_links.txt'")
