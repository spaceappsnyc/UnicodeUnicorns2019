import requests
import json
import pprint
from datetime import timedelta, date
import pandas as pd



start_date = date(1999, 1, 1).strftime('%Y-%m-%d')
end_date = date(2001, 12, 31).strftime('%Y-%m-%d')


beaufort_lat = '73'
beaufort_lon = '-150'

cacana_lat = '85'
cacana_lon = '-120'

cafram_lat = '85'
cafram_lon = '0'

esiber_lat = '82'
esiber_lon = '150'



def getCSVData(lat, lon, start_date, end_date):
    url = 'http://api.meteomatics.com/'+start_date+'T00:00:00Z'+ '--' + end_date + 'T00:00:00Z:P1D/t_2m:C,wind_speed_10m:kmh,relative_humidity_2m:p,direct_rad:W/'+lat+','+lon+'/csv'
    print (url)
    data = { 'username' : 'your_username', 'password' : 'your_password' }
    response = requests.get(url, auth=(data["username"], data["password"]))
    return response.text

def downloadAllDataFiles():

    beaufortMeteo = getCSVData(beaufort_lat, beaufort_lon, start_date, end_date)
    beaufortMeteoFile = open('dataset/beaufort99-01.csv', 'w+')
    beaufortMeteoFile.write(beaufortMeteo)
    beaufortMeteoFile.close()


    cacanaMeteo = getCSVData(cacana_lat, cacana_lon, start_date, end_date)
    cacanaMeteoFile = open('dataset/cacana99-01.csv', 'w+')
    cacanaMeteoFile.write(cacanaMeteo)
    cacanaMeteoFile.close()


    caframMeteo = getCSVData(cafram_lat, cafram_lon, start_date, end_date)
    caframMeteoFile = open('dataset/cafram99-01.csv','w+')
    caframMeteoFile.write(caframMeteo)
    caframMeteoFile.close()

    esiberMeteo = getCSVData(esiber_lat, esiber_lon, start_date, end_date)
    esiberMeteoFile = open('dataset/esiber99-01.csv','w+')
    esiberMeteoFile.write(esiberMeteo)
    esiberMeteoFile.close()


downloadAllDataFiles()


#df = pd.read_csv('1999-2001-73--150.csv', header=None)

#print(df.head(20))

