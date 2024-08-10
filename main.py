import requests
import selectolax
import re
import os

def get_images(no_of_images):
    resp = requests.get(base_url+searchQuery)

    tree = selectolax.parser.HTMLParser(resp.content)

    images = tree.css('a[title="Download this image"]')

    return images[:no_of_images]

searchQuery = 'house'

base_url = 'https://unsplash.com/s/photos/'

resp = requests.get(base_url+searchQuery)

tree = selectolax.parser.HTMLParser(resp.content)

images = get_images(5)

i=0
for img in images:
    download_link = img.attrs['href']
    img_src = re.search('(photos\/)(.*)/',download_link).group(2)
    title = str.replace(tree.css(f'a[href*="{img_src}"]')[0].attrs['title'],' ', '-')

    download_path = 'images/'+searchQuery
    if not (os.path.isdir(download_path)):
        os.mkdir(download_path)

    with open(f'{download_path}/{title}.jpg', 'wb') as file:
        print('Downloading image: %d ...' % i)
        file.write(requests.get(download_link).content)
    i = i+1