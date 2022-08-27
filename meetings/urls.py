from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.new_room, name='new-room'),
    path('room/<slug:slug>/', views.room, name='room'),
    path('get_token/', views.get_token, name='get-token'),
    path('create_meeting_member/', views.create_meeting_member, name='create-meeting-member'),
    path('delete_meeting_member/', views.delete_meeting_member, name='delete-meeting-member'),
    path('get_meeting_member/', views.get_meeting_member, name='get-meeting-member'),
]
