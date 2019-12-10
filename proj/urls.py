from django.contrib import admin
from django.urls import path
from proj import views
from django.conf.urls import url,include
urlpatterns = [
    path('',views.index,name="index"),
    path('admin/', admin.site.urls),
    path('register/',views.register, name="register"),
    path('homepage/',views.homepage,name="homepage"),
    path('/search/', views.search, name="search"),
    path('/add/', views.add, name="add"),
    path('addpre/',views.addpre,name="addpre"),
    path('/view/',views.view,name="view"),
    path('prof/',views.prof,name='prof'),
    path('/userprof/',views.userprofile,name="userprof"),
    path('pres/',views.pres,name="presc")
]
