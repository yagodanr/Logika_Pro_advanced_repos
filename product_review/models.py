from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    
    class Meta:
        verbose_name = ("product")
        verbose_name_plural = ("products")

    def __str__(self):
        return self.name

    
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("review")
        verbose_name_plural = ("reviews")

    def __str__(self):
        return f"{self.id} : {self.product} : {self.author}"