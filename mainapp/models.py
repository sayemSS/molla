from django.db import models

# Create your models here.
class product(models.Model):
    p_name = models.CharField(max_length=50)
    p_img = models.ImageField(upload_to="my_informatin")
    p_det = models.TextField()


