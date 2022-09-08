import imp
import json
from unittest import result
from urllib import response
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import urllib.parse

from matplotlib.style import context
from .form import UserForm
from myapp02.models import Board
from myapp02.models import Comment, Forecast, Movie
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myapp02 import bigdataProcess
from django.db.models.aggregates import Avg, Count
import pandas as pd
# Create your views here.

UPLOAD_DIR = 'D:/djangoWork/upload/'


@login_required(login_url='/login/')
def insert_form(request):
    return render(request, 'board/insert.html')


@csrf_exempt
def insert(request):
    fname = ''
    fsize = 0
    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()
    dto = Board(writer=request.POST['writer'],
                title=request.POST['title'],
                content=request.POST['content'],
                filename=fname,
                filesize=fsize)
    dto.save()
    return redirect('/list/')


def list(request):
    boardList = Board.objects.all()
    context = {'boardList': boardList}
    return render(request, 'board/list.html', context)


def list_page(request):
    page = request.GET.get('page', '1')
    word = request.GET.get('word', '')
    boardCount = Board.objects.filter(Q(writer__contains=word) |
                                      Q(title__contains=word) |
                                      Q(content__contains=word)).count()

    boardList = Board.objects.filter(Q(writer__contains=word) |
                                     Q(title__contains=word) |
                                     Q(content__contains=word)).order_by('-id')

    pageSize = 5

    paginator = Paginator(boardList, pageSize)
    page_obj = paginator.get_page(page)

    rowNo = boardCount - (int(page)-1)*pageSize

    context = {'page_list': page_obj, 'page': page,
               'word': word, 'boardCount': boardCount, 'rowNo': rowNo}
    return render(request, 'board/list_page.html', context)


def detail_id(request):
    id = request.GET['id']
    dto = Board.objects.get(id=id)
    dto.hit_up()
    dto.save()
    return render(request, 'board/detail.html', {'dto': dto})


def detail(request, board_id):
    dto = Board.objects.get(id=board_id)
    dto.hit_up()
    dto.save()

    return render(request, 'board/detail.html', {'dto': dto})


def delete(request, board_id):
    Board.objects.get(id=board_id).delete()
    return redirect('/list/')


def update_form(request, board_id):
    dto = Board.objects.get(id=board_id)
    return render(request, 'board/update.html', {'dto': dto})


@csrf_exempt
def update(request):
    id = request.POST['id']
    dto = Board.objects.get(id=id)
    fname = dto.filename
    fsize = dto.filesize
    if 'file' in request.FILES:
        file = request.FILES['file']
        fname = file.name
        fsize = file.size
        fp = open('%s%s' % (UPLOAD_DIR, fname), 'wb')
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close

    dto_update = Board(id,
                       writer=request.POST['writer'],
                       title=request.POST['title'],
                       content=request.POST['content'],
                       filename=fname,
                       filesize=fsize)
    dto_update.save()
    return redirect('/list/')


@csrf_exempt
def comment_insert(request):
    id = request.POST['id']
    dto = Comment(board_id=id,
                  writer=request.POST['id'],
                  content=request.POST['content'])
    dto.save()
    return redirect('/detail_id?id='+id)


def download_count(request):
    id = request.GET['id']
    dto = Board.objects.get(id=id)
    dto.down_up()
    dto.save()
    count = dto.down
    return JsonResponse({'id': id, 'count': count})


def download(request):
    id = request.GET['id']
    dto = Board.objects.get(id=id)
    path = UPLOAD_DIR + dto.filename
    filename = urllib.parse.quote(dto.filename)
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(),
                                content_type='application/octet-stream')
        response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(
            filename)
        return response


# 회원가입

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            print('signup PSOT is_valid')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else:
            print('signup POST un_valid')
    else:
        form = UserForm()

    return render(request, 'common/signup.html', {'form': form})


def login_form(request):
    return render(request, 'common/login.html')


def melon(request):
    datas = []
    bigdataProcess.melon_crawing(datas)
    print(datas)
    return render(request, "bigdata/melon.html", {'data': datas})


def wordcloud(request):
    a_path = "D:/djangoWork/myPro02/myPro02/data/"
    data = json.loads(open(a_path+'4차 산업혁명.json',
                      'r', encoding='utf-8').read())
    bigdataProcess.make_wordCloud(data)
    return render(request, "bigdata/chart.html", {'img_data': 'k_wordCloud.png'})


def weather(request):
    last_date = Forecast.objects.values('tmef').order_by('-tmef')[:1]
    print('last_date :', len(last_date))
    weather = {}
    bigdataProcess.weater_crawling(last_date, weather)

    print("last_date query: ", str(last_date.query))
    for i in weather:
        for j in weather[i]:
            dto = Forecast(city=i, tmef=j[0], wf=j[1], tmn=j[2], tmx=j[3])
            dto.save()

    result = Forecast.objects.filter(city='부산')
    result1 = Forecast.objects.filter(city='부산').values(
        'wf').annotate(dcount=Count('wf')).values("dcount", "wf")
    print("result1 query:", str(result1.query))

    df = pd.DataFrame(result1)

    image_dic = bigdataProcess.weather_make_chart(result, df.wf, df.dcount)
    return render(request, "bigdata/chart1.html", {'img_data': image_dic})


def movie(request):
    data = []
    bigdataProcess.movie_crawling(data)
    for r in data:
        dto = Movie(title=r[0],
                    point=r[1],
                    content=r[2])
        dto.save()
    return redirect('/')


def movie_chart(request):
    data = Movie.objects.values('title').annotate(point_avg=Avg('point'))[0:10]
    df = pd.DataFrame(data)
    bigdataProcess.make_chart(df.title, df.point_avg)
    return render(request, 'bigdata/movie_chart.html', {'data': data, 'img_data': 'movie_fig.png'})


def map(request):
    bigdataProcess.map()
    return render(request, 'bigdata/map.html')


def tv(request):
    for i in range(1, 4):
        bigdataProcess.program_crawling(i)
    image_dic = {'plot': 'program1.png',
                 'bar': 'program2.png', 'pie': 'program3.png'}
    return render(request, "bigdata/chart1.html", {'img_data': image_dic})
