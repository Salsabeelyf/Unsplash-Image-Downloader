import requests
import selectolax
import re
import os
import constants as c

# Get a list of images download link html nodes
def get_images(no_of_images):
    resp = requests.get(c.base_url+c.search_query)

    global tree
    tree = selectolax.parser.HTMLParser(resp.content)

    images = tree.css('a[title="Download this image"]')

    return images[:no_of_images]

# search for images using search query
def search_for_images(search_query, no_of_images):
    resp = requests.get(c.base_url+search_query)
    tree = selectolax.parser.HTMLParser(resp.content)

    return get_images(no_of_images)


def get_image_title(image):
    # Exctract image id from its download link
    img_src = re.search('(photos\/)(.*)/',image.attrs['href']).group(2)

    # Find image title using its img_src based on id
    title = str.replace(tree.css(f'a[href*="{img_src}"]')[0].attrs['title'],' ', '-')

    return title
     

# Create local download folder if doesn't exist
def create_local_folder(path):
        if not (os.path.isdir(path)):
            os.mkdir(path)


def download_images_locally(images):
    i=1
    for img in images:
        # Get download folder ready
        download_path = 'images/'+c.search_query
        create_local_folder(download_path)

        # Download images into local folder
        with open(f'{download_path}/{get_image_title(img)}.jpg', 'wb') as file:
            print('Downloading image: %d ...' % i)
            file.write(requests.get(img.attrs['href']).content)
        i = i+1