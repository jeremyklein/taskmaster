"""tasks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, signup

urlpatterns = [
    url(r'^list/$', TaskListView.as_view(),name = "task_list"),
    url(r'^add/$', TaskCreateView.as_view(), name = "task_add"),
    url(r'^edit/(?P<pk>\d+)/$', TaskUpdateView.as_view(), name='task_edit',),
    url(r'^delete/(?P<pk>\d+)/$', TaskDeleteView.as_view(), name='task_delete',),
    url(r'^signup/$', signup, name='signup')
]
