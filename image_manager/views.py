from django.shortcuts import render
from django.views import View
from django.http import Http404

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
        image_byte = request.POST['image']
        ImageWorker.save_image(image_byte)
        return render(
            request,
            self.template_name,
            {
                'image': ImageWorker.get_binary_imag_from_remote()
            }
        )

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                'image': ImageWorker.get_binary_imag_from_remote()
            }
        )

    def patch(self, request, *args, **kwargs):
        index = request.POST['index']
        pk = request.POST['pk']
        ImageWorker.set_index(pk, index)


def gallery_preview(request, index):
    try:
        ImageWorker.get_image_from_database(index)
    except :
        raise Http404("Poll does not exist")
    return render(request, "polls/detail.html", {"poll": p})
