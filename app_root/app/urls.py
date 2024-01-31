from django.contrib import admin
from django.urls import include, path

from app.settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
]

if DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]

# Маршруты
# www.site.com/admin

# www.site.com
# www.site.com/about

# www.site.com/catalog
# www.site.com/catalog/product
