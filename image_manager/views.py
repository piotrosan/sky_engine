from django.shortcuts import render
from django.views import View

from image.image_worker import ImageWorker

class GalleryView(View):
    template_name = 'gallery.html'

    def get(self, request, *args, **kwargs):
        #  set page to 1 because i think i dont have enough time to finish it
        return render(
            request,
            self.template_name,
            {
                'gallery_list': ImageWorker.get_paginated_image_from_databse(page=1)
            }
        )



class ImageView(View):
    template_name = 'image.html'

    def post(self, request, *args, **kwargs):
        ImageWorker.save_image()
        return self.render_the_same(request)

    def get(self, request, *args, **kwargs):
        #  set page to 1 because i think i dont have enough time to finish it
        return render(
            request,
            self.template_name,
            {
                'image': ImageWorker.get_binary_imag_from_remote()
            }
        )

    def patch(self, request, *args, **kwargs):
        pass
