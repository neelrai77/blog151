from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from App_Blog.admin import blog_site
urlpatterns = [
    path('blog_admin/', blog_site.urls),
    path('admin/', admin.site.urls),
    path('account/', include('App_Login.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('blog/', include('App_Blog.urls')),

    path('', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Main Admin Panel"
admin.site.site_header= "Main Admin"
admin.site.site_title= "Main Admin"
