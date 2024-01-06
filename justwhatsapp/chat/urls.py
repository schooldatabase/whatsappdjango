from django.urls import path
from chat import views
from django.urls import re_path
urlpatterns = [
path('', views.index, name='index'),
path("<str:room_name>/", views.room, name="room"),
# re_path(r"ws/chat/<str:room_name>/",views.room, name="room"),
# re_path(r"ws/chat/(?P<room_name>\w+)/$",views.room, name="room"),
# re_path('ws/jwc/<str:groupkaname>/',views.room, name="room"),
# re_path('ws/ajwc/<str:groupkaname>/', views.room, name="room"),
]