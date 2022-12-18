from django.urls import path
from .views import Posts, PostDetail, PostCreateViews, PostUpdateViews, PostDeleteViews, CategoryListView, multiply, PostSearch, subscribe

urlpatterns = [
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('', Posts.as_view()),
    path('create/', PostCreateViews.as_view(), name='post_create'),
    path('create/<int:pk>', PostUpdateViews.as_view(), name='post_update'),
    path('delete/<int:pk>', PostDeleteViews.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='posts_search'),
    path('multiply/', multiply),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
]