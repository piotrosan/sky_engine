from PIL import Image
from image_manager.models import Image as ImageModel
import io

class ImageAPI:

    def resize_image(self, resolutionx: int, resolutiony: int, image_byte: io.BytesIO) -> Image:
        x = resolutionx
        y = resolutiony
        im: Image = Image.open(image_byte)
        return self.convert_to_byte(im.resize((x, y)))

    def save_image(self, image_byte, file_extension: str = 'jpg', index: int = None, name: str = None) -> Image:
        image = ImageModel.objects.create(
            content=image_byte,
            file_extension=file_extension,
        )
        image.name = f"Face{image.id}"
        image.index = image.id
        return image

    def update_image(self, pk: int, params: dict):
        im = ImageModel.objects.get(pk=pk)
        {setattr(im, k, v) for k, v in params.items()}
        im.save()

    def convert_to_byte(self, image: Image, encoder_name: str = 'raw'):
        return image.tobytes(encoder_name=encoder_name)
