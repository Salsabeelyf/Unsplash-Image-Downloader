import requests
import selectolax
import re
import constants as c
import classes

# Get a list of images download link html nodes
def get_images():
    resp = requests.get(c.base_url+c.search_query)

    global tree
    tree = selectolax.parser.HTMLParser(resp.content)

    images = tree.css('a[title="Download this image"]')

    return images

# Get image title
def get_image_title(image):
    # Exctract image id from its download link
    img_src = re.search('(photos\/)(.*)/',image.attrs['href']).group(2)

    # Find image title using its img_src based on id
    title = str.replace(tree.css(f'a[href*="{img_src}"]')[0].attrs['title'],' ', '-')

    return title


# Create list of image objects
def get_images_info(images):
    images_list = [classes.Image(id = re.search('(photos\/)(.*)/',image.attrs['href']).group(2),
                        title = get_image_title(image),
                        download_link = image.attrs['href']) for image in images[:c.no_of_images]]
    return images_list