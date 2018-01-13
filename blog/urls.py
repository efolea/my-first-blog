from django.conf.urls import include, url
from . import views

urlpatterns = [
	#r'^$' representa una cadena vacia
	url(r'^$',views.post_list),
]