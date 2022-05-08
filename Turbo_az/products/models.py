from django.db import models

# Create your models here.

class Category(models.Model):
  category_name = models.CharField(max_length = 50)

  def __str__(self):
    return self.category_name


class Product(models.Model):
  product_name = models.CharField(max_length = 200)
  product_description = models.CharField(max_length = 200)
  product_price = models.PositiveIntegerField(default = "-")
  product_img = models.ImageField(upload_to = 'images')
  category = models.ForeignKey(Category, on_delete = models.SET_NULL, null = True, blank = True)
  choose = models.BooleanField(default = False)
  slug = models.SlugField()

  def __str__(self):
    return self.product_name