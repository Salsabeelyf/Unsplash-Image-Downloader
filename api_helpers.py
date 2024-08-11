import requests
import constants as c
import classes

def get_images_info():
    page_no = 0
    images_list = []

    # Get images and save them to the list until reach the desired number of images
    while(len(images_list) < c.no_of_images ):
        page_no = page_no + 1

        # Get images per page
        resp = requests.get(f'https://unsplash.com/napi/search/photos?page={page_no}&per_page={c.no_of_images}&query={c.search_query}').json()
        
        # Extract images from response
        images = resp.get('results')

        # Save images ids, titles, and download links if only free
        list = [classes.Image(id = image.get('id'),
                              title = str.replace(image.get('alt_description'),' ','-'),
                              download_link = image.get('links').get('download')) for image in images if image.get('premium') == False]
        
        # Add images to images list
        images_list.extend(list)

    return images_list[:c.no_of_images]