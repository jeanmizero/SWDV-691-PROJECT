from django.db import models
from django.urls import reverse
# Add Categories Models
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    
    class Meta:
        # sort by name
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def get_url(self):
      return reverse('products_by_category', args=[self.slug])
      
    # Display output
    def __str__(self):
        return self.name
    
# Create Product Class Model
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    # Category relationship
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        # sort by name
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    # Display output
    def __str__(self):
        return self.name
      
    

# Create your models here.
