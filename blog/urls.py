from django.urls import path
from . import views
urlpatterns = [
    path('mg/', views.mg_page),
    path('gw/', views.gw_page),
    path('sj/', views.sj_page),
    path('je/', views.je_page),
    path('sy/', views.sy_page),
    path('<int:value>/', views.single_post_page),
    path('', views.index),
]
# 나중에 채움