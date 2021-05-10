from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

from was_rest.models import *
from was_front.forms import *
import csv

import pandas as pd
import os
from sklearn.metrics import f1_score

def get_SKH_score_2021(submission_path):
    score = 0.0
    return score

def get_SKT_score(submission_path):
    answer_path = "was_front/mysuni/answer_skt.csv"
    submission_path = submission_path
    with open(answer_path, 'r') as t1, open(submission_path, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

    count = 0
    wrong = 0
    score = 0.0
    for line in filetwo:
        if line not in fileone:  wrong +=1
        count += 1

    score = round((count - wrong) / count *100, 3)

    print(score)

    t1.close()
    t2.close()
    
    return score

def get_SKC_score(submission_path):
    answer_path = "was_front/mysuni/answer_skc.csv"
    score = 0.0
    answer_df = pd.read_csv(answer_path)
    submission_df = pd.read_csv(submission_path)

    submission_dict = dict(zip(list(submission_df['img_name']), list(submission_df['defect'])))  # make dictionary 
    answer_df['submission'] = answer_df['img_name'].map(submission_dict)

    answer_df.head()

    score = f1_score(answer_df['defect'], answer_df['submission'], average='weighted')

    print(score)
    return score


# Create your views here.
class MainView(View):

    def get(self, request , *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        scores_list = Score.objects.filter(user_id=Profile.objects.get(user=request.user))
        return render(self.request, 'main.html', {'scores': scores_list})



# Create your views here.
class SKTUploadView(View):

    def get(self, request , *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        scores_list = Score.objects.filter(company='skt').filter(user_id=Profile.objects.get(user=request.user)).order_by('-create_date')
        return render(self.request, 'skt_upload.html', {'scores': scores_list})

    def post(self, request):
        if not request.user.is_authenticated:
            return render(request, 'auth/login.html')
        print('upload data')
        print(request.FILES)
        score = Score(
            user_id = Profile.objects.get(user = request.user),
            file = request.FILES['file'],
            company = 'skt',
        )
        score.save()
        calc_score = get_SKT_score(score.file.path)
        score.score = calc_score
        score.save()
        data = {'is_valid': True, 'name': score.file.name, 'url': score.file.url, 'create_date':score.create_date, 'score': score.score}
        
        return JsonResponse(data)

class SKCUploadView(View):

    def get(self, request , *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        scores_list = Score.objects.filter(company='skc').filter(user_id=Profile.objects.get(user=request.user)).order_by('-create_date')
        return render(self.request, 'skc_upload.html', {'scores': scores_list})

    def post(self, request):
        if not request.user.is_authenticated:
            return render(request, 'auth/login.html')
        print('upload data')
        print(request.FILES)
        score = Score(
            user_id = Profile.objects.get(user = request.user),
            file = request.FILES['file'],
            company = 'skc',
        )
        score.save()
        calc_score = get_SKC_score(score.file.path)
        score.score = calc_score
        score.save()
        data = {'is_valid': True, 'name': score.file.name, 'url': score.file.url, 'create_date':score.create_date, 'score': score.score}
        
        return JsonResponse(data)

class SKTLeaderBoard(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        skt_global_score_list = Score.objects.filter(company = 'skt').order_by('-score')[0:20]
        skt_local_score_list = Score.objects.filter(company = 'skt').filter(user_id = Profile.objects.get(user=request.user)).order_by('-score')[0:20]
        return render(self.request, 'skt_leaderboard.html', {'global_score_list':skt_global_score_list, 'local_score_list':skt_local_score_list})

class SKCLeaderBoard(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        skc_global_score_list = Score.objects.filter(company = 'skc').order_by('-score')[0:20]
        skc_local_score_list = Score.objects.filter(company = 'skc').filter(user_id = Profile.objects.get(user=request.user)).order_by('-score')[0:20]
        return render(self.request, 'skc_leaderboard.html', {'global_score_list':skc_global_score_list, 'local_score_list':skc_local_score_list})

from django.contrib.auth.models import User
from django.contrib import auth
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('frontend:main')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    
    auth.logout(request)
    return redirect('frontend:login')