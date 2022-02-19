from django.shortcuts import render , redirect

# Create your views here.
def index(request):
    return render(request , "var/index.html")

def variables01(request):
    my_list = ['python' , 'django' , 'templates']
    return render(request , "var/variables01.html", {"lst":my_list})

def variables02(request):
    my_dict = {"class" : "multi" , "name" : "hong-gd"}
    return render(request , "var/variables02.html" , {"dct":my_dict})

def for_loop(request):
    return render(request , 'var/forloop.html' , {"number" : range(1,11)})

# django가 가진 기본 탬플릿 엔진에서는  for i in range가 먹히지 않는다. -> 그래서 views에서 미리 만들어서 전달


def if01(request):
    return render(request, 'var/if01.html' , {'user':{'id':'kim-sd' , 'job': 'student'}})

def if02(request):
    return render(request , 'var/if02.html' , {'role' : 'manager' , 'id': 'multi'})

def href(request):
    return render(request, 'var/href.html')

def get_post(request):
    if request.method == 'GET':
        return render(request, 'var/get.html')
    elif request.method == 'POST':
        return render(request , 'var/post.html')
    else:
        return redirect('index')