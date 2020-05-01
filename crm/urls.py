from django.conf.urls import url
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('golf_course_list', views.golf_course_list, name='golf_course_list'),
    path('golf_course/<int:pk>/edit/', views.golf_course_edit, name='golf_course_edit'),
    path('golf_course/<int:pk>/delete/', views.golf_course_delete, name='golf_course_delete'),
    path('golf_course/create/', views.golf_course_new, name='golf_course_new'),
    path('score_list', views.score_list, name='score_list'),
    path('score/<int:pk>/edit/', views.score_edit, name='score_edit'),
    path('score/<int:pk>/delete/', views.score_delete, name='score_delete'),
    path('score/create/', views.score_new, name='score_new'),
    path('golf_course/<int:pk>/score_compare/', views.score_compare, name='score_compare'),
]