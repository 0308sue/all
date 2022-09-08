from fileinput import filename
from importlib.resources import path
from urllib import response
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
import urllib.parse
import math
from django.db.models import Q
from myapp01.models import Comment
from myapp01.models import Board
# Create your views here.

UPLOAD_DIR = 'D:/djangoWork/upload/'


def write_form(request):
    return render(request, 'board/write.html')


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


# def list(request):
#     boardList = Board.objects.all()
#     context = {'boardList': boardList}
#     return render(request, 'board/list.html', context)

def list(request):
    page = request.GET.get('page', 1)
    word = request.GET.get('word', '')
    field = request.GET.get('field', 'title')
    if field == 'all':
        boardCount = Board.objects.filter(Q(writer__contains=word) |
                                          Q(title__contains=word) |
                                          Q(content__contains=word)).count()
    elif field == 'writer':
        boardCount = Board.objects.filter(Q(writer__contains=word)).count()
    elif field == 'title':
        boardCount = Board.objects.filter(Q(title__contains=word)).count()
    elif field == 'content':
        boardCount = Board.objects.filter(Q(content__contains=word)).count()
    else:
        boardCount = Board.objects.all().count()

    boardList = Board.objects.all()
    pagesize = 5
    blockPage = 3
    currentPage = int(page)
    start = (currentPage-1)*pagesize
    totPage = math.ceil(boardCount/pagesize)
    startPage = math.floor((currentPage-1)/blockPage)*blockPage+1
    endPage = startPage+blockPage-1

    if endPage > totPage:
        endPage = totPage

    if field == 'all':
        boardList = Board.objects.filter(Q(writer__contains=word) |
                                         Q(title__contains=word) |
                                         Q(content__contains=word)).order_by('-idx')[start:start+pagesize]
    elif field == 'writer':
        boardList = Board.objects.filter(
            Q(writer__contains=word)).order_by('-idx')[start:start+pagesize]
    elif field == 'title':
        boardList = Board.objects.filter(
            Q(title__contains=word)).order_by('-idx')[start:start+pagesize]
    elif field == 'content':
        boardList = Board.objects.filter(
            Q(content__contains=word)).order_by('-idx')[start:start+pagesize]
    else:
        boardList = Board.objects.all().order_by('-idx')[start:start+pagesize]

    context = {'boardList': boardList,
               'startpage': startPage, 'blockpage': blockPage, 'endpage': endPage, 'range': range(startPage, endPage+1),
               'boardcount': boardCount, 'currentpage': currentPage, 'totpage': totPage, 'field': field, 'word': word}
    return render(request, 'board/list.html', context)


def detail_idx(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()

    commentList = Comment.objects.filter(board_idx=id).order_by('-idx')

    return render(request, 'board/detail.html', {'dto': dto, 'commentList': commentList})


# detail/<int:board_idx>
def detail(request, board_idx):
    dto = Board.objects.get(idx=board_idx)
    dto.hit_up()
    dto.save()
    commentList = Comment.objects.filter(board_idx=board_idx).order_by('-idx')

    return render(request, 'board/detail.html', {'dto': dto, 'commentList': commentList})


def delete(request, board_idx):
    Board.objects.get(idx=board_idx).delete()
    return redirect('/list/')


def update_form(request, board_idx):
    dto = Board.objects.get(idx=board_idx)
    return render(request, 'board/update.html', {'dto': dto})


@csrf_exempt
def update(request):
    id = request.POST['idx']
    dto = Board.objects.get(idx=id)
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


def download_count(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx=id)
    print(id)
    # path = UPLOAD_DIR + dto.filename
    dto.down_up()
    dto.save()
    count = dto.down
    print(count)

    return JsonResponse({'idx': id, 'count': count})


def download(request):
    id = request.GET['idx']
    print('id : ', id)

    dto = Board.objects.get(idx=id)
    path = UPLOAD_DIR + dto.filename
    filename = urllib.parse.quote(dto.filename)
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(),
                                content_type='application/octet-stream')
        response['Content-Disposition'] = "attachment;filename*=UTF-8''{0}".format(
            filename)
        return response


@csrf_exempt
def comment_insert(request):
    id = request.POST['idx']
    dto = Comment(board_idx=id,
                  writer='aa',
                  content=request.POST['content'])
    dto.save()
    return redirect('/detail_idx?idx='+id)
