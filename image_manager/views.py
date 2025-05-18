import ipdb
from django.shortcuts import render
from django.views import View
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt

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

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        ipdb;ipdb.set_trace()
        image_byte = request.POST['image']
        ImageWorker.save_image(image_byte)
        return render(
            request,
            self.template_name,
            {}
        )

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                'image': ImageWorker.get_binary_imag_from_remote()
            }
        )

    @csrf_exempt
    def patch(self, request, *args, **kwargs):
        index = request.POST['index']
        pk = request.POST['pk']
        ImageWorker.set_index(pk, index)

def gallery_preview(request, index):
    try:
        image = ImageWorker.get_image_from_database(index)
    except :
        #  sorry for dump error
        raise Http404("SOme error")
    return render(request, "galery_preview.html", {'image': image})

def gallery(request, index):
    try:
        image = ImageWorker.change_index(index)
    except :
        #  sorry for dump error
        raise Http404("Some error")
    return render(request, "galery_preview.html", {'image': image})
