from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.png',upload_to='profile_pics')
    skills=models.CharField(max_length=50,default='-')

    def __str__(self):
        return str(self.user.username)

    def save(self,*args,**kwargs):
        super().save()
        img=Image.open(self.image.path)

        if img.height >300 or img.width >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)




