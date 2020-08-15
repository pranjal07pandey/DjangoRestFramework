from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#create a router and register our viewset with it
router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)


# the api URLs are now determined automatically by the router
urlpatterns = router.urls

# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_details),

# ]

