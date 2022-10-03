from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('',views.front_page, name='front_page'),
    path('signup/',views.sign_up, name='sign_up'),
    path('login/',auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
