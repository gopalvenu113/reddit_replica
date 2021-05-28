from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from posts.models import Post, Employee
from django.views import generic
from rest_framework import serializers, viewsets, filters
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from posts.serializers import EmployeeSerializer, EmployeeCreateSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from posts.filters import EmployeeFilterSet
# Create your views here.




#django views


# def posts_list(request):
#     posts_list = Post.objects.values('name', 'created', 'created_by', 'id')
#     return render(request, 'lists_of_posts.html', context={'posts':posts_list})

class PostsList(generic.ListView):
    template_name = 'lists_of_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.values('name', 'created', 'created_by', 'id')

def posts_retrieve(request, pk):
    posts_list = Post.objects.filter(id=pk).values('name', 'created', 'created_by', 'id', 'data', 'votes')
    return render(request, 'retrieve_post.html', context={'posts':posts_list})

def create(request):
    if request.method == 'POST':
        data = request.POST
        post = Post.objects.create(name=data['name'], data=data['data'], created_by=data['created_by'])
        return redirect(reverse('posts:posts_retrieve', args=(post.id,)))
    else:
        raise Exception('Can not create a post for this method')

def create_post(request):
    return render(request, 'create_post.html')

def update(request, pk):
    if request.method == 'POST':
        data = request.POST
        Post.objects.filter(id=pk).update(data=data['data'], votes=data['votes'])
        return redirect(reverse('posts:posts_retrieve', args=(pk,)))
    else:
        raise Exception('Can not update a post for this method')

def update_post(request, pk):
    post = Post.objects.filter(id=pk).last()
    return render(request, 'update_post.html', context={'post':post})

def delete(request, pk):
    Post.objects.filter(id=pk).delete()
    return redirect(reverse('posts:posts_list'))


#django rest framework views

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    pagination_class = PageNumberPagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EmployeeFilterSet
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer_mapping = {
            'create': EmployeeCreateSerializer,
        }
        return serializer_mapping.get(self.action, EmployeeSerializer)

    def list(self, request):
        queryset = self.queryset
        queryset = self.filter_queryset(queryset)
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)
    
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.get_object()
        serializer = self.get_serializer(instance, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
