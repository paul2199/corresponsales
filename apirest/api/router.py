from rest_framework.routers import DefaultRouter
from apirest.api.view import PostApiViewSet

router_posts = DefaultRouter()

router_posts.register(prefix='get',basename='corresponsale', viewset=PostApiViewSet)