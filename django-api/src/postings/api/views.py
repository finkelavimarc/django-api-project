# generic

from django.db.models import Q
from rest_framework import generics, mixins

from postings.models import BlogPost
from .serializers import BlogPostSerializer

from rest_framework.filters import SearchFilter, OrderingFilter

from django.db.models import  F

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    serializer_class        = BlogPostSerializer
    filter_backends         = [SearchFilter,OrderingFilter]
    search_fields           = ['date','clicks','os','country']
    ordering_fields         = '__all__'

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        query2 = self.request.GET.get("b")


        if query is not None:
            qs = qs.filter(
                    Q(date__lt=query)
                    ).distinct()
        elif query2 is not None:
            qs = qs.annotate(cpi=F('spend') / F('installs')).order_by('-cpi')

        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



