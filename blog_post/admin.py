from django.contrib import admin
from .models import Post, Post_categories, Commit

# Register your models here.
admin.site.register(Post_categories)
# admin.site.register(Post)
# admin.site.register(Commit)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title', 'categorie','date']
#     prepopulated_fields = {'slug':('title',)}
    


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