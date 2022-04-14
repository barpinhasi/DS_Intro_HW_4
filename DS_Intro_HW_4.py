import requests
API_KEY = input("enter your google api key: ")
dest = 'Jerusalem'
citys = open('dests.txt','r').read().splitlines()
data = {}
furthest = []
count = 0

for c in citys:
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?destinations=%s&origins=%s&key=%s" % (dest,c,API_KEY)
    response = requests.get(url).json()
    url2 = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (c,API_KEY)
    response2 = requests.get(url2).json()
    distance = response['rows'][0]['elements'][0]['distance']['text']
    duration = response['rows'][0]['elements'][0]['duration']['text']
    latitude = response2['results'][0]['geometry']['location']['lat']
    longtiude = response2['results'][0]['geometry']['location']['lng']
    if duration.find('days') != -1 or duration.find('day') != -1:
        dur = duration.split()
        if len(dur) == 4:
            dur = str(int(dur[0])*24+int(dur[2]))+' hours'
            duration = dur
        elif len(dur) == 6:
            dur = str(int(dur[0])*24+int(dur[2]))+' hours '+str(dur[5])+' mins'
            duration = dur
        elif len(dur) == 2:
            dur = str(int(dur[0])*24)+' hours'
            duration = dur
     
    data[c] = (distance,duration,longtiude,latitude)
    if count >= 3:
        if distance > min(furthest):
            furthest.remove(min(furthest))
            furthest.append(distance)
    else:
        furthest.append(distance)
        count = count + 1
temp = {}
for i in data:
    if data[i][0] in furthest:
        temp[i] = data[i][0]
print(data)
print(" ")
print('The furthest cities from Jerusalem are:',temp)