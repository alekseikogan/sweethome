from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
]

if DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

# Маршруты
# www.site.com/admin

# www.site.com
# www.site.com/about

# www.site.com/catalog
# www.site.com/catalog/product
