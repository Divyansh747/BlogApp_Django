from django.conf.urls import patterns, include, url
from blog import views
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SimpleBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^addblog/', views.createBlog, name="create"),
)

