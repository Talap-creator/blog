from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from .models import BlogPost
from django.core.files.storage import default_storage
import logging

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

logger = logging.getLogger(__name__)

@csrf_exempt
def ck_editor_5_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        try:
            uploaded_file = request.FILES['upload']
            file_path = os.path.join('blog_images', uploaded_file.name)
            saved_path = default_storage.save(file_path, ContentFile(uploaded_file.read()))
            file_url = default_storage.url(saved_path)
            return JsonResponse({
                'url': file_url,
                'uploaded': True,
            })
        except Exception as e:
            logger.error(f"File upload failed: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method or no file uploaded'}, status=400)
