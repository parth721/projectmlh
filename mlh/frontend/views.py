from django.shortcuts import render, redirect
from backend.form import *
from .models import *
from django.http import HttpResponse, JsonResponse



def create_user_info(request):
    if request.method == 'POST':
        # Create and save UserInfo instance
        user = request.user  # Assuming you are using Django's default User model
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        user_info_instance = UserInfo(user=user, Name=name, Phone=phone, Country=country)
        user_info_instance.save()

        # Redirect to create_user_bio with user_id as a parameter
        return redirect('create_user_bio', user_id=user_info_instance.id)

    return render(request, 'user_info_form')

def create_user_bio(request, user_id):
    if request.method == 'POST':
        form_user_bio = UserBioForm(request.POST)
        if form_user_bio.is_valid():
            # Retrieve the UserInfo instance based on user_id
            user_info_instance = UserInfo.objects.get(id=user_id)

            # Create and link the UserBio instance
            user_bio_instance = form_user_bio.save(commit=False)
            user_bio_instance.user = user_info_instance
            user_bio_instance.save()

            return redirect('success_page')

    else:
        form_user_bio = UserBioForm()

    return render(request, 'user_bio_form.html', {'form_user_bio': form_user_bio})

def success_page(request):
    return render(request, 'success_page')



# Create your views here.
def home(request) :
    return render(request, "html/home.html")

def success(request):
    return render(request, "html/success.html")
'''
def user_form(request):
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            form_user.save()
            return redirect("user_bio")
    else:
        form_user = UserForm()
    return render(request, 'html/user.html', {'form_user':form_user})
'''
def partner_form(request):
    if request.method == 'POST':
        form_partner = PartnerForm(request.POST)
        if form_partner.is_valid():
            form_partner.save()
            return redirect('html/partner.html')
    else:
        form_partner= PartnerForm()
    return render(request, 'html/partner.html', {'form_partner':form_partner})
'''
def redirect_user(request, user_id):
    if request.method == 'POST':
        bio_user = UserRef(request.POST)
        if bio_user.is_valid():
            bio_user.save()
            return redirect('success_page')
    else:
        bio_user = UserRef()
        
    return  render(request, 'html/userbio.html', {'bio_user':bio_user})


def create_user_bio(request, id):
    if request.method == 'POST':
        form_user_bio = UserRef(request.POST)
        if form_user_bio.is_valid():
            user_info_instance = UserInfo.objects.get(user_id=id)
            user_bio_instance = form_user_bio.save(commit=False)  
            user_bio_instance.user_id = user_info_instance 
            user_bio_instance.save()  
            return redirect('success_page')

    else:
        form_user_bio = UserRef()

    return render(request, 'html/userbio.html', {'form_user_bio': form_user_bio, 'user_id': user_id})
'''
    
def redirect_partner(request):
    if request.method == 'POST':
        bio_partner = PartnerRef(request.POST)
        if bio_partner.is_valid():
            
            bio_partner.save()
            return redirect('html/partner.html')
    else:
        bio_partner = PartnerRef()
        
    return  render(request, 'html/partnerbio.html', {'bio_partner':bio_partner})


def login(request):
    return render(request, "html/login.html")

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        if Profile.objects.filter(phone_number = phone_number).exists():
            ...
        else:
            user = User.objects.create(username = username)
            profile = Profile.objects.create(user = user, phone_number = phone_number)
        
        return redirect('/')
    return render(request, 'register.html.')
'''
# the verification with another system.
def sendOTP(request):
    #if request.method == 'POST':
       # try:  
            phone_number = request.POST.get('phone_number')
            phone_number = str(phone_number)
            otp = str(random.randrange(1000, 9999))

            client = Client("AC157a3deced6810930de61fcd331c090d", "22a173d4fad92dedf5ba699ca09fea7e")
            response = client.messages.create(to="+91" + phone_number, from_="+15178360990", body=f'Your OTP is : {otp}')

            # Handle the error if the OTP could not be sent
            if response.status_code != 200:
                raise Exception(f'Failed to send OTP: {response.status_code}')

            request.session['verification_code'] = otp
            return JsonResponse({'success': True})
       # except Exception as e:
            import logging
            logging.error(str(e))
            return JsonResponse({'success': False, 'error_message': str(e)})
   # return JsonResponse({'success': False, 'error_message': 'Invalid request'})

def verify_user(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('code')
        saved_otp = request.session.get('verification_code')

        # Check if the OTP is valid.
        if entered_otp != saved_otp:
            return render(request, 'html/user.html', {'error_message': 'Invalid OTP.'})

        # The OTP is valid
        form_user = UserForm(request.POST)

        if form_user.is_valid():
            form_user.save()
            return redirect('success_page')
        else:
            return render(request, 'html/user.html', {'form_user': form_user, 'error_message': 'Invalid user information.'})
    else:
        form_user = UserForm()
        return render(request, 'html/user.html', {'form_user': form_user})
    '''
