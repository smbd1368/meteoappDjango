from django.urls import path

import users.views as views


urlpatterns = [
    path('login/', views.login, name="users_login"),
    path('logout/', views.logout, name="users_logout"),
    path('settings/', views.settings, name="users_settings"),
    path('/', views.home, name="users_home"),
]
