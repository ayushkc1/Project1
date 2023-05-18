from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from snippet.views import SnippetViewSet, UserViewSet
from rest_framework import renderers

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
router = routers.DefaultRouter()
router.register(r'snippets', SnippetViewSet,basename="snippet")
router.register(r'users', UserViewSet,basename="user")

urlpatterns = [

    path('', include(router.urls)),
    # path('snippets/', snippet_list),
    # path('snippets/<int:pk>/',snippet_detail),
    # path('users/', UserViewSet.as_view({'get': 'list'})),
    #path('users/<int:pk>/', user_detail),
    path('api-auth/', include('rest_framework.urls')),




]
#urlpatterns = format_suffix_patterns(urlpatterns)
