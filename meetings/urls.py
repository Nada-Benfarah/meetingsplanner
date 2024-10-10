from django.urls import path
from .views import add_meeting, detail, meetings_list_view, room_detail, room_list_view

urlpatterns = [
    path('all', meetings_list_view, name='all'),
    path('<int:id>', detail, name='detail'),
    path('add', add_meeting, name='add'),
     path('list', room_list_view, name='room_list_view'),
      path('detailRoom/<int:id>', room_detail, name='room_detail'),
]