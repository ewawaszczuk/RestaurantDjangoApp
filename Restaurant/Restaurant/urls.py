"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from FrescoBasilico.views import DashboardView, AboutUsView, MenuView, BlogView, ContactView, ElementsView, AddReservationView, LeaveACommentView, reservation_modify_id, ModificationView
from User import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from User.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^$", DashboardView.as_view(), name="dashboard"),
    url(r'^contact/', ContactView.as_view(), name="contact"),
    url(r'^about_us/', AboutUsView.as_view(), name="about_us"),
    url(r'^menu/', MenuView.as_view(), name="menu"),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='User/login.html'), name='login'),
    path('accounts/profile/', DashboardView.as_view(), name="dashboard"),
    path('log-out/', auth_views.LogoutView.as_view(template_name='FrescoBasilico/index.html'), name = 'logout_home'),
    url(r'^add-reservation/$', AddReservationView.as_view(), name="add"),
    url(r'^leave-a-comment/$', LeaveACommentView.as_view(), name="comment"),
    path('profile/', user_views.profile, name='profile'),
    path('modification/', ModificationView.as_view(), name='modification'),
    url(r'^reservation/(?P<id>\d+)', reservation_modify_id.as_view(), name = "modify" ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
