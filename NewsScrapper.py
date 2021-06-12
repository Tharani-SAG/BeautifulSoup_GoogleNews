#!/usr/bin/env python3

import urllib
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup


class NewsScrapper:
    def __init__(self):
        self.images = {}

    def get_images(self, url):
        dom = urllib.request.urlopen(url).read()
        bs = BeautifulSoup(dom, "html.parser")
        body = bs.find('body')

        headings = body.findAll('h3')
        img_tags = body.findAll('img')

        min_index = len(headings) if len(headings) < len(img_tags) else len(img_tags)

        for index in range(min_index):
            self.images[headings[index].text] = img_tags[index]['src']

    def list_images(self):
        for heading, image in self.images.items():
            print(heading, image)

    def show_image_from_heading(self, keyword):
        img_url = None
        for heading in self.images.keys():
            if keyword in heading:
                img_url = self.images[heading]
                break

        if not img_url:
            print("No image found for the keyword")
            return

        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        img.show()


def main():
    newsScrapper = NewsScrapper()
    newsScrapper.get_images('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
    # newsScrapper.list_images()
    newsScrapper.show_image_from_heading('Digvijaya Singh')


if __name__ == '__main__':
    main()
