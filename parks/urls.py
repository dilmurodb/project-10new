from django.urls import path
from . import views

urlpatterns = [
    path('', views.park_list, name='park_list'),
    path('comments/', views.comment_list, name='comment_list'),
    path('parks/<int:pk>', views.park_detail, name='park_detail'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('parks/new', views.park_create, name='park_create'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('parks/<int:pk>/edit', views.park_edit, name='park_edit'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('parks/<int:pk>/delete', views.park_delete, name='park_delete'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete')
]