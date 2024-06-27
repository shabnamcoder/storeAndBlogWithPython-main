from django.urls import path, include
from blog import views


urlpatterns = [
    path('head-post/', views.HeadPostList.as_view()),
    path('top-posts/', views.TopPostList.as_view()),
    path('latest-posts/', views.LatestPostsList.as_view()),
    path('posts/search/', views.search),
    path('posts/<slug:category_slug>/<slug:post_slug>',views.PostDetail.as_view()),
    path('post/<slug:category_slug>/', views.BlogCategoryDetail.as_view()),
]
