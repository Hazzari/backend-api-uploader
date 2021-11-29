from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

schema_view = get_schema_view(
    openapi.Info(
        title='Data Fort',
        default_version='v1',
        description='Image loader services',
        contact=openapi.Contact(email="dev.aleksan@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('upload/', include('src.image_uploader.urls')),
    path('token/access/', TokenRefreshView.as_view(), name='token_get_access'),
    path('token/both/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('', include('djoser.urls')),
]
