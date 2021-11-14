from django.contrib import admin
from .models import Post, Post_categories, Commit


# admin.site.register(Post_categories)

@admin.register(Post_categories)
class Post_categoriesAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)