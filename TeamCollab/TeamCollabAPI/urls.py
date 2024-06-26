from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls), name='API'),
    path('users/register/', UserViewSet.as_view({'post': 'register'}), name='user-register'),
    path('user/login/', LoginAPI.as_view(), name='user-login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]