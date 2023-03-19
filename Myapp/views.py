from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post

# Create your views here.
def homepage(request):
    posts =Post.objects.all()
    context = { 'posts':posts}
    return render(request, 'Myapp/homepage.html',context)

def addjoke(request):
    if request.method == 'POST':
        content = request.POST['content']
        name = request.POST['name']
        post = Post(content=content, name=name)
        try:
            post.save()
            messages.success(request, 'Your submission has been saved.')
            return redirect('homepage')
        except ValidationError as e:
            messages.error(request, e.message)
    return render(request, 'Myapp/addjoke.html')


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Post
def joke(request, id):
    # Retrieve the post object with the specified ID
    post = get_object_or_404(Post, id=id)

    # Create a dictionary of the post's data
    post_dict = {
        'id': post.id,
        'name': post.name,
        'content': post.content,
    }

    # Return the post's data as a JSON response
    return JsonResponse(post_dict)