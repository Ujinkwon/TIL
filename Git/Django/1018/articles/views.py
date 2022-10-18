from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article, Comment


# Create your views here.
# error: .accepted_renderer not set on Response : 데코레이터

@api_view(['GET','POST'])
def article_cr(request):
    if request.method =='GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many = True) # error: 'QuerySet' object has no attribute 'title'.
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = ArticleSerializer(data = request.data) #키워드 인자로 전달해줘야함 error:.is_valid()` as no `data=` keyword argument was passed when instantiating the serializer instance.
        if serializer.is_valid(raise_exception = True): # 404 에러 잡아준다!
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def article_rud(request,article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method =='GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method =='PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method =='DELETE':
        article.delete()
        return Response( {'id': article_pk} , status=status.HTTP_204_NO_CONTENT) #삭제된 글정보 리턴

@api_view(['GET', 'DELETE', 'PUT'])
def comment_rud(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response({'id': comment_pk}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
def comment_c(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)