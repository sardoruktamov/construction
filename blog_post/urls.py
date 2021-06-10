from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blogpost'),
    path('search', views.search, name='search_post'),
    path('categorie/<int:id>', views.categorie, name='post_categorie'),
    # path('addpost/',views.BlogCreateView.as_view(), name='post_new'),
    path('blog-detail/<slug:slug>', views.blog_detail, name='blog-detail'),
    path('<slug:slug>/',views.blog_detail,name='post_detail'),
    path('tag/<slug:slug>/', views.tagged, name = 'tagged')
]