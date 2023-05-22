from django.urls import path, include
from . import views
# from views import all_data
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'datas',all_data,basename='datas')
urlpatterns = [

    path('', views.apiOverview, name='apioverview'),
    path('showall/',views.showAll, name='showall'),
    # path('show/<int:pk>/',views.show,name='show'),
    path('create/',views.create, name='create'),
    path('update/<int:pk>/',views.update, name='update'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('room/create/',views.create_room,name='create'),
    path('room/showall/',views.showAll_room,name='showall'),
    path('room/update/<int:pk>/',views.update_room,name='update'),
    path('room/delete/<int:pk>/',views.delete_room,name='delete'),
    path('time/create/',views.add_time,name='create'),
    path('time/update/<int:id>',views.update_time,name='update'),
    path('time/showall/',views.show_time,name='showall'),
    path('time/showall/<int:pk>',views.show_time,name='showall'),
    path('time/delete/<int:pk>/',views.delete_time,name='delete'),
    path('all/',views.teams,name='view'),
    # path('showdatas/',views.show_datas,name='datas'),
    # path('datas/<int:pk>/',views.all_data,name='datas'),

]
