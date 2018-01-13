from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #Django ahora redirigirá todo lo que vaya hacia 'http://127.0.0.1:8000/' a  blog.urls  y buscará más instrucciones allí.
    url(r'',include('blog.urls')),
]
