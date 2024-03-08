from django.urls import path
from .views import NewsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch


urlpatterns = [

   path('posts/', NewsList.as_view(), name='news_list'),
   path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/search/', PostSearch.as_view(), name='post_search'),
   path('news/create/', PostCreate.as_view(), name='post_create'),
   path('article/create/', PostCreate.as_view(), name='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('article/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('article/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]