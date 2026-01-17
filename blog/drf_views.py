from rest_framework.response import Response


from blog.models import Article
from blog.serializers import ArticleSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
# function View 會造成邏輯跟方法混再一起
# @api_view(["GET", "POST"])
# def article_list(request):
#     """文章列表 API"""
#     if request.method == "GET":
#         return Response({"message": "文章列表"})
#     elif request.method == "POST":
#         return Response({"message": "新增文章"}, status=201)


# @api_view(["GET", "PUT", "DELETE"])
# def article_detail(request, pk):
#     """文章詳情 API"""
#     if request.method == "GET":
#         return Response({"message": f"取得文章 {pk}"})
#     elif request.method == "PUT":
#         return Response({"message": f"更新文章 {pk}"})
#     elif request.method == "DELETE":
#         return Response({"message": f"刪除文章 {pk}"}, status=204)


# class View 可以明確的分隔
class ArticleListAPIView(GenericAPIView):
    """文章列表 API"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        articles = self.get_queryset()
        serializer = self.get_serializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # # 手動建立 Article 物件
            # article = Article.objects.create(
            #     title=serializer.validated_data["title"],
            #     content=serializer.validated_data["content"],
            #     is_published=serializer.validated_data.get("is_published", False),
            #     created_by=request.user,
            # )
            # output_serializer = ArticleSerializer(article)

            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(GenericAPIView):
    """文章詳情 API"""

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request, pk):
        article = self.get_object()
        serializer = self.get_serializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object()
        serializer = self.get_serializer(article, data=request.data)
        if serializer.is_valid():
            # 手動更新 Article 物件
            # article.title = serializer.validated_data["title"]
            # article.content = serializer.validated_data["content"]
            # article.is_published = serializer.validated_data.get(
            #     "is_published", article.is_published
            # )
            # article.save()
            # output_serializer = ArticleSerializer(article)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object()
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
