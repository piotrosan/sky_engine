import requests

from image.exceptions import ImageException
from image.respository import Repository
from image_manager.models import Image as ImageModel
from django.core.paginator import Paginator
from image.image_api import ImageAPI
import base64

class ImageGetter:

    @classmethod
    def get_binary_imag_from_remote(cls):
        r = requests.get(Repository.BASE_URL, stream=True)
        r.raw.decode_content = True
        return base64.b64encode(r.content)


    @classmethod
    def get_image_from_database(cls, index: int):
        return ImageModel.objects.get(index=index)

    @classmethod
    def get_paginated_image_from_databse(cls, page: int):
        paginator = Paginator(
            ImageModel.objects.order_by('created_date'),
        7)
        return paginator.get_page(page)

    @classmethod
    def change_index(cls, old_index: int):
        set1 = set(ImageModel.objects.value_list('id', flat=True).all())
        set2 = set(range(0, 1000000))
        diff = set2.difference(set1)
        ImageModel.objects.fiter(index=old_index).update(index=diff.pop())

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