from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'url', 
            'pk',   
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount',
        ]
        
    def get_url(self,obj):
        request = self.context.grt("request")
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)
        
    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None 
        if not isinstance(obj,Product):
            return None
        return obj.get_discount()
