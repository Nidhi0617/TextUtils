from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def analyze(request):
    #GET THE TEXT
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalize=request.POST.get('capitalize','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    charcount=request.POST.get('charcount','off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+ char
        djtext=analyzed
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
    if capitalize == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        djtext = analyzed
        params = {'purpose': 'Capitalized', 'analyzed_text': analyzed}
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed = analyzed+char
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ''):
                analyzed = analyzed+char
        params = {'purpose': 'Extra Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcount == 'on':
        analyzed = len(djtext)
        params = {'purpose': 'Char Count', 'analyzed_text': analyzed}
        djtext = analyzed
    if (removepunc !='on' and capitalize !='on' and newlineremover !='on' and extraspaceremover!='on' and
    charcount !='on'):
        return HttpResponse('Please select the operations!')

    return render(request,'analyze.html',params)

