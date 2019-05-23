from django.shortcuts import render
import requests
import json
import xmltodict


apiKey = 'HG2TuxqoS3g908JrZdJVzQ50myJPPRcqNXnsvEVf583kC1R35ThFM7wnJTwkO5cJzku%2FjgSLJoTcBVxzzYn5Uw%3D%3D'
raw_data = requests.get(f'http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?serviceKey='+apiKey).content
xmlObject = xmltodict.parse(raw_data)

# print(type(raw_data))
# print(xmlObject)
busData = xmlObject['ServiceResult']['msgBody']['itemList']
print('버스 노선 정보')
for data in busData:
    print('노선번호 : ' + data['busRouteNm'])
    print('출발지 : '+data['edStationNm'])
    print('첫차시간 : '+data['firstBusTm'])
    print('막차시간 : '+data['lastBusTm'])
    print('도착지 : '+data['stStationNm'])
    print('간격 : '+data['term'])
    print('-------------------------------------------------')