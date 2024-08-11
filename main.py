import sys
import constants as c
import helpers as h


def run():
    # Check if argument provided
    if len(sys.argv) == 1:
        print('Please Provide 2 arguments, search keywork and number of images\nFor example: py main.py "water drop" 5')
        exit()

    c.search_query = sys.argv[1]
    c.no_of_images = int(sys.argv[2])

    # Seach for images and get a list of them as html nodes
    images_list = h.decide_html_or_api()

    # Download images into local folder
    h.download_images_locally(images_list)


    
if __name__ == '__main__':
    run()

