from django.contrib import admin
from django.urls import path,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),
    path('orders/', include('orders.urls')),
]
