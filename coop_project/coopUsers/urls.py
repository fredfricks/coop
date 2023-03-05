from django.urls import path
# import app views
from coopUsers import views


#Register your app
# app_name='easyCoop'

urlpatterns = [
    path('', views.index, name='coopUsers_index'),
    
    # path('register/', views.register, name='easyCoop_register'),
    # path('myShow/', views.myShow, name='easyCoop_myShow'),
    
 ]