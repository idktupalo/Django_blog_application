from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/<uuid:id>/', views.post_detail, name='post_detail'),
    path('<uuid:post_id>/share/', views.post_share, name='post_share'),
    path('<uuid:post_id>/comment/', views.post_comment, name='post_comment'),
]