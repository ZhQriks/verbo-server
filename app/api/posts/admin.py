from django.contrib import admin
from app.api.posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('explanation', 'mediaUrl', 'transcript', 'isPhoto', 'viewCount')  # Fields to display in the admin list
    list_filter = ('isPhoto', 'transcript', 'explanation')  # Filters on the right sidebar
    search_fields = ['isPhoto', 'transcript', 'explanation']  # Fields to search in the admin

admin.site.register(Post, PostAdmin)
