from django.conf import settings
from django.http import JsonResponse

class StaticFilesCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if settings.DEBUG:
            # Проверяем доступность папки staticfiles
            staticfiles_path = settings.STATIC_ROOT
            if not os.path.exists(staticfiles_path):
                message = f"Папка staticfiles ({staticfiles_path}) не существует или недоступна."
                print(message)
                if request.is_ajax():
                    return JsonResponse({'message': message}, status=500)
                else:
                    # Выводим alert только на странице, а не в админке
                    alert_script = """
                    <script>
                        alert("Папка staticfiles недоступна. Проверьте настройки сервера.");
                        console.log("Папка staticfiles недоступна. Проверьте настройки сервера.");
                    </script>
                    """
                    if not request.path.startswith('/admin/'):
                        response.content += alert_script.encode()
        return response
