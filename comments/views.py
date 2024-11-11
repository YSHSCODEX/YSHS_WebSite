from django.shortcuts import render, redirect
from .models import Comment

def add_comment(request):
    if request.method == 'POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        Comment.objects.create(author=author, content=content)
        return redirect('comment_list')  # 댓글 목록 페이지로 이동

    return render(request, 'comments/add_comment.html')
