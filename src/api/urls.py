from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'predication', views.PredicationViewSet, basename='prediction')

urlpatterns = [
    path('', include(router.urls)),
    path('user/<int:pk>/', views.UserPublicDetailedView.as_view(), name='user-view'),
    path('my/profile/', views.UserProfileDetailedView.as_view(), name='profile-info-view-update'),
    path('my/password/change/', views.UserPasswordChangeView.as_view(), name='user-password-chang-put'),

]
