from django.conf.urls import url
from rest_framework import routers
from . import views

account_list = views.AccountViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

account_detail = views.AccountViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
}) 

User_list = views.UserViewSet.as_view({
    'post' : 'create'
})
User_detail = views.UserViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
})

router = routers.SimpleRouter()
router.register('register', views.UserViewSet)
router.register('account', views.AccountViewSet)


urlpatterns = router.urls
#urlpatterns = [ url(r'^rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login') ]
