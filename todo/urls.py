from django.urls import path
from .views import ListCreateTodoApiView, DeleteTodoApiView

urlpatterns = [
    path('api/', ListCreateTodoApiView.as_view(), name="todoAPI"),
    path('api/delete/<str:gid>', DeleteTodoApiView.as_view(), name="todoAPI"),
]
