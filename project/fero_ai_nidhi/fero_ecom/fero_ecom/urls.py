from django.contrib import admin
from django.urls import path, include
from fero_ecom_app.urls import urlpatterns as app_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(app_urls)),
]
