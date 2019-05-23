from django.shortcuts import render
import requests
import json
import xmltodict
import pickle


# Create your views here.

def home(request):    
    if request.method =="POST":
        startST = request.POST.get('startST')
        
        apiKey = ''
        raw_data = requests.get(f'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?serviceKey='+apiKey).content
        xmlObject = xmltodict.parse(raw_data)
        busData = xmlObject['ServiceResult']['msgBody']['itemList']
        # query = pickle.loads(startST)
        # qs = busData.objects.all()
        # qs.query = query
        
        busDataSorted =[]
        for data in busData:
            busDataSorted.append({
                'arStation': data['edStationNm'],
                'stStation': data['stStationNm'],
                'firstBus': data['firstBusTm'],
                'lastBus': data['lastBusTm'],
                'term': data['term']
            })
        
        return render(request, 'result.html', {'busDataSorted': busDataSorted})
    
    else:
        return render(request, 'home.html')
def result(request):
    return render(request, 'result.html')


# # def home(request):
# apiKey = 'HG2TuxqoS3g908JrZdJVzQ50myJPPRcqNXnsvEVf583kC1R35ThFM7wnJTwkO5cJzku%2FjgSLJoTcBVxzzYn5Uw%3D%3D'
# raw_data = requests.get(f'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?serviceKey='+apiKey).content
# xmlObject = xmltodict.parse(raw_data)

# # print(type(raw_data))
# # print(xmlObject)
# busData = xmlObject['ServiceResult']['msgBody']['itemList']
# # for data in busData:
# #     print(data['corpNm']+'회사 정보')
# #     print('출발지'+data['edStationNm'])
# #     print('첫차시간'+data['firstBusTm'])
# #     print('막차시간'+data['lastBusTm'])
# #     print('도착지'+data['stStationNm'])
# #     print('간격'+data['term'])
# busDataSorted =[]
# for data in busData:
#     busDataSorted.append({
#         'arStation': data['edStationNm'],
#         'stStation': data['stStationNm'],
#         'firstBus': data['firstBusTm'],
#         'lastBus': data['lastBusTm'],
#         'term': data['term']
#     })

#     return render(request, 'home.html', {'busDataSorted': busDataSorted})
# def bus_api(request):
#     qs = busDataSorted
#     # if request.method =="POST":
#     startStation = request.POST.get('startStation')
#     arrivalStation = request.POST.get('arrivalStation')

#     if  startStation:
#         qs = qs.filter('stStation' = startStation)
#         if arrivalStation:
#             qs = qs.filter('arStation' = arrivalStation)
#     return render(request, 'result.html', {})

