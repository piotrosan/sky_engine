import requests

from respository import Repository
from image_manager.models import Image as ImageModel
from django.core.paginator import Paginator


class ImageGetter:

    @classmethod
    def get_binary_imag_from_remote(cls):
        r = requests.get(Repository.BASE_URL, stream=True)
        r.raw.decode_content = True
        return r.content


    def get_image_from_database(self, id: int):
        return ImageModel.objects.get(pk=id)


    def get_paginated_image_from_databse(self, page: int):


        paginator = Paginator(
            ImageModel.objects.,
        7)
