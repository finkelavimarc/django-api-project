from django.conf.urls import url


from .views import BlogPostAPIView

urlpatterns = [
    url(r'^$', BlogPostAPIView.as_view(), name='post-listcreate'),
]