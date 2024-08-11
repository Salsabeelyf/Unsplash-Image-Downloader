import constants as c
import helpers as h


def run():
    # Seach for images and get a list of them as html nodes
    images = h.search_for_images(search_query=c.search_query, no_of_images=c.no_of_images)

    # Download images into local folder
    h.download_images_locally(images)

if __name__ == '__main__':
    run()

