from django.shortcuts import render
from django.http import HttpResponse
import json


# from facial import emotion_classifier

# Create your views here.
def index(request):
    return render(request, 'index.html')


def get(request):
    a = request.POST['a']
    b = request.POST['b']
    print(a)
    print(b)
    return render(request, 'index.html')


def uploadFile(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("img", None)  # 获取上传的文件，如果没有文件，则默认为None
        print(myFile.name)
        if not myFile:
            return HttpResponse("no files for upload!")
        import os

        # destination = open(os.path.join("D:\\upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        # for chunk in myFile.chunks():  # 分块写入文件
        #     destination.write(chunk)
        # destination.close()

        # 表情识别接口
        # if myFile:
        #     print(emotion_classifier.predict_emotion(myFile))
        print(os.path)
        # 返回表情识别结果
        return HttpResponse("成功")
