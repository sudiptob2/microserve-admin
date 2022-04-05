from django.contrib import admin
from django.urls import path, include

from products import urls as product_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(product_urls)),
]
