from django.urls import path
from . import views
app_name = 'regapp'


urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', views.login_vew, name='login'),
    path('logout', views.logout, name="logout"),


]
