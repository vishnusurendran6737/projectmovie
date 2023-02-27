from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')
    #                       height_filed='image_height', width_field='image_width')
    # image_height=models.PositiveIntegerField(null=True,blank=True, editable=False,default='100')
    # image_width=models.PositiveIntegerField(null=True,blank=True, editable=False,default='100')
    def __str__(self):
        return self.name