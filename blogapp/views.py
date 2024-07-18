from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
from .models import BlogPost

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
        uploaded_file = request.FILES.get('upload')
        response = upload(request)
        
        # Check if it's a single file or multiple files
        if isinstance(response, list):
            # Multiple files uploaded
            urls = [file_data['url'] for file_data in response]
        else:
            # Single file uploaded
            urls = [response.url]

        return JsonResponse({
            'urls': urls,
            'uploaded': True,
        })
    return JsonResponse({'error': 'Invalid request method or no file uploaded'}, status=400)
