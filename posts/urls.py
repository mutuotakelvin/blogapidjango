from django.urls import path
from .views import PostList, PostDetail

# All the blog route will be api/v1/
urlpatterns = [
    path('<int:pk>/',PostDetail.as_view()),
    path('',PostList.as_view())
]