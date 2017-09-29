from django.conf.urls import url
from rest_framework import routers
from . import views

Userform_list = views.UserformViewSet.as_view({
    'get' : 'list',
    'post' : 'create'
})

Userform_detail = views.UserformViewSet.as_view({
    'get' : 'retrieve',
    'put' : 'update',
    'patch' : 'partial_update',
    'delete' : 'destroy'
}) 

router = routers.SimpleRouter()
router.register('form', views.UserformViewSet)

urlpatterns = router.urls
