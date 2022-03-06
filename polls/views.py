#!/usr/bin/python
# -*- coding: UTF-8 -*-
#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("你好，这里是在线投票系统。")

def detail(request, question_id):
    return HttpResponse("将为您打开问卷 %s。" % question_id)

def results(request, question_id):
    response = "正在查看问卷 %s 的结果。"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("请为问卷 %s 提交您的答案。" % question_id)