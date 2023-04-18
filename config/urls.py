from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),
    # Local apps
    path('blog/', include('blog.urls', namespace='blog'))
]
