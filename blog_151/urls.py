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
    path('accounts/', include('django.contrib.auth.urls')), 
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('blog/', include('App_Blog.urls')),

    path('', views.index, name='index'),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
        name='password_reset_complete'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Main Admin Panel"
admin.site.site_header= "Main Admin"
admin.site.site_title= "Main Admin"
