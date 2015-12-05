from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from seller.models import sellers
from seller.models import Document
from seller.forms import DocumentForm


# Create your views here.

def home(request):
        return render(request,'seller/home.html')
        
def profile(request):
        return render(request, 'seller/profile.html')

def product(request):
        return render(request, 'seller/product.html')

def contact(request):
        return render(request, 'seller/contact.html')

def grid(request):
        return render(request, 'seller/grid.html')

def upload(request):
        return render(request, 'seller/upload.html')

def channel(request):
        return render(request, 'seller/channel.html')

def my_products(request):
        return render(request, 'seller/my_products.html', {'thumbs':(1,2,3,4,5,6,7,8,9,10)})

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect('list')
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'seller/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
