from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import BlogPost

def blogs(request):
    posts = BlogPost.objects.all()
    data = {
        'blogs': [{
            'id':post.id,
            'category': post.category,
            'title': post.title,
            'content': post.content,
            'short_description': post.short_description,
            'created_at': post.created_at.strftime('%d %B, %H:%M'),
            'updated_at': post.updated_at.strftime('%d %B, %H:%M'),
            'image':post.image.url if post.image else None,
        } for post in posts]
    }
    return JsonResponse(data)

@csrf_exempt
def ck_editor_5_upload_file(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        file_url = settings.MEDIA_URL + uploaded_file.name
        try:
            with open(settings.MEDIA_ROOT + uploaded_file.name, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return JsonResponse({'uploaded': True, 'url': file_url})
        except Exception as e:
            return JsonResponse({'uploaded': False, 'error': str(e)})
    return JsonResponse({'uploaded': False, 'error': 'Invalid request'})
