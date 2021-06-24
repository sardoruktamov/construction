from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post, Commit, Post_categories
from .forms import CommentForm, PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormView
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.db.models import Q




def blog(request):
    posts = Post.objects.all()[:5]      # section qismiga ma`lumot chiqarish uchun
    all_posts = Post.objects.all()[:5] #popular pos bo'limiga ma'lumot chiqarish uchun ikkimarta ikki xil o'zgaruvchi qilib olindi
    common_tags = Post.tags.most_common()[:12]
    categories = Post_categories.objects.all()    
    pgn = Paginator(posts, 3)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)
    
    context = {
        'posts':page,
        'common_tags':common_tags,
        'categories':categories,
        'all_posts':all_posts
        }
    return render(request, 'blog.html', context)


def search(request):
    all_posts = Post.objects.all()[:5]
    common_tags = Post.tags.most_common()[:12]

    all_categories = Post_categories.objects.all()
    search_post = request.GET.get('search') 
    if search_post:
        posts = Post.objects.filter(Q(title__icontains=search_post) | Q(text_body1__icontains=search_post) | Q(text_body2__icontains=search_post))
    else:
        posts = Post.objects.all()

    pgn = Paginator(posts, 3)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)
    
    context =  {
        'posts':page,
        'common_tags':common_tags,
        'categories':all_categories,
        'all_posts':all_posts
        }
    return render(request, 'blog.html', context)


def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    
    categories = Post_categories.objects.all()
    common_tags = Post.tags.most_common()[:12]
    all_posts = Post.objects.all()[:5]
    # postlarni tag lar bilan filtrlaymiz 
    posts = Post.objects.filter(tags=tag)

    pgn = Paginator(posts, 3)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    context = {
        'tag':tag,
        'posts':page,
        'common_tags':common_tags,
        'categories':categories,
        'all_posts':all_posts
    }
    return render(request, 'blog.html', context)

def categorie(request, id):
    categories = get_object_or_404(Post_categories, pk=id)
    common_tags = Post.tags.most_common()[:12]
    all_posts = Post.objects.all()[:5]
    
    all_categories = Post_categories.objects.all()
    posts = Post.objects.filter(categorie=categories)

    pgn = Paginator(posts, 3)
    page_nums = request.GET.get('page',1)

    try:
        page = pgn.page(page_nums)
    except EmptyPage:
        page = pgn.page(1)

    context = {
        'posts':page,
        'common_tags':common_tags,
        'categories':all_categories,
        'all_posts':all_posts
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    categories = Post_categories.objects.all()
    comments = Commit.objects.filter(post=post, reply=None)

    post_object=Post.objects.get(slug=slug)
    post_object.post_view = post_object.post_view + 1
    post_object.save()

    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Commit.objects.get(id=reply_id)

            new_comment = comment_form.save(commit=False)
            new_comment.reply = comment_qs
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return HttpResponseRedirect(request.path)
    else:
        comment_form = CommentForm()
    return render(request,'single-blog.html', {'post':post, 
                                                'comments':comments,
                                                'new_comment':new_comment,
                                                'comment_form':comment_form,
                                                'categories':categories
                                                })

