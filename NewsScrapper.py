#!/usr/bin/env python3

import urllib
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup


class NewsScrapper:
    def __init__(self):
        self.images = []

    def get_images(self, url):
        dom = urllib.request.urlopen(url).read()
        bs = BeautifulSoup(dom, "html.parser")
        img_tags = bs.find('body').findAll('img')
        for img in img_tags:
            self.images.append(img['src'])

    def list_images(self):
        for image in self.images:
            print(image)

    def show(self, index):
        if index >= len(self.images):
            return
        response = requests.get(self.images[index])
        img = Image.open(BytesIO(response.content))
        img.show()


def main():
    newsScrapper = NewsScrapper()
    newsScrapper.get_images('https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en')
    newsScrapper.list_images()
    newsScrapper.show(2)


if __name__ == '__main__':
    main()
