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
                print('Couldn\'t download Image %d' % resp.status_code)
                print(resp.text)
                print('Retrying ...')
                resp = requests.get(img.download_link)
                if resp.status_code != 200:
                    print('Couldn\'t download Image %d' % resp.status_code)
                    print(resp.text)
                else:
                    file.write(resp.content)
            else:
                file.write(resp.content)
        i = i+1

    check_all_are_downloaded(download_path, images_list)


def check_all_are_downloaded(path, images_list):
    images_titles = set([image.title for image in images_list])

    dir_list = os.listdir(path)
    
    dir_list = [str.replace(file_name, '.jpg','') for file_name in dir_list]

    intersection_set = set(dir_list).intersection(images_titles)
 
    if len(intersection_set)==len(images_titles):
        print("All images downloaded successfully")
    else:
        missing_images_titles = images_titles.difference(intersection_set)
        missing_images = [image for image in images_list if list(missing_images_titles).count(image.title) > 0]
        download_images_locally(missing_images)
