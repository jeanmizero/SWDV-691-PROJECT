# from django.urls import path
# from . import views

# urlpatterns = [
#     # Homepage url
#     path('', views.home, name ="home"),
#     path('category/<slug:category_slug>', views.home, name="products_by_category"),
#     # Aboutpage url
#     path('category/<slug:category_slug>/<slug:product_slug>', views.productPage, name ="product_detail"),
#     # Create cart url
#     # cart
#     # path('cart',views.cart, name='cart'),
#     path('cart', views.cart_detail, name ='cart_detail'),
#     path('cart/add/<int:product_id>', views.add_cart, name="add_cart"),
#     # remove item
#     path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
#     # Delete item/cart

# ]

from django.urls import path
from . import views

urlpatterns = [
    # Homepage url
    path('', views.home, name ='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    # Aboutpage url
    path('category/<slug:category_slug>/<slug:product_slug>', views.productPage, name ='product_detail'),
    # Create cart url
    # cart
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name ='cart_detail'),
    # remove item
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    # Delete item/cart
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    # Thanks page
    path('thankyou/<int:order_id>', views.thanks_page, name='thanks_page'),
    # Sign up
    path('account/create/', views.signupView, name='signup'),
    # Login 
    path('account/signin/', views.signinView, name='signin'),
    # View account
    path('account/signout/', views.signoutView, name='signout'),
    # View history
    path('order_history/', views.orderHistory, name='order_history'),
    path('order/<int:order_id>', views.viewOrder, name='order_detail'),
    # Search
    path('search/', views.search, name='search'),
    # Contact
    path('contact/', views.contact, name='contact')
]