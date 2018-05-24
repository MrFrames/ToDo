from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from todoapp import views

app_name = 'todoapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^$',views.IndexView.as_view(),name='index'),
    #url(r'^ new/$',views.newpage,name='newpage'),
    # todoapp/1
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail',)
    # Experiment with regex, below checks for id= and then some value,
    # passes the id value to the view named code_view
    #path(r'^u(?P<task_code>[0-9])/$', views.UpdateView,
    #     name='UpdateView')
]