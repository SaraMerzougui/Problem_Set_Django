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



from .forms import JokeForm
def addjoke(request):
    if request.method == 'POST':
        form = JokeForm(request.POST)
        if form.is_valid():
            # save the post to the database
            form.save()
            # redirect to the homepage
            return redirect('homepage')
    else:
        form = JokeForm()
    return render(request, 'Myapp/addjoke.html',{'form':form})



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