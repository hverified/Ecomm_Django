from django.urls import path
from .views import (shopIndexView, aboutView, contactView,
                    trackerView, searchView, productView, checkoutView)


urlpatterns = [
    path('', shopIndexView, name="ShopHome"),
    path('about/', aboutView, name="About"),
    path('contact/', contactView, name="Contact"),
    path('tracker/', trackerView, name="Tracker"),
    path('search/', searchView, name="Search"),
    path('product/<int:pid>', productView, name="Product"),
    path('checkout/', checkoutView, name="Checkout"),

]
