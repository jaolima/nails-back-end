from django.db import models


class Base(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(Base):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


class Products(Base):
    color = models.CharField(max_length=255)
    alias_color = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    qtd = models.DecimalField(max_digits=2, decimal_places=2)
    type = models.CharField(max_length=99)
    size = models.DecimalField(max_digits=2, decimal_places=2)
    barcode = models.TextField(unique=True),
    uri_image = models.CharField(max_length=1000)
    price = models.FloatField()
    top_products = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=2, decimal_places=2)
    category = models.ForeignKey(Category, related_name='categorys', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
