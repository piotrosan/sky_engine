from PIL import Image
from image_manager.models import Image as ImageModel
import io

class ImageWorker:

    def __init__(self, resolutionx: int, resolutiony: int):
        self.x = resolutionx
        self.y = resolutiony

    def resize_image(self, image_byte: io.BytesIO) -> Image:
        im: Image = Image.open(image_byte)
        return im.resize((self.x, self.y))

    def save_image(self, image_byte, file_extension: str = 'jpg') -> Image:
        image = ImageModel.objects.create(
            content=self.convert_to_concrete_format(
                self.resize_image(image_byte)
            ),
            file_extension=file_extension,
        )
        image.name = f"Face{image.id}"
        image.index = image.id
        return image

    def convert_to_concrete_format(self, image_byte, encoder_name: str = 'raw'):
        sized: Image = self.resize_image(image_byte)
        return sized.tobytes(encoder_name=encoder_name)
