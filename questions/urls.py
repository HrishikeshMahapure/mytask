from django.urls import path
from . import views


urlpatterns = [
	path('',views.indexview,name='index'),
	path("query",views.queryview,name="query"),
    ]


