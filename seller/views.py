from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from seller.models import Document, products
from seller.forms import DocumentForm, UserForm, UploadFileForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponse
    else:
        form = UploadFileForm()
    return render(request, 'seller/upload.html', {'form': form})

def home(request):
        return render(request,'seller/home.html', {'seller_folks':User.objects.all(),"u":request.user})

@login_required
def channel_edit(request):
        return render(request,'seller/channel_edit.html', {'u':request.user})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            #profile = profile_form.save(commit=False)
            #profile.user = user
            #MY COMMENT u = UserProfile(user=user, picture=profile_form['picture'],phone=profile_form['phone'],address=profile_form['address'],desc=profile_form['desc'],video=profile_form['video'],timings=profile_form['timings'] )
            # Now we save the UserProfile model instance.
            #profile.save()
            #s = request.POST
            #u = user
            #if len(s)==0:
                #return render(request, 'seller/my_products.html', {'thumbs':(1,2,3,4,5,6,7,8,9,10), "u":u})# "u_products":u.products},#
            #else:
                #error = ""
               # try:
                 #   b = UserProfile(user=u, picture=s['picture'],phone=s['phone'], address=s['address'],video=s['video'],desc=s['desc'], timings=s['timings'])
                  #  b.save()
                   # kek= True
                #except Exception:
                 #   error = str(Exception)
                  #  kek = False
                #if kek:
                 #   return render (request, "seller/channel.html", {"u":u})
                #else:
                 #   return HttpResponse

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,'seller/register.html', {'user_form': user_form, registered: 'registered'} )
        
def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return render(request,'seller/home.html',{"u":request.user,'user_folk':username, 'user_folk_id':user.id,'seller_folks':User.objects.all()} )
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your yardsale account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'seller/login.html', {"u":request.user})

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('seller/login.html')

def profile(request):
        #u = request.POST
        #error = ""
        #try:
         #   b = sellers(first_name=s['first_name'],last_name=s['last_name'],phone=s['phone'],email=s['email'],address=str(s['address']),desc=s['desc'],timings=s['timings'],video=s['video'])
          #  b.save()
          #  kek= True
        #except Exception:
         #   error = str(Exception)
          #  kek = False

       # if kek:
        #    return render (request, 'seller/profile.html', {'post':request.POST})
        #else:
         #   return render(request,'seller/profile.html',{'post':error})
        return render(request,'seller/profile.html',{"u":request.user})
def product(request):
        return render(request, 'seller/product.html',{"u":request.user})

def contact(request):
        return render(request, 'seller/contact.html',{"u":request.user})

def index(request):
        return render(request, 'seller/index.html')

@login_required
def restricted(request):
        return render(request, 'seller/contact.html',{"u":request.user})

def grid(request):
        return render(request, 'seller/grid.html')

def upload(request):
        return render(request, 'seller/upload.html')

@login_required
def channel(request):
        return render(request, 'seller/channel.html',{"u":request.user})

@login_required
def my_products(request):
        form = UploadFileForm(request.POST, request.FILES)
        u = request.user
        s = request.POST
        if len(s)==0:
            return render(request, 'seller/my_products.html', {"u":u, "u_products":u.products_set.all(), "form":form})# "u_products":u.products},#
        else:
            error = ""
            try:
                b = products(seller=u, product_name=s['product_name'],age=s['age'], sold="FALSE",reason=s['reason'],listed="2015-01-01",video=s['video'], desc=s['desc'])
                b.save()
                kek= True
            except Exception:
                error = str(Exception)
                kek = False
            if kek:
                return render (request, "seller/my_products.html", {"u":u, "u_products":u.products_set.all(), "q":request.FILES.getlist('picture')})
            else:
                return HttpResponse

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
