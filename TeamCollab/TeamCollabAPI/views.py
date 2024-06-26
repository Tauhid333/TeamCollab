from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import *
from .models import User
from rest_framework import viewsets, permissions, status, generics
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
class LoginAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data= data)
            
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                user     = User.objects.get(username = username, password = password)
                if user is None:
                    print("Authentication failed for user:", username)
                    return Response({
                        'status' :400,
                        'message': 'Invalid Password',
                        'data':{}

                    })
                refresh = RefreshToken.for_user(user)

                return Response ({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            print(e)
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    
    


