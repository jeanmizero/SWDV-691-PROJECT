from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User





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
        
    # Get category url
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
        
    # def get_image(self): 
    #     if not self.image == '' or None:
    #         return self.image.url
    #     else:
    #         return None
    
    # Get product url   
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
        
    # Display output
    def __str__(self):
        return self.name

# Creaate Cart Product Order  model class
class Cart(models.Model):
    cart_id = models.CharField(max_length = 250, blank = True)
    date_added = models.DateField(auto_now_add = True)
    
    class Meta:
        db_table ='Cart'
        ordering =['date_added']
        
    # Display output
    def __str__(self):
        return self.cart_id
    
#  Create cart item model class for single product add to the cart
class CartItem(models.Model): 
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table ='CartItem'
        
    # Calculate sub total
    def sub_total(self):
        return self.product.price * self.quantity
    
    # Display output
    def __str__(self):
        return self.product 
    
#  Create order item model class     
class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(max_length=250, blank=True, verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=250, blank=True)
    billingCountry = models.CharField(max_length=250, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostcode = models.CharField(max_length=250, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)

#  Create order item model class
class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='USD Price')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def sub_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.product  

# Review Model
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return self.content

# Create your models here.
