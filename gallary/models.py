from django.db import models

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=50)
    p_height = models.PositiveIntegerField(blank=True)
    description = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/cat/', height_field='p_height')

    def __str__(self) -> str:
        return self.name +str(self.id ) 

class Pics(models.Model):
    name = models.CharField(max_length=50)
    decription = models.CharField(max_length=80,blank=True)
    p_height = models.PositiveIntegerField(blank=True,default='360')  
    cat = models.ForeignKey(Cat,on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/pics/',height_field='p_height',blank=True)

    def __str__(self) -> str:
        return self.name + str("|") + self.cat.name

    def get_Img(self):
        img_url = ''
        try:
            img_url = self.img.url 
        except:
            img_url = self.img.get()
        return img_url