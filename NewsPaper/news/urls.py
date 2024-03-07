from django.urls import path
from .views import NewsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch


urlpatterns = [

   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='product_create'),
   path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearch.as_view(), name='post_search')
]