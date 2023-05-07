from django.contrib.auth.models import User
# from sre_constants import Category
from django.db import models

# Create your models here.

class  Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    quantity = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

         # def get_absolute_url(self):
        #  return reverse('store:category_list', args=[self.Slug])
       
        

    def __str__(self):
         return self.name

    class Product(models.Model):
        id = models.CharField(max_length=20)
        title = models.CharField(max_length=255, db_index=True)
        # slug = models.SlugField(max_length=255, unique=True)
        price = models.DecimalField(max_digits=4, decimal_places=2)
        category = models.ForeignKey( Category, on_delete=models.PROTECT, related_name='categories')
        description = models.TextField(blank=True)
        image = models.ImageField(upload_to='images/')


    class Meta:
        verbose_name_plural = 'Products'  
        # ordering = ('-created', )  

    def __str__(self):
        return super.name

