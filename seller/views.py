from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from seller.models import sellers, Document, products
from seller.forms import DocumentForm
from seller.forms import NameForm


# Create your views here.

def home(request):
        return render(request,'seller/home.html')
        
def profile(request):
        for seller_boy in request.POST:
            s = seller_boy
        print (s)
        error = ""
        for s in seller_boy:
            try:
                s = sellers(first_name=str(s['first_name']),phone=str(s['phone']),email=str(s['email']),address=str(s['address']),about=str(s['about']),timings=str(s['timings']))
                s.save()
                kek = True
            except Exception:
                #error = str(Exception)
                kek = False
                break

        if kek:
            return render (request, 'seller/channel.html', {'post':"Your information has been updated"})
        else:
            return render(request,'seller/channel.html',{'post':'Sorry something went wrong.'})

def product(request):
        return render(request, 'seller/product.html')

def index(request):
        return render(request, 'seller/index.html')

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

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})

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
