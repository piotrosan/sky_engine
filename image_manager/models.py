from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Image(models.Model):
    index = models.BigIntegerField(null=True, blank=True)
    content = models.BinaryField(null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)
    file_extension = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    publications = models.ManyToManyField(Gallery)


    def recreate_index(self):
        pass

