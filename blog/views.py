from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST

class PostListView(ListView):
    queryset = Post.published.all() # or model = Post, but then we haved Post.objects.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/blog_list.html'

def post_detail(request, year, month, day, post, id):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, 
                            slug=post,
                            id = id,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'blog/post/post_detail.html',{
        'post': post,
        'comments': comments,
        'form': form})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data # return dict with valid fields
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'kostya.tupalo@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent,
    })

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post # set wich post relate comment
        comment.save()
    return render(request, 'blog/post/comment.html', {
        'post': post,
        'form': form,
        'comment': comment,
    })
