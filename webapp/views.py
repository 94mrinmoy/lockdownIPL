from django.http import HttpResponse
from django.shortcuts import render
import service as s
from tabulate import tabulate
from .forms import NameForm
from .forms import NameForm2
from django.http import HttpResponseRedirect

def index(request):
    data = s.fixtures()
    # print(data)
    data = data.values.tolist()

    # table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]

    # data = tabulate(table, tablefmt='html')
    context= {
        'data': data,
        }
    # if 'points' == request.POST.get('submit'):
    #     print('here')  
    #     points(request)      
    return render(request, 'index2.html',context)

def points(request):
    data = s.getPoints()
    # print(data)
    datas = data.values.tolist()[3:]
    leaders = data.values.tolist()[:3]
    results = s.getResults()
    results = results.values.tolist()
    print(results)
    orangeData,purpleData = s.getBestPlayers()
    bestPlayer = orangeData.values.tolist()
    purpleData = purpleData.values.tolist()
    for i in range(len(bestPlayer)):
	    bestPlayer[i].append(purpleData[i][0])
	    bestPlayer[i].append(purpleData[i][1])
    context= {
        'data' : datas,
        'results' : results,
        'leaders' : leaders,
        'bestPlayer' : bestPlayer,
        # 'purpleData' : purpleData,
        }
    return render(request, 'index.html',context)    

def adminPortal(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(form.cleaned_data)
            global matchNo
            matchNo = form.cleaned_data['match_no']
            {'match_no': '4', 'team1': 'KKR', 'team2': 'KIX', 'team1Run': '45', 'team1Wickets': '4', 'team1Overs': '5', 'team1Balls': '0', 'team2Run': '48', 'team2Wickets': '3', 'team2Overs': '4', 'team2Balls': '3'}
            team1 = form.cleaned_data['team1']
            team2 = form.cleaned_data['team2']
            team1Wickets = form.cleaned_data['team1Wickets']
            team2Wickets = form.cleaned_data['team2Wickets']
            team1Score = form.cleaned_data['team1Run']+'/'+form.cleaned_data['team1Wickets']+','+form.cleaned_data['team1Overs']+'.'+form.cleaned_data['team1Balls']
            team2Score = form.cleaned_data['team2Run']+'/'+form.cleaned_data['team2Wickets']+','+form.cleaned_data['team2Overs']+'.'+form.cleaned_data['team2Balls']
            s.getNRR(matchNo,team1,team2,team1Score,team2Score,team1Wickets,team2Wickets)
            return HttpResponseRedirect('/points/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'index3.html', {'form': form})   

def adminPortal2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm2(matchNo).form2()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form.cleaned_data)
            return HttpResponseRedirect('/adminportal2/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm2(matchNo).form2()

    return render(request, 'index4.html', {'form': form})   

    