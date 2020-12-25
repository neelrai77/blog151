from django.contrib import admin
from .models import Blog,Comment,Likes
# TEXT = 'Some text we can include'
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','publish_date','upload_date','author')
    fieldsets = (
        ('Section1', {
            'fields':('blog_title','author'),
            
        }),
        ('Section2',{
            'fields':('slug','blog_image'),
            'classes': ('collapse',),
        }),
        


    )
admin.site.register(Blog,BlogAdmin)
blog_site = BlogAdminArea(name='BlogAdmin2')
blog_site.register(Blog)
blog_site.register(Comment)
blog_site.register(Likes)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog',  'comment_date')
    list_filter = ('comment_date',)
    search_fields = ('comment_date',)
admin.site.register(Comment, CommentAdmin)

admin.site.register(Likes)