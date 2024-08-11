import requests
import constants as c
import classes

def get_images_info():
    page_no = 1
    resp = requests.get(f'https://unsplash.com/napi/search/photos?page={page_no}&per_page={c.no_of_images}&query={c.search_query}').json()
    images = resp.get('results')
    images_list = [classes.Image(id = image.get('id'),
                                 title = str.replace(image.get('alt_description'),' ','-'),
                                 download_link = image.get('links').get('download')) for image in images]
    return images_list