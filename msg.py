import requests
import csv
from csv import reader

def sms(name,time):

    url = "https://www.fast2sms.com/dev/bulk"

    querystring = {"authorization":"NLieK4M0ENVgqwuZKCzyHF1zrHuDLoNJaCfHnetZABdPqYPoEgj5PcswWWSo",
                   "sender_id":"FSTSMS",
                   "message":"WARNING !!!... "+name+"have been seen at time"+time+" .",
                   "language":"english",
                   "route":"p",
                   "numbers":"7415640671"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
sms("himanshu","09:27:50")
# with open('culprit_list.csv', 'r') as read_obj:
#     csv_reader = reader(read_obj)
#     header = next(csv_reader)
#     if header != None:
#         for row in csv_reader:
#             if len(row) != 0:
#                 name = row[0]
#                 time = row[1]
#                 print(name,time)
#                 sms(name,time)


