from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('ckeditor/upload/', views.ck_editor_5_upload_file, name='ck_editor_5_upload_file')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
