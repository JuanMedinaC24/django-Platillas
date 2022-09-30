from gc import get_objects
from django.shortcuts import get_object_or_404, render

from . models import Categoria, Producto
# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:9]
    list_categoria = Categoria.objects.all()
    context = {
        'product_list':product_list,
        'categorias':list_categoria
    }
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto,pk=producto_id)
    return render(request,'producto.html',{'producto':producto})


