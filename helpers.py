import requests
import os
import api_helpers
import html_helpers
import constants as c

def decide_html_or_api():
    images = html_helpers.get_images()

    if c.no_of_images <= len(images):
        return html_helpers.get_images_info(images)
    return api_helpers.get_images_info()

# Create local download folder if doesn't exist
def create_local_folder():
        path = 'images/'+c.search_query
        if not (os.path.isdir('images')):
            os.mkdir('images')
        if not (os.path.isdir(path)):
            os.mkdir(path)
        return path

def download_images_locally(images_list):
    # Get download folder ready
    download_path = create_local_folder()

    i=1
    for img in images_list:
        # Download images into local folder
        with open(f'{download_path}/{img.title}.jpg', 'wb') as file:
            print('Downloading image: %d ...' % i)
            resp = requests.get(img.download_link)
            if resp.status_code != 200:
                raise RuntimeError('Couldn\'t download Image %d' % resp.status_code)
            file.write(resp.content)
        i = i+1