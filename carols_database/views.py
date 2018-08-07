from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html', {'key': 'yet another test'})

def finalcount(request):
    original_text = request.GET['fulltext']
    split_text = original_text.split()
    word_count = len(split_text)
    wordDict = {}
    for word in split_text:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    return render(request, 'finalcount.html', {'original_text':original_text, 'word_count': word_count, 'wordDict': wordDict.items()})

def troll(request):
    return render(request, 'troll.html')
