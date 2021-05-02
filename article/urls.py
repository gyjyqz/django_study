"""article URL Configuration

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
from django.urls import path
from articles.views import get_html,get_content,get_or_create_articles,get_article_or_update_or_delete,register,login
from django.views.decorators.csrf import csrf_exempt
from articles import views as articles_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('html',get_html),
    path('content',get_content),
    #path('api/v1/articles',csrf_exempt(get_or_create_articles)),
    #path('api/v1/articles/<int:id>',csrf_exempt(get_article_or_update_or_delete)),
    path('api/v1/register',csrf_exempt(register)),
    path('api/v1/login',csrf_exempt(login)),
    path('api/v1/articles',csrf_exempt(articles_views.ArticlesView.as_view())),


]
