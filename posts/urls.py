from django.urls import path

from .views import (
	PostListView,
	PostUpdateView,
	PostDetailView,
	PostDeleteView,
	PostCreateView)


urlpatterns = [
	path('<int:pk>/edit/', PostUpdateView.as_view(), name = 'post-edit'),
	path('<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
	path('<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
	path('', PostListView.as_view(), name = 'post-list'),
	path('new/', PostCreateView.as_view(), name = 'post-new'),
]