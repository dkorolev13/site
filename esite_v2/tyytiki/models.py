from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField('Ссылка', max_length=200, db_index=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})


class Product(models.Model):
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    name = models.CharField('Название', max_length=100, db_index=True)
    slug = models.SlugField('Ссылка', max_length=200, db_index=True, unique=True)
    image = models.ImageField('Изображение', upload_to='photos/%Y/%m/%d/')
    description = models.TextField('Описание', max_length=1000, blank=True)
    price = models.IntegerField('Цена', default=0)
    posted = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('prod', kwargs={'prod_id': self.pk})

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'
