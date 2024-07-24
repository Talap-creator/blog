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

def ck_editor_5_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES.get('upload')
        
        # Define the file path where the file will be saved
        file_path = os.path.join(settings.MEDIA_ROOT, 'blog_images', uploaded_file.name)
        
        # Save the file to the media directory
        file_url = default_storage.save(file_path, uploaded_file)
        file_url = os.path.join(settings.MEDIA_URL, 'blog_images', uploaded_file.name)

        return JsonResponse({
            'url': file_url,
            'uploaded': True,
        })
    return JsonResponse({'error': 'Invalid request method or no file uploaded'}, status=400)
