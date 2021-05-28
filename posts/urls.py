
from django.conf.urls import url, include
from posts import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('emp', views.EmployeeViewSet)

urlpatterns = [
    url('employees/', include(router.urls)),
    url(r'^$', views.PostsList.as_view(), name='posts_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.posts_retrieve, name='posts_retrieve'),
    url(r'^create_post', views.create_post, name='create_post'),
    url(r'^create', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/update_post', views.update_post, name='update_post'),
    url(r'^(?P<pk>[0-9]+)/update', views.update, name='update'),
    url(r'^(?P<pk>[0-9]+)/delete', views.delete, name='delete')
]