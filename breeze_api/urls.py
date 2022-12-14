from django.urls import path
from . import views

urlpatterns = [
    path('api/sequences', views.SequenceList.as_view(), name='sequence_list'),
    path('api/sequences/<int:pk>', views.SequenceDetail.as_view(), name='sequence_detail'),
    path('api/users', views.UserList.as_view(), name='User_list'),
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='User_detail'),
]
