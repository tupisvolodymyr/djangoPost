from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from .models import Post
from django.views.decorators.csrf import csrf_exempt # це як раз саме імпортує цей захист токену

@csrf_exempt # цей декоратор дозволяє вимкнути перевірку на CSRF-токен
def post_list(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body) # Записуємо ці дані з запиту "POST"
            author = User.objects.first()

            new_post = Post.objects.create(
                title=data.get('title'),
                content=data.get('content'),
                author=author  # Тут додаємо автора, тому що в "views.py" вказано що автор "IS NOT NULL" тобто обовʼязковий, а в нас його немає
            )
            return JsonResponse({"message": "Post created!", "id": new_post.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    posts = list(Post.objects.values()) # Якщо запит "GET" просто повертаємо список
    return JsonResponse(posts, safe=False)