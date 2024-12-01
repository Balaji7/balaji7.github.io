from django.shortcuts import render, redirect
from .models import *


# Create your views here.

def home(request):
    if 'userid' in request.session:
        mailid=request.session['userid']
        return render(request,'index.html', {'email':mailid})
    else:
        return render(request,'index.html')

def login(request):
    if request.method == 'POST':

            
            password = request.POST['password']
            email = request.POST['email'] 

            if logindata.objects.filter(Email=email, Password=password):
                    request.session['userid']=email
                    loginpg = logindata.objects.get(Email=email, Password=password)


                    return render(request, 'index.html', {'log':loginpg,'email':email})
            else:
                     return render(request, 'login.html', {'error':'Please check the Email and Password'})
                 
            
            
            
    return render(request, 'login.html')




def table(request):
    if 'userid' in request.session:
        mailid=request.session['userid']
        data = contactdata.objects.filter(Email = mailid)
        return render(request,'table.html', {'doctor':data})
    else:
         return redirect('login_page')
         

def form(request):
    if 'userid' in request.session:
        mailid=request.session['userid']
        print(mailid,'This is mail id')
        return render(request,'index.html',{'email':mailid})
    else:
         return redirect('login_page')



def tab1(request):
    
    return render(request,'tab1.html')


def pt_data(request):
    if 'userid' in request.session:
        print("1")
    if request.method == "POST":
        print('2')
        ptname = request.POST['ptname']
        print('3')
        department = request.POST['department']
        print('4')
        medicine = request.POST['medicine']
        print('5')
        city = request.POST['city']
        print('')
        mailid=request.session['userid']

        ptdata = contactdata()
        ptdata.ptname = ptname
        ptdata.department = department
        ptdata.medicine = medicine
        ptdata.city = city
        ptdata.Email = mailid
        ptdata.save()
        data = contactdata.objects.filter(Email = mailid)

        return render(request,'table.html', {'doctor':data})
    return render(request,'form.html')

def updatepage(request,id):
    if 'userid' in request.session:
        updatedata=contactdata.objects.get(id=id)
    return render(request,'updatepage.html',{'data':updatedata})

def pt_update(request):
    if 'userid' in request.session:
        print('1')
    if request.method == "POST":
        print('2')
        ptname = request.POST['ptname']
        print('3')
        department = request.POST['department']
        print('4')
        medicine = request.POST['medicine']
        print('5')
        city = request.POST['city']
        print('6')
        ptid = request.POST['ptid']
        print('7')
        

        updatedata = contactdata.objects.get(id=ptid)
        updatedata.ptname = ptname
        updatedata.department = department
        updatedata.medicine = medicine
        updatedata.city = city
        updatedata.save()

        return redirect('home')
    
def delete(request,id):
    tabledelete = contactdata.objects.get(id=id)
    tabledelete.delete()

    return redirect('home')

def search_results(request):
    if 'userid' in request.session:
      if request.method == "POST":
        search_results = request.POST['search']
        searchdata = contactdata.objects.filter(city=search_results)
        return render(request,'tab1.html', {'doctor':searchdata})
    return render(request,'table.html')


def signup(request):
    if request.method == 'POST':
        
            name = request.POST['name']
            education = request.POST['education']
            phone_no = request.POST['phone_no']
            email = request.POST['email']
            city = request.POST['city']
            passwords = request.POST['password']
            
            
            logindata.objects.create(
                Name=name,  
                Email=email,
                Password=passwords,  
                Education=education,
                Phone_no=phone_no,
                City=city,
            )
            
    
            return redirect('signup') 

    return render(request, 'signup.html')





def signup_page(request):
    return render(request,'signup.html')

def login_page(request):
    return render(request,'login.html')

def logout(request):
    if 'userid' in request.session:
        email = request.session['userid']
        del request.session['userid']  
        
        return redirect('login')
    else:
         return redirect('login')
    





    






