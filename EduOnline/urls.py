"""EduOnline URL Configuration

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
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve

import xadmin

from apps.users.views import NamePsdLoginView, LogoutView, SendSmsView, DynamicLoginView, RegisterView
from EduOnline.settings import MEDIA_ROOT
from apps.operations.views import IndexView

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('login/', NamePsdLoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register"),
    path('d_login/', DynamicLoginView.as_view(), name="d_login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    url(r'^captcha/', include("captcha.urls")),
    url(r'^send_sms/', csrf_exempt(SendSmsView.as_view()), name="send_sms"),
    # 媒体文件url
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve, {"document_root": STATIC_ROOT}),
    # 机构相关页面
    url(r'^org/', include(("apps.origanizations.urls", "origenizations"), namespace="org")),
    # 用户相关操作
    url(r'^op/', include(("apps.operations.urls", "operations"), namespace="op")),
    # 课程相关页面
    url(r'^course/', include(("apps.courses.urls", "courses"), namespace="course")),
    # 个人中心
    url(r'^users/', include(("apps.users.urls", "users"), namespace="users")),
]
