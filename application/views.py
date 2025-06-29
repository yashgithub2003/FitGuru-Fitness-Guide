from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from application.models import enquiry_table,customplan,register_users,verified_users
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
import json


def home(request):
    
    return render(request, 'index.html')





def reg_user(request):
    context = {}
    
    if request.method == 'POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('number')
        d = request.POST.get('password')
        e = request.POST.get('gender')
        f = request.POST.get('dob')

        if register_users.objects.filter(phone=c).exists():
            context['message'] = "⚠️ Phone number already registered."
            context['status'] = 'error'
            return render(request, 'user_logins.html', context)

        # 🔒 Hash the password before saving
        hashed_password = make_password(d)

        # Save to DB
        info = register_users(name=a, email=b, phone=c, password=hashed_password, gender=e, dob=f)
        info.save()

        context['message'] = "✅ Registration successful! Wait for Confirmation..."
        context['status'] = 'success'

    return render(request, 'user_logins.html', context)


def contact(request):
    if not request.session.get('islogin'):
        return redirect('user_login_page')
    if request.method=='POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')

        info = enquiry_table(name = a, email = b, phone = c, message = d)
        info.save()


        messages.success(request, 'Data Submitted ')
    return render(request, 'contact.html')

def about(request):
    if not request.session.get('islogin'):
        return redirect('user_login_page')

    return render(request, 'about.html')

def services(request):
    if not request.session.get('islogin'):
        return redirect('user_login_page')

    return render(request, 'services.html')

def worklib(request):
    if not request.session.get('islogin'):
        return redirect('user_login_page')

    return render(request, 'worklib.html')

def getyourplan(request):
    if not request.session.get('islogin'):
        return redirect('user_login_page')

    return render(request, 'yourplan.html')

def dashboard(request):
    info = enquiry_table.objects.all()
    countfeedback= enquiry_table.objects.count()
    totaluser= verified_users.objects.count()
    totalcustplan= customplan.objects.count()
    last_five_enquiries = enquiry_table.objects.order_by('-id')[:5]
    context = {
        'information': info,
        'countfeedback': countfeedback,
        'totaluser': totaluser,
        'totalcustplan': totalcustplan,
        'last_five_enquiries': last_five_enquiries
    }
    return render(request, 'admin_dashboard/html/dashboard.html',context )

def feedbacks(request):
    info = enquiry_table.objects.all()
    # contact is table name which we create in models.py
    data = {'information':info}
    return render(request, 'admin_dashboard/html/feedbacks.html',data)

def user_logins(request):

    return render(request, 'user_logins.html')

def login_user(request):

    if request.method == "POST":
        a = request.POST.get('username', '').strip()
        b = request.POST.get('password', '').strip()

        user = authenticate(request, username = a, password = b)

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            messages.error(request, 'In-correct username or password!..')

    return render(request, 'login.html')
def user_login_page(request):

    return render(request, 'user_login.html')



from django.contrib.auth.hashers import check_password


def user_login(request):
    if request.method == "POST":
        a = request.POST.get('username', '').strip()
        b = request.POST.get('password', '').strip()

        try:
            user = verified_users.objects.get(phone=a)
        except verified_users.DoesNotExist:
            user = None

        if user and check_password(b, user.password):
            request.session['islogin'] = True
            request.session['user_number'] = user.phone
            return render(request, 'index.html')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid credentials'})

    return render(request, 'user_login.html')



@csrf_protect
def logout_user(request):
    if request.method == 'POST':
        print("Logging out...")
        request.session.flush()
        return redirect('home')
    return redirect('home')

def logout(request):

    return render(request, 'index.html')

def add_user(request):

    infoadmin = verified_users.objects.all()

    alldata = {'allinformation':infoadmin}
    return render(request, 'admin_dashboard/html/adduser.html',alldata)

    
def alluser(request):
    infoadmin = register_users.objects.all()

    alldata = {'allinformation':infoadmin}
    return render(request, 'admin_dashboard/html/alluser.html',alldata)


from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect


def reject_reg(request, id):
    if request.method == 'POST':
        data = get_object_or_404(register_users, pk=id)
        data.delete()
        
    return HttpResponseRedirect('/after_alluser/')

def after_alluser(request):

    return render(request, 'admin_dashboard/html/alluser.html')

def approve_reg(request, id):
    info = register_users.objects.filter(pk=id)
    data = {'information':info}
    return render(request, 'admin_dashboard/html/approve_reg.html', data)

def verified_reg(request, id):
    info = get_object_or_404(register_users, pk=id)

    info.name = request.POST.get('name')
    info.email = request.POST.get('email')
    info.phone = request.POST.get('phone')
    info.password = request.POST.get('password')
    info.gender = request.POST.get('gender')
    info.dob = request.POST.get('dob')

    context = {}


    if verified_users.objects.filter(phone=info.phone).exists():
        context['message'] = "⚠️ Phone number already registered."
        context['status'] = 'error'
        return render(request, 'admin_dashboard/html/alluser.html', context)


    final_users = verified_users(
        name=info.name,
        email=info.email,
        phone=info.phone,
        password=info.password,
        gender=info.gender,
        dob=info.dob
    )
    final_users.save()
    info.delete()

    context['message'] = "✅ Registration successful!"
    context['status'] = 'success'
    return HttpResponseRedirect('/alluser/')


def displayplan(request):
    imgdata = sendimg.objects.all()
    alldata = {'allimgdata':imgdata}
    return render(request, 'admin_dashboard/html/displayplan.html',alldata)


def modifyuser(request):
    infoadmin = verified_users.objects.all()
    alldata = {'allinformation':infoadmin}
    return render(request, 'admin_dashboard/html/modifyuser.html',alldata)

def delete_record(request, id):
    if request.method=='POST':
        data = verified_users.objects.get(pk=id)
        data.delete()
    return HttpResponseRedirect('/modifyuser/')


def edit_record(request, id):
    info = verified_users.objects.filter(pk=id)
    data = {'information':info}
    return render(request, 'admin_dashboard/html/edituser.html', data)




def update_record(request, id):
    info = verified_users.objects.get(pk=id)
    
    info.name = request.POST.get('name')
    info.email = request.POST.get('email')
    info.phone = request.POST.get('phone')
    info.message = request.POST.get('message')
    info.save()
    

    return HttpResponseRedirect('/modifyuser/')


def precustomplan(request):
    infoadmin = verified_users.objects.all()
    alldata = {'allinformation':infoadmin}

    return render(request, 'admin_dashboard/html/precustplan.html',alldata)




def customizeplan(request,id):
    info = verified_users.objects.filter(pk=id)
    data = {'information':info}
    return render(request, 'admin_dashboard/html/customizepla.html',data)





def customplans(request):
    if request.method == 'POST':
        contact_no = request.POST.get('contact_no')


        chest = request.POST.getlist('chest[]')
        triceps = request.POST.getlist('triceps[]')
        shoulder = request.POST.getlist('shoulder[]')
        back = request.POST.getlist('back[]')
        biceps = request.POST.getlist('biceps[]')
        legs = request.POST.getlist('legs[]')


        customplan.objects.filter(contact_no=contact_no).delete()


        plan = customplan(
            contact_no=contact_no,
            chest=",".join(chest),
            triceps=",".join(triceps),
            shoulder=",".join(shoulder),
            back=",".join(back),
            biceps=",".join(biceps),
            legs=",".join(legs)
        )
        plan.save()

        messages.success(request, 'Custom plan updated successfully!')
        return redirect('/precustomplan/')

    return redirect('/')



def getyourplan(request):
    context = {}
    alldata = None


    if request.session.get('islogin') and request.session.get('user_number'):
        phone = request.session['user_number']
        alldata = customplan.objects.filter(contact_no=phone)
        context['alldata'] = alldata


        body_parts = ['chest', 'triceps', 'shoulder', 'back', 'biceps', 'legs']

        for item in alldata:
            for part in body_parts:
                value = getattr(item, part, None)
                if isinstance(value, str):
                    part_list = value.split(',')
                elif isinstance(value, list):
                    part_list = value
                else:
                    part_list = []

                setattr(item, f'{part}_list', part_list)

    else:
        
       return redirect('user_login_page')

    return render(request, 'yourplan.html', context)







def searchplan(request):
    contact_no = request.POST.get('contactno', '')
    found = False
    fitness_record = None
    message = ''
    
    if request.method == 'POST' and contact_no:
        try:
            fitness_record = customplan.objects.get(contactno=contact_no)
            found = True
        except customplan.DoesNotExist:
            message = f"No data found for contact number: {contact_no}"
    
    return render(request, 'fitness_data.html', {
        'contact_no': contact_no,
        'fitness_record': fitness_record,
        'found': found,
        'message': message
    })