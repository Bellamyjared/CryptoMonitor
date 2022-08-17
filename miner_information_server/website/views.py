from flask import Blueprint, render_template
import requests



# ~~~~~~~~~~GET DATA FROM APIs~~~~~~~~~~~~~~~~~
def GetData():
    urls = {
        "http://~~~~~~~/miner_data",
        "http://~~~~~~~/miner_data"
        }
    APIData = []
    for url in urls:
        try:
            r = requests.get(url)
            status = "PASS"
            APIData.append(r.json())
        except requests.exceptions.RequestException as err:
            status = "FAIL"


# ~~~~~~~~COUNT HOW MANY MINERS ARE ONLINE ~~~~~~~~~~~~~
    onlineMiners = 0
    totalMiners = 0

    for miners in APIData:
        for miner in miners:
            if ((miner[1]['status']) == 'error'):
                totalMiners = totalMiners + 1
            elif ((miner[2]['data']) == 'error'):
                totalMiners = totalMiners + 1
            else:
                totalMiners = totalMiners + 1
                onlineMiners = onlineMiners + 1

    if(totalMiners != 0):
        if (onlineMiners == totalMiners):
            totalStatus="✔️"
        elif (onlineMiners == 0):
            totalStatus="❌"
        else: totalStatus="⚠️"

                             
    return ([APIData, onlineMiners, totalMiners, totalStatus, status])




views = Blueprint('views', __name__)

@views.route('/')
def home():
    data = GetData()
    if(data[4] == "PASS"):
        return render_template("home.html", 
            request = data
        )
    else:
        return render_template("error.html")