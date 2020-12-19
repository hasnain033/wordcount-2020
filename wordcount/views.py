from django.http import HttpResponse
from django.shortcuts import render


def home(request):

	return render(request,'home.html')


def count(request):
	fulltext=request.GET['fulltext']
	textList=fulltext.split()
	wordcount={}
	for word in textList:
		if word in wordcount:
			wordcount[word]+=1
		else:
			wordcount[word]=1

	return render(request,'count.html',{'wordlist':wordcount,'totalword':len(textList)})