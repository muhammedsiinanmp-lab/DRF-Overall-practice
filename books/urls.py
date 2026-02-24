from rest_framework.routers import DefaultRouter
from .views import UserList,BookList
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r"users",UserList)
router.register(r"books",BookList)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',obtain_auth_token),
    # path('api-auth/',include('rest_framework.urls'))
]