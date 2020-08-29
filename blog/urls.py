from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path('post/<pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<id>/edit/', views.post_edit, name='post_edit'),
    path('post/<id>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<id>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<id>/remove/', views.comment_remove, name='comment_remove'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<id>/publish/', views.post_publish, name="post_publish"),
    path("post/<id>/remove/", views.post_remove, name="post_remove"),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about_me, name='about_me'),
    path('projects/', views.projects, name="projects"),
]
