from django.shortcuts import render,redirect

# Create your views here.
from django.contrib import messages
from .forms import usersignup,userlogin,restaurant_signup_form,restaurant_login_form,DishForm
from django.http import HttpResponse
from .models import user,restaurant,city,dish
from django.contrib.auth import authenticate, login
from django.urls import reverse
from math import ceil

def index(request):
    if 'username' in request.session:
        url = reverse('home')
        return redirect(url)
    elif 'restaurantname' in request.session:
        url = reverse('restaurant_home')
        return redirect(url)
    return render(request,'index.html')
def login(request):
    if 'username' in request.session:
        url = reverse('home')
        return redirect(url)

    if request.method == 'POST':
        form = userlogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            # return HttpResponse("Got it")
            check = user.objects.filter(username=username, password=password).exists()
            print(check)
            if check:
                request.session['username'] = username
                my_variable = request.session['username']
                print(my_variable)
                url = reverse('home')
                return redirect(url)
            else:
                params={'form':form,'msg':'wrong',}
                return render(request,'login.html',params)
    else:
        form=userlogin()
    return render(request,'login.html',{'form': form})



    # if request.method=='POST':
    #     username=request.POST.get('username')
    #     password=request.POST.get('password')
    #     check = user.objects.filter(username=username, password=password).exists()
    #     print(check)
    #     if check:
    #         request.session['username'] = username
    #         my_variable = request.session['username']
    #         print(my_variable)
    #         url = reverse('home')
    #         return redirect(url)
    #     else:
    #         params={'msg':'wrong',}
    #         return render(request,'login.html',params)
    # return render(request,'login.html')



def signup(request):
    if 'username' in request.session:
        url = reverse('home')
        return redirect(url)
    elif 'restaurantname' in request.session:
        url = reverse('restaurant_home')
        return redirect(url)
    if request.method == 'POST':
        form = usersignup(request.POST)
        if form.is_valid():
            # Access the validated form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            myuser = user(username=username,email = email,phone = phone,address = address,city = city,zip_code = zip_code,password = password1)
            myuser.save()
            url = reverse('login')
            return redirect(url)

            
    else:
        form=usersignup()
    return render(request,'signup.html',{'form': form})


def home(request):
    if 'username' in request.session: 
        params={'username':request.session['username'].capitalize()}
        cities=city.objects.all()
        tempparams={}
        for i in cities:
            restaurants=restaurant.objects.filter(city=i)
            print(i.city_name)
            n = len(restaurants)
            if restaurants:
                print(n)
                nSlides = n//3 + ceil((n/3)-(n//3))
                tempparams[i.city_name]={'no_of_slides':nSlides, 'range': range(1,nSlides),'product': restaurants}
        # print(params['restaurants'])
        print(tempparams['Banglore'])
        params['city']=tempparams
        return render(request,'home.html',params)
    elif 'restaurantname' in request.session:
        url = reverse('restaurant_home')
        return redirect(url)

    else:
        url = reverse('index')
        return redirect(url)

def logout(request):
    if 'username' in request.session:
        del request.session['username']
    url = reverse('index')
    return redirect(url)



def restaurant_detail(request):
    restaurant_name = request.GET.get('restaurant_name')
    restaurant_details=restaurant.objects.filter(name=restaurant_name)

    for i in restaurant_details:
        dishs=dish.objects.filter(restaurant_id=i)
        print(i.name)
        print(i.description)
    context = {
        'username': request.session['username'].capitalize(),
        'restaurant': restaurant_details,
        'dish':dishs
    }
    return render(request, 'restaurant_details.html', context)


def restaurant_login(request):
    if 'username' in request.session:
        url = reverse('home')
        return redirect(url)
    elif 'restaurantname' in request.session:
        url = reverse('restaurant_home')
        return redirect(url)

    if request.method == 'POST':
        form = restaurant_login_form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['restaurantname']
            password = form.cleaned_data['password']
            print(username)
            print(password)
            # return HttpResponse("Got it")
            check = restaurant.objects.filter(name=username, password=password).exists()
            print(check)
            if check:
                request.session['restaurantname'] = username
                my_variable = request.session['restaurantname']
                print(my_variable)
                url = reverse('restaurant_home')
                return redirect(url)
            else:
                params={'form':form,'msg':'wrong',}
                return render(request,'restaurant_login.html',params)
    else:
        form=restaurant_login_form()
    return render(request,'restaurant_login.html',{'form': form})
    
    
def restaurant_signup(request):
    if 'username' in request.session:
        url = reverse('home')
        return redirect(url)
    elif 'restaurantname' in request.session:
        url = reverse('restaurant_home')
        return redirect(url)
    if request.method == 'POST':
        form = restaurant_signup_form(request.POST or None, request.FILES or None)
        if form.is_valid():
            # Access the validated form data
            restaurant_name = form.cleaned_data['restaurant_name']
            description = form.cleaned_data['description']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            zip_code = form.cleaned_data['zip']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            image = form.cleaned_data['image']
            if(image):
                print('image')
            else:
                print('no')
            

            myuser = restaurant(name=restaurant_name,description=description,email = email,phone = phone,address = address,city = city,zip_code = zip_code,image=image,password = password1)
            myuser.save()
            url = reverse('restaurant_login')
            return redirect(url)

            
    else:
        form=restaurant_signup_form()
    return render(request,'restaurant_signup.html',{'form': form})



def restaurant_home(request):
    if 'restaurantname' in request.session: 
        params={'restaurantname':request.session['restaurantname'].capitalize()}
        restaurants=restaurant.objects.filter(name=request.session['restaurantname'])
        # dishs=dish.objects.filter()
        print(restaurants)
        for i in restaurants:
            dishs=dish.objects.filter(restaurant_id=i)
            print(i.name)
            print(i.description)
            print(dishs)
        context = {
        'restaurant': restaurants,
        'dish':dishs
        }

    return render(request,'restaurnat_home.html',context)


def restaurant_logout(request):
    if 'restaurantname' in request.session:
        del request.session['restaurantname']
    url = reverse('index')
    return redirect(url)


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            new_dish = form.save(commit=False)  # Create an instance but don't save it to the database yet
            # Set the restaurant_id manually to the desired ID (e.g., '52')
            restaurants=restaurant.objects.filter(name=request.session['restaurantname'])
            for i in restaurants:
                new_dish.restaurant_id = i
            new_dish.save()  # Now save the instance with the modified restaurant_id
            url = reverse('restaurant_home')
            return redirect(url)

            # form.save()
            # return redirect('dish_list')  # Redirect to a success page or dish list page
    else:
        form = DishForm()
    return render(request, 'add_dish.html', {'form': form})
def checkout(request):
    # return HttpResponse('Checkout')
    context = {
        'username': request.session['username'].capitalize(),
    }
    return render(request,'checkout.html',context)