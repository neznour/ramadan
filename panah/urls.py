from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Configure Admin Title
admin.site.site_header ="MY E-center Administration Page"
admin.site.site_title= "Browser Title"
admin.site.index_title = "Welcome to the Admin Area"