
from django.contrib import admin
from django.urls import path, include
from todolist import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todolist_views.index, name = 'index'),
    path('task/', include('todolist.urls') ),
    path('account/', include('users_app.urls') ),
    path('hello', todolist_views.contact, name = 'hello'),
    path('abouts', todolist_views.about, name = 'abouts'),

]
