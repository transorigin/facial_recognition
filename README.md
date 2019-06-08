## 惊奇六人组-表情识别项目

## 项目概况
    本项目是基于keras框架建立的表情识别工程，数据集为fer2013，基于自己的训练模型算法，具体过程为opencv识别人脸，然后将人脸框出来，接下来调用表情识别的函数，识别表情；
    django部分是前后端的中枢，通过调用后端的表情识别代码识别表情，具体过程为客户端上传表情图片到服务器，然后服务器识别表情，截至到目前，已经能够将表情识别后的图片保存服务器的目录中，还未进行前端输出部分。

## 项目功能

* 实现表情模型的训练
* 实现人脸的检测
* 实现表情的识别
* 实现django启动
* 实现django调用表情识别函数
* 基于django输出输出表情识别结果

## 项目效果

![1560003377888](./source/1560003377888.png)

## 项目结构

|-- facial  人脸表情识别核心部分
    |-- README.md
    |-- db.sqlite3
    |-- manage.py
    |-- nohup.out
    |-- .idea
    |   |-- dataSources.local.xml
    |   |-- dataSources.xml
    |   |-- facial_recognition.iml
    |   |-- misc.xml
    |   |-- modules.xml
    |   |-- other.xml
    |   |-- vcs.xml
    |   |-- workspace.xml
    |-- Expression 人脸表情使用的django app
    |   |-- __init__.py
    |   |-- admin.py
    |   |-- apps.py
    |   |-- function.py
    |   |-- models.py
    |   |-- tests.py
    |   |-- urls.py
    |   |-- views.py
    |   |-- emoji
    |   |   |-- angry.png
    |   |   |-- disgust.png
    |   |   |-- fear.png
    |   |   |-- happy.png
    |   |   |-- neutral.png
    |   |   |-- sad.png
    |   |   |-- surprise.png
    |   |-- img  存储上传的图片
    |   |-- migrations
    |   |   |-- __init__.py
    |   |   |-- __pycache__
    |   |       |-- __init__.cpython-36.pyc
    |   |-- static # 存放静态图像
    |   |   |-- JMU1.jpg
    |   |   |-- JMU2.jpg
    |   |   |-- JMU3.jpg
    |   |   |-- JMU4.jpg
    |   |   |-- layui.css
    |   |   |-- layui.js
    |   |   |-- login1.jpg
    |   |   |-- login2.jpg
    |   |   |-- pw.PNG
    |   |   |-- test.jpg
    |   |   |-- lay
    |   |       |-- modules
    |   |           |-- carousel.js
    |   |           |-- code.js
    |   |           |-- colorpicker.js
    |   |           |-- element.js
    |   |           |-- flow.js
    |   |           |-- form.js
    |   |           |-- jquery.js
    |   |           |-- laydate.js
    |   |           |-- layedit.js
    |   |           |-- layer.js
    |   |           |-- laypage.js
    |   |           |-- laytpl.js
    |   |           |-- mobile.js
    |   |           |-- rate.js
    |   |           |-- slider.js
    |   |           |-- table.js
    |   |           |-- tree.js
    |   |           |-- upload.js
    |   |           |-- util.js
    |   |-- templates  存放模板页面
    |       |-- index.html
    |-- facial
    |   |-- confusion_matrix.py
    |   |-- convert_csv2gray.py
    |   |-- convert_current.py
    |   |-- convert_fer2013.py
    |   |-- emotion_classifier.py
    |   |-- emotion_train_self.py
    |   |-- __pycache__
    |   |   |-- emotion_classifier.cpython-36.pyc
    |   |-- img_store
    |   |   |-- 1.jpg
    |   |-- pic
    |       |-- haarcascade_frontalface_alt.xml
    |       |-- model
    |       |   |-- model_fit_log
    |       |   |-- model_json.json
    |       |   |-- model_weight.h5
    |       |-- picTest
    |           |-- 0.jpg
    |           |-- 1.jpg
    |           |-- 10.jpg
    |           |-- 2.jpg
    |           |-- 4.jpg
    |           |-- 5.jpg
    |           |-- 6.jpg
    |           |-- 7.jpg
    |           |-- 8.jpg
    |           |-- 9.jpg
    |-- project   django的配置部分
        |-- __init__.py
        |-- settings.py
        |-- urls.py
        |-- wsgi.py

## 实现原理

### 人脸表情识别部分

1.通过网上的资源获取fer2013数据集，该数据集是免费的

2.通过keras框架训练卷积神经网络，训练出模型

3.opencv检测人脸

4.opencv框出的人脸，使用我们的模型来识别表情

5.通过opencv API的运用，输出表情图片框出来的人物表情

### django部分

1.template存放主页的代码

2.通过使用jquery的ajax来请求人脸表情识别函数

3.暂时通过使用static来存放表情识别出来的图片

## 项目使用

本项目已在conda中搭建了虚拟环境，后期我们会将虚拟环境上传至git，目前项目还在进行中

### 项目成员使用

​	已在云服务器上搭建我们项目的python环境

- 启动虚拟环境

```python
source activate facial
```

- 训练模型

```python
python emotion_train_self.py 
```

- 使用模型（基于django调用来使用模型）

```python
python manage.py runserver 0.0.0.0:80
```

## 
