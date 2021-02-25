from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from .form import Pass_generator
from django.core.mail import send_mail
from django.conf import settings
from pass_gen.settings import EMAIL_HOST_USER
import random
import os

# Create your views here.
def index(request):
    """docstring forpassword_generator """
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '/', '|', '~', '>','*',]
    combined_set = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS
    rand_digit = random.choice(DIGITS)
    rand_lower_case = random.choice(LOCASE_CHARACTERS)
    rand_upper_case = random.choice(UPCASE_CHARACTERS)
    rand_Symbols = random.choice(SYMBOLS)
    temp_pass = rand_digit + rand_lower_case + rand_upper_case + rand_Symbols
    tempp = rand_digit + rand_lower_case + rand_Symbols + rand_upper_case + random.choice(combined_set)
    t = tempp
        #print(f" weeak password      : {tempp}")
    tem = list(tempp)
    random.shuffle(tem)
    z = rand_lower_case + rand_Symbols + rand_upper_case + rand_digit
    temp_pass2 = (z.join(combined_set))
    s = temp_pass2[:8]
        #print(f" Medium Password     : {temp_pass2[:8]}")
    z1 = list(temp_pass2)
    random.shuffle(z1)
    x = rand_upper_case + rand_lower_case + rand_digit + rand_Symbols
    temp_pass3 = (x.join(combined_set))
    r = temp_pass3[:10]
        #print(f" Strong Password     : {temp_pass3[:10]}")
    x1 = list(temp_pass3)
    random.shuffle(x1)
    y = random.choice(combined_set) + rand_lower_case + rand_upper_case +rand_digit + rand_Symbols
    temp_pass4 = (y.join(combined_set))
    q =  temp_pass4[:16]
        #print(f" Complex Password    : {temp_pass4[:12]}")
    y1 = list(temp_pass4)
    random.shuffle(y1)
    dict = {
        "Week_password" : t,
        "Medium_Password": s,
        "Strong_Password": r,
        "Complex_Password": q
    }
    # form genearation 
    if request.method == 'POST':
        fm = Pass_generator(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['Full_name']
            em = fm.cleaned_data['Email_ID']
            print('Name:', nm)
            print('Email:', em)
            print(os.getenv("EMAIL_ID"))
            fm.save()
            subject = "Welcome to Password Generator"
            message = f" Hello {nm}, \n \n Thank you for using the Password generator \n \n Below are the passwords\n  \n week_password : {t} \n Medium_password : {s} \n Strong Password : {r} \n Complex_password : {q}  \n  \n \n \n Regards, \n PASSWORD GENERATOR\n contact : 9748901762"
            recepient = str(fm['Email_ID'].value())
            send_mail(subject, message , EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request, 'pg/pass_gen.html', {'n':nm, 'em': em, 'dict':dict})
        # send_mail(
        #    'Password Generator',
        #    'Than you for using password gernerator',
        #     settings.EMAIL_HOST_USER,
        #     ['sudhirmd@zohomail.in'],
        #     fail_silently=False)
    else:
        fm = Pass_generator()
        return render(request, 'pg/index.html', {'form':fm})

    
    # if request.method == 'POST':
    #     form = pass_generator(request.POST)
    #     # form = AuthenticationForm(data=request.POST)
    #     if form.is_valid():
    #         print("form validated !")
    #         print('NAME: ', form.cleaned_data['Full_name'])
    #         name = form.request.POST.get['form.Full_name']
    #         print(name)
    #         email = form.cleaned_data['Email_ID']
    #         print(email)
    #         form.save()
    #         return render(request, 'pg/pass_gen.html', {'nm': name})
    # else:
    #     context = {'form': form}
    #     form = AuthenticationForm()
    #     return render(request, 'pg/index.html', context)

def Need_of_password(request):
    return render(request, 'pg/Need_of_password.html')

def contact_us(request):
    return render(request, 'pg/contact_us.html')

# def pass_gen(request):

#     """docstring forpassword_generator """
#     DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
#                      'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
#                      'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#                      'z']
#     UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
#                      'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
#                      'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
#                      'Z']
#     SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '/', '|', '~', '>','*',]
#     combined_set = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS
#     rand_digit = random.choice(DIGITS)
#     rand_lower_case = random.choice(LOCASE_CHARACTERS)
#     rand_upper_case = random.choice(UPCASE_CHARACTERS)
#     rand_Symbols = random.choice(SYMBOLS)
#     temp_pass = rand_digit + rand_lower_case + rand_upper_case + rand_Symbols
#     tempp = rand_digit + rand_lower_case + rand_Symbols + rand_upper_case + random.choice(combined_set)
#     t = tempp
#         #print(f" weeak password      : {tempp}")
#     tem = list(tempp)
#     random.shuffle(tem)
#     z = rand_lower_case + rand_Symbols + rand_upper_case + rand_digit
#     temp_pass2 = (z.join(combined_set))
#     s = temp_pass2[:8]
#         #print(f" Medium Password     : {temp_pass2[:8]}")
#     z1 = list(temp_pass2)
#     random.shuffle(z1)
#     x = rand_upper_case + rand_lower_case + rand_digit + rand_Symbols
#     temp_pass3 = (x.join(combined_set))
#     r = temp_pass3[:10]
#         #print(f" Strong Password     : {temp_pass3[:10]}")
#     x1 = list(temp_pass3)
#     random.shuffle(x1)
#     y = random.choice(combined_set) + rand_lower_case + rand_upper_case +rand_digit + rand_Symbols
#     temp_pass4 = (y.join(combined_set))
#     q =  temp_pass4[:16]
#         #print(f" Complex Password    : {temp_pass4[:12]}")
#     y1 = list(temp_pass4)
#     random.shuffle(y1)
#     dict = {
#         "Week_password" : t,
#         "Medium_Password": s,
#         "Strong_Password": r,
#         "Complex_Password": q
#     }
#     # content = " "
#     # for x, y in This_dict.items():
#     #     content =(x,y)
    # return render(request, 'pg/pass_gen.html', {})