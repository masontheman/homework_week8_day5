from django.urls import include, path
from rest_framework import routers
from snippets import views
from knox import views as knox_views
from rest_framework.authtoken import views as viewss

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'signup', views.SignupViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'posts',views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', viewss.obtain_auth_token),
    path('login/', knox_views.LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    
]
