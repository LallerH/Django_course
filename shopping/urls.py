from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('customers', views.get_customers, name='customers'),
    path('customers/add/', views.add_customer, name='customer_add'),
    path('customers/<customer_id>/', views.get_customer_details, name='customer_details'),
    path('products', views.get_products, name='products'),
    path('products/<product_id>/', views.get_product_details, name='product_details'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)