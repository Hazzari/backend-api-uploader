from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('src.routers')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
