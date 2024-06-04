from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accountapp.forms import MemberForm
from accountapp.models import Member

res_data = {}

# Create your views here.
def signup(request):
    if request.method=="POST":
        form = MemberForm(request.POST)
        email=request.POST['email']
        password = request.POST['password']
        lenpwd=len(password)
        checkpwd = request.POST['checkpwd']
        if not (email and password and checkpwd):
            res_data['error_msg'] = "모든 값을 입력해야 합니다."
        elif (password != checkpwd):
            res_data['error_msg'] = '비밀번호가 다릅니다.'
        elif Member.objects.filter(email=email).exists():
            res_data['error_msg']='동일한 이메일로 가입한 회원이 있습니다.'
        elif (lenpwd<8 or lenpwd>20):
            res_data['error_msg']='비밀번호는 8자리 이상, 20자리 이하로 설정하세요.'
        elif form.is_valid():
            email1 = form.clean_email()
            form = Member(email=email1, password=make_password(password))
            form.save()
            return redirect('/')

    return render(request, 'accountapp/signup.html', res_data)

