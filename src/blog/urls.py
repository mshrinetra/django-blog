from django.urls import path

from blog.views import (
    blog_list_page,
    blog_view_page,
    blog_new_page
)

urlpatterns = [
    path("list/", blog_list_page),
    path("view/<str:slug>/", blog_view_page),
    path("new/", blog_new_page),
]
