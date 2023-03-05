from django.urls import path
# import the app views
from coopApp import views

# This url is for the core app operations mainly for posting
# updating for the admin users such as Financial secretary, 
# Chairman, financial treasurer and loan committees

#Register your app
# app_name='coopApp'

urlpatterns = [
    path('showCoopApp/', views.showCoopApp , name='coopApp_showCoopApp'),
    # path('register/', views.register, name='easyCoop_register'),
    # path('myShow/', views.myShow, name='easyCoop_myShow'),
    
 ]