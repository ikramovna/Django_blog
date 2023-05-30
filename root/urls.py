from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('users/', include('apps.users.urls')),
    path('blogs/', include('apps.blogs.urls')),
    path('crud/', include('apps.crud.urls')),


] + static(MEDIA_URL, document_root=MEDIA_ROOT)
