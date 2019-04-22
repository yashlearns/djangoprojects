
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.log_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.reg_user, name='register'),
    path('count/',views.count,name='count'),
    path('count1/',views.count1,name='count1'),
    path('secondhome/',views.secondhome,name='secondhome'),
    path('index/',views.index,name='index'),
    path('add/',views.add,name='add'),
    path('submit',views.submit,name='submit'),
    path('about/',views.about,name='about')
    

    
]
