from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',) #сортування за ім'ям в категоріях
        verbose_name_plural='Категорії' # вивід назви категорій

    def __str__(self):
        return self.name # як відображається ім'я
    
class Item(models.Model):
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)#категорія
    name = models.CharField(max_length=255) #назва 
    descriptions=models.TextField(blank=True,null=True) # опис
    image = models.ImageField(upload_to='item_images',blank=True,null=True) # картинка
    price = models.FloatField() # ціна
    is_sold=models.BooleanField(default=False) # чи продано
    created_by = models.ForeignKey(User, related_name='items',on_delete=models.CASCADE)# хто створив
    created_at = models.DateTimeField(auto_now=True)# коли створенно

    class Meta:
        ordering = ('name',) #сортування за ім'ям 
       

    def __str__(self):
        return self.name # як відображається ім'я