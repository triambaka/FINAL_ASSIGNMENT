#Collaborated with Sakshi
#Scrapping data from multiple HTML files along with multiple headers
#Scrapped data is stored in Weather.csv
from bs4 import BeautifulSoup
import urllib.request
import csv


f=open('Weather.csv','a+',newline='')
writer=csv.writer(f)
url='https://karki23.github.io/Weather-Data/'
list=['Albury.html','BadgerysCreek.html','Cobar.html','CoffsHarbour.html','Moree.html','Newcastle.html','NorahHead.html','NorfolkIsland.html','Penrith.html','Richmond.html','Sydney.html','SydneyAirport.html','WaggaWagga.html','Williamtown.html','Wollongong.html','Canberra.html','Tuggeranong.html','MountGinini.html','Ballarat.html','Bendigo.html','Sale.html','MelbourneAirport.html','Melbourne.html','Mildura.html','Nhil.html','Portland.html','Watsonia.html','Dartmoor.html','Brisbane.html','Cairns.html','GoldCoast.html','Townsville.html','Adelaide.html','MountGambier.html','Nuriootpa.html','Woomera.html','Albany.html','Witchcliffe.html','PearceRAAF.html','PerthAirport.html','Perth.html','SalmonGums.html','Walpole.html','Hobart.html','Launceston.html','AliceSprings.html','Darwin.html','Katherine.html', 'Uluru.html']
for n in list:
    base=f'{url}{n}'
    soup= BeautifulSoup(urllib.request.urlopen(base).read(), 'lxml')
    print(base)    
    tbody=soup('table')[0].find_all('tr')
    for row in tbody:
        cols=row.findChildren(recursive=False)
        cols=[ele.text.strip() for ele in cols]
        writer.writerow(cols)
        #print(cols)
        #Printing it will make it slow


#Shuffling the dataset in order to include many cities in the training set
#Shuffled data is stored in shuffled.csv
from random import shuffle

with open('Weather.csv') as ip:
    lines=ip.readlines()
    header = lines.pop(0)
    shuffle(lines)
    lines.insert(0, header)

with open('shuffled.csv','w') as out:
    out.writelines(lines)

#The header that has been included 49 times has to be present only once.
#Hence that and any other repeated data is removed and the rest is stored in Weather.csv    
from more_itertools import unique_everseen
with open('shuffled.csv','r') as f, open('Weather.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))
