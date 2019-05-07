"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from .views import (
    home_page,
    example_httpresponse,
    example_regexurl,
    example_render,
    example_planetemplate,
    example_contexttemplate,
    example_contextprocessor,
    example_form
)

urlpatterns = [
    path("", home_page),
    path("blog/", include("blog.urls")),
    path("httpresponse/", example_httpresponse),
    path("form/", example_form),
    re_path("^regexurl?/$", example_regexurl),
    # RegEx Path e.g. for both /page & /pages
    path("render/", example_render),
    path("planetemplate/", example_planetemplate),
    path("contexttemplate/", example_contexttemplate),
    path("contextprocessor/", example_contextprocessor),
    path('site-admin/', admin.site.urls),
]
