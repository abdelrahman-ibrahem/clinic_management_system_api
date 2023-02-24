from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# SETUP SWAGGER 
schema_view = get_schema_view(
   openapi.Info(
      title="Clinic Management System",
      default_version='v1',
      description="Designed and Developed by Abdelrahman Ibrahem Abdelkader",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('auth/', include('dj_rest_auth.urls')),
   path('auth/register', include('dj_rest_auth.registration.urls')),
   path('users/', include('users.urls')),
   path('clinic/', include('clinic.urls')),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
# ADD STATIC FILES
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)