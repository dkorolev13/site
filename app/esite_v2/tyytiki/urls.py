from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .views import *

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("products/", all_products, name="products"),
    path("prod/<int:prod_id>/", show_prod, name="prod"),
    path("category/<int:cat_id>/", show_category, name="category"),
]
