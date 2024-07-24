from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from .models import BlogPost
from django.core.files.storage import default_storage

def blogs(request):
    posts = BlogPost.objects.all()
    data = {
        'blogs': [{
            'id': post.id,
            'category': post.category,
            'title': post.title,
            'content': post.content,
            'short_description': post.short_description,
            'created_at': post.created_at.strftime('%d %B, %H:%M'),
            'updated_at': post.updated_at.strftime('%d %B, %H:%M'),
            'image': post.image.url if post.image else None,
        } for post in posts]
    }
    return JsonResponse(data)

@csrf_exempt
def ck_editor_5_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', uploaded_file.name)
        path = default_storage.save(save_path, uploaded_file)
        url = default_storage.url(path)

        return JsonResponse({
            'url': url,
            'uploaded': True,
        })
    return JsonResponse({'error': 'Invalid request method or no file uploaded'}, status=400)
