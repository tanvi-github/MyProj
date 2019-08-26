from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpResponseNotFound
from .models import tb_Registration,web1,basic
from .form import RegistrationForm,LoginForm#,Basic

# Create your views here.
def hello(request):
    return HttpResponse("<h1> hello welcome to django framework </h1>")

def template_thanks(request):
 return render(request,"MyApp/thanks.html")

def template_Home(request):
    all_web=web1.objects.all()
    return render(request,"MyApp/home.html",{"web_head":all_web})

def Register(request):
    if request.method=='POST':
       data=request.POST
       # form = UserCreationForm(request.POST)
       form = RegistrationForm(data)
       if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            address = form.cleaned_data['address']
            password = form.cleaned_data['password']
            gender=form.cleaned_data['gender']

            p=tb_Registration(name=name,email=email,contact=contact,address=address,gender=gender,password=password)
            p.save()
            print('this is the valid data from the form',gender)
            #return HttpResponseRedirect('MyApp/thanks.html')
            return HttpResponseRedirect('MyApp/thanks.html')
       else:
           print("22222")
           return render(request,"MyApp/reg.html",{'form':form})
    else:
          print("56876857")
          return render(request,"MyApp/reg.html")

def Login(request):
    if request.method=='POST':
        data=request.POST #getting data from the form
        form=LoginForm(data)

        if form.is_valid():
            u_email=form.cleaned_data['email']
            u_password=form.cleaned_data['password']
            p=tb_Registration.objects.filter(email=u_email,password=u_password)
            if (p.count()>0):
                request.session['username']=u_email
                print("valid user",p)
                return HttpResponseRedirect("/thanks")
            else:
                print("try again user",p)
                return HttpResponseNotFound('<h1> no page here</h1>')
        else:
            print("\n\n this is else block:{0}\n\n")
            return render(request,"MyApp/thanks.html",{'form':form})
    else:
        form=LoginForm()
        print('\n\n this is else block....:{0}\n\n')
        return render(request,"MyApp/Login.html",{'form':form})



#try code
"""def Base(request):
    if request.method=='POST':
       data=request.POST
       # form = UserCreationForm(request.POST)
       form = Basic(data)
       if form.is_valid():
            name = form.cleaned_data['name']
            age=form.cleaned_data['age']
            gender=form.cleaned_data['gender']
            p=basic(name=name,age=age, gender=gender)
            p.save()
            return HttpResponseRedirect('MyApp/thanks.html')
            else:
        return render(request,"MyApp/reg.html",{'form':form})"""



