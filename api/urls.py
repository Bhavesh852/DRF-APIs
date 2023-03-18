from django.urls import path
from media.views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('authenticate/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('getuser/', getuser),
    path('follow/',followAPI.as_view()),
    path('unfollow/',unfollowAPI.as_view()),
    path('user/',user_detail.as_view()),
    path('posts/', create_post.as_view()),
    path('like/', like_post.as_view()),
    path('unlike/', unlike_post.as_view()),
    path('comment/', comment_post.as_view()),
    path('all_posts/', all_posts.as_view()),
]
