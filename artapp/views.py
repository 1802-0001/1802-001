from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # 请求路径和请求方法
    print(request.path, '\n\n', request.method, '\n\n')

    # 请求头的元信息
    print(request.META, '\n\n')

    # 请求头的GET请求参数（查询参数）
    print(request.GET, '\n\n')
    print(request.GET.get('page'), request.GET.get('tag'))

    # 请求头的POST请求参数（表单参数）
    print(request.POST, '\n\n')

    # 请求头的元信息中的远程服务器地址REMOTE_ADDR
    print(request.META.get('REMOTE_ADDR'), '\n\n')

    # return HttpResponse('<h1>您好！</h1>')
    # return JsonResponse({'name':'disen', 'age':30})
    return render(request, 'art/list.html', context={'name':'disen', 'age':30})


