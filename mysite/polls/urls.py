
import imp
from os import name
from urllib import request
from django.urls import path 
from .views import IndexClass , LoginClass , BccClass , NewsView ,  PersonalClass , WorkexperienceCLass  , AcademiClass , TableClass , Table1Class , Table2Class , HextimeconvertClass, TelegramClass, TestClass


app_name = "demo"
 
urlpatterns = [
    
    path('', IndexClass.as_view()),
    path('login/', LoginClass.as_view(), name= "login"),
    path('BCC/', BccClass.as_view(), name= "BCC"),
    path('Hex-time-convert/', HextimeconvertClass.as_view(), name= "hex-time-convert"),
    path('news/', NewsView.as_view(), name= "news"), 
    path('personal-info/', PersonalClass.as_view(), name= "personal-info"),
    path('work-experience/', WorkexperienceCLass.as_view(), name= "work-experience"),
    path("academi/", AcademiClass.as_view(), name="academi"),
    path("table/", TableClass.as_view(), name="table"),
    path("table1/", Table1Class.as_view(), name="table1"),
    path("table2/", Table2Class.as_view(), name="table2"),
    path("telegram/", TelegramClass.as_view(), name="telegram"),
    path("test/", TestClass.as_view(), name="test"),




]
