import requests

from image.exceptions import ImageException
from respository import Repository
from image_manager.models import Image as ImageModel
from django.core.paginator import Paginator
from image_api import ImageAPI

class ImageGetter:

    @classmethod
    def get_binary_imag_from_remote(cls):
        r = requests.get(Repository.BASE_URL, stream=True)
        r.raw.decode_content = True
        return r.content


    @classmethod
    def get_image_from_database(cls, id: int):
        return ImageModel.objects.get(pk=id)

    @classmethod
    def get_paginated_image_from_databse(cls, page: int):
        paginator = Paginator(
            ImageModel.objects.order_by('created_date'),
        7)
        return paginator.get_page(page)


class ImageSetter:
    image_api = ImageAPI()

    @classmethod
    def set_index(cls, pk: int, index: int):
        cls.image_api.update_image(pk, {'index': index})

    @classmethod
    def save_image(cls, image_data: dict):
        try:
            cls.image_api.save_image(
                image_data['image_byte']
            )
        except KeyError as e:
            raise ImageException(f'Image data variable is empty -> {e}')


class ImageWorker(ImageSetter, ImageGetter):
    pass