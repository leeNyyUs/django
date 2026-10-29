
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("users/", views.users_list, name="users_list"),
    path("users/<str:username>/", views.user_info, name="user_info"),
    path("forum/", views.forum, name="forum"),
    path("contacts/", views.contacts, name="contacts"),
    path("archive/", views.archive, name="archive"),
]
