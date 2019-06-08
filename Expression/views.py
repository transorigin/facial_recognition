from django.shortcuts import render
from django.http import HttpResponse
from Expression import function
import os


# Create your views here.
def index(request):
<<<<<<< HEAD
=======
#    print("`1111")
>>>>>>> a3582187c74a4d6adf80bf396c51f55ff4e9b3e6
    return render(request, 'index.html')


def get(request):
    a = request.POST['a']
    b = request.POST['b']
    print(a)
    print(b)
    return render(request, 'index.html')


def uploadFile(request):
    print(request)
    print("123")
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("img", None)  # 获取上传的文件，如果没有文件，则默认为None
        print("myFile:", myFile)
        print(myFile.name)
        if not myFile:
            return HttpResponse("no files for upload!")
        print(os.getcwd())
        imgPath = './Expression/img/' + myFile.name
        destination = open(imgPath, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        #
        # 表情识别接口
        if myFile:
            img, emoStore = function.recFacial(imgPath, myFile.name)
        print(os.path)
        # 返回表情识别结果
        return HttpResponse(img, content_type="image/jpg")


def test(request):
    return HttpResponse('success')
