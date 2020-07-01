'''
 ' Python Local Webpage Images Extractor/Downloader
 ' @author: Sanjan Geet Singh
'''

from bs4 import BeautifulSoup       # Module to work with HTML files.
from urllib.request import urlretrieve    # Module to download files from remote web server.

# Settings
html_file = 'page.html'
download_directory = './imgs'
download_files_extension = 'png'

# Main Code
print('[INFO] Image Links will be extracted from file:', html_file)
print('[INFO] Downloaded Images will be stored in directory:', download_directory)
print('[INFO] Downloaded Images will have the extension:', download_files_extension)

print('Reading File {}'.format(html_file))
try:
      file = open(html_file, 'r')
      page = file.read()
      file.close()
except FileNotFoundError:
      print('[ERROR] HTML Webpage is absent')
      exit()

print('Extracting Image Links...')

soup = BeautifulSoup(page, 'html.parser')
links = []

for link in soup.findAll('img'):    # we only want to extract image links, written as <img src="{Link to Image}"></img>
      links.append(link.get('src'))

no_of_images = len(links)
print('Total Number of Images:', no_of_images)

for i in range(no_of_images):
      file = '{}/{}.{}...'.format(download_directory, i, download_files_extension)
      print('Downloading {} into {}'.format(links[i], file))
      urlretrieve(links[i], file)
