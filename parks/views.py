from django.shortcuts import render, redirect
from .forms import ParkForm, CommentForm
from .models import Park, Comment

# Create your views here.


def park_list(request):
    parks = Park.objects.all()
    return render(request, 'parks/park_list.html', {'parks': parks})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'parks/comment_list.html', {'comments': comments})

def park_detail(request, pk):
    park = Park.objects.get(id=pk)
    return render(request, 'parks/park_detail.html', {'park': park})

def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'parks/comment_detail.html', {'comment': comment})

def park_create(request):
    if request.method == 'POST':
        form = ParkForm(request.POST)
        if form.is_valid():
            park = form.save()
            return redirect('park_detail', pk=park.pk)
    else:
        form = ParkForm()
    return render(request, 'parks/park_form.html', {'form': form})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm()
    return render(request, 'parks/comment_form.html', {'form': form})

def park_edit(request, pk):
    park = Park.objects.get(pk=pk)
    if request.method == "POST":
        form = ParkForm(request.POST, instance=park)
        if form.is_valid():
            park = form.save()
            return redirect('park_detail', pk=park.pk)
    else:
        form = ParkForm(instance=park)
    return render(request, 'parks/park_form.html', {'form': form})

def comment_edit(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'parks/comment_form.html', {'form': form})

def park_delete(request, pk):
    Park.objects.get(id=pk).delete()
    return redirect('park_list')

def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')
