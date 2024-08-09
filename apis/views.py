from rest_framework import viewsets, generics
from clothes.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ListAPIView by default allows read-only access to this end point collection
# To add CRUD operations you must use  RetrieveUpdateDestroyAPIView
class ProductViewSet(generics.ListAPIView):
    # Specifies the serializer used to convert the Product model instances
    # to JSON format. The ProductSerializer handles how the data is structured when returned to the client.
    serializer_class = ProductSerializer

    # This is a method that overrides the default queryset retrieval behavior of ListAPIView.
    def get_queryset(self):
        # This line retrieves the value of the category parameter from the URL.
        # kwargs is a dictionary containing keyword arguments passed to the view,
        # which in this case includes parameters captured from the URL.
        # If the URL pattern is something like product/shirt/, this line will extract
        # "shirt" as the category.
        category = self.kwargs.get('category')
        if category:
            # category__name__iexact=category: This filter is case-insensitive (iexact),
            # meaning it will match "Shirt", "shirt", "SHIRT", etc.
            return Product.objects.filter(category__name__iexact=category).order_by('id')
        return Product.objects.all().order_by('id')
