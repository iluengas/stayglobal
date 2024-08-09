from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,
                            verbose_name="Category Name")
    description = models.TextField(blank=True, verbose_name="Description")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Product Name")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products", verbose_name="Category")
    description = models.TextField(blank=True, verbose_name="Description")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Price")
    image = models.ImageField(
        upload_to="products/", blank=True, null=True, verbose_name="Product Image")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
