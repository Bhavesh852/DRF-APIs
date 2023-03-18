from rest_framework.decorators import api_view
from rest_framework.response import Response
from media.serializers import *
from media.models import Person, Following
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView


@api_view(['GET'])
def getuser(request):
    objs = User.objects.all()
    serializer = UserSerializer(objs, many=True)
    return Response(serializer.data)


class followAPI(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        data = request.data
        following_user = User.objects.get(id = data['id'])
        print(following_user)
        payload = {
            'user' : request.user.id,
            'following_user' : following_user.id
        }
        serializer = FollowingSerializer(data = payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class unfollowAPI(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        data = request.data
        unfollowing_user = Following.objects.get(following_user = data['id'], user = request.user.id)
        unfollowing_user.delete()
        return Response({'msg' : 'Unfollow succesfully'})


class user_detail(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        total_followers =  len(list(Following.objects.filter(user = request.user.id)))
        total_followings = len(list(Following.objects.filter(following_user = request.user.id)))
        return Response({'username' : request.user.username, 'followers' : total_followers, 'followings' : total_followings})


class create_post(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        data = request.data
        serializer = PostsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request):
        data = request.data
        obj = Posts.objects.get(id = data['id'])
        obj.delete()
        return Response({'msg' : 'Post deleted successfully'})

    def get(self, request):
        data = request.data
        obj = Posts.objects.get(id=data['id'])
        serializer = PostsSerializer(obj)
        return Response(serializer.data)


class all_posts(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        objs = Posts.objects.all()
        data = []
        for p in objs:
            _dict = {}
            likes = len(Like.objects.filter(post=p.id))
            comment_data = comment.objects.filter(post=p.id)
            comment_serial = commentSerializer(comment_data, many=True)
            all_comments = comment_serial.data
            _dict['id'] = p.id
            _dict['title'] = p.title
            _dict['desc'] = p.description
            _dict['created_at'] = p.created_at
            _dict['comments'] = all_comments
            _dict['likes'] = likes
            data.append(_dict)
        return Response(data)


class like_post(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        payload = request.data
        data = {
            'post' : payload['id'],
            'user' : request.user.id
        }
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class unlike_post(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        data = request.data
        unlikePost = Like.objects.get(post = data['id'], user = request.user.id)
        unlikePost.delete()
        return Response({'msg' : 'Unlike succesfully'})


class comment_post(APIView):
    authentication_classes = [ JWTAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def post(self, request):
        data = request.data
        payload = {
            'post' : data['id'],
            'user' : request.user.id,
            'comment' : data['comment']
        }
        serializer = commentSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors) 

