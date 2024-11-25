from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django_bongo import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('machine_learning.urls')),
    path('receipe/', include('receipe_app.urls')),
    # path(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root', settings.STATIC_URL})

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += staticfiles_urlpatterns()    
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)