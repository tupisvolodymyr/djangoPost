from django.http import JsonResponse
from .models import Post

def post_list(request):
    posts = list(Post.objects.values())
    return JsonResponse(posts, safe=False)
