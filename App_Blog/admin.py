from django.contrib import admin
from .models import Blog,Comment,Likes
# TEXT = 'Some text we can include'
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'

class BlogAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Section1', {
            'fields':('blog_title','author'),
            
        }),
        ('Section2',{
            'fields':('slug','blog_image'),
            'classes': ('collapse',),
        }),
        


    )

blog_site = BlogAdminArea(name='BlogAdmin2')
blog_site.register(Blog)
blog_site.register(Comment)
blog_site.register(Likes)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Likes)