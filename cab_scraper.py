import requests
from utils.DBHelper import Cab
from utils import DBHelper
from utils.time_utils import convert_datetime_string_to_time

URL = 'https://embed.liveviewgps.com/embedPlot.aspx'


def get_data():
    headers = {"Host": "embed.liveviewgps.com",
               "Origin": "https://embed.liveviewgps.com",
               "Referer": "https://embed.liveviewgps.com/embed.aspx",
               "X-Requested-With": "XMLHttpRequest",
               "DNT": "1",
               "Cookie": "org_id=30;"}

    resp = requests.post(URL, headers=headers)
    return resp.json()


# creates and returns Cab model
def create_cab_model(cab):
    name = cab['device']
    id = cab['did']
    heading = cab['heading']
    ignition = cab['ignition']
    latitude = cab['lat']
    longitude = cab['lng']
    moved = convert_datetime_string_to_time(cab['moved'])
    updated = convert_datetime_string_to_time(cab['updated'])
    velocity = cab['velocity']
    cab = Cab(name=name, id=id, heading=heading, ignition=ignition, latitude=latitude, longitude=longitude, moved=moved,
              updated=updated, velocty=velocity)
    return cab


def analyze_data(data_json):
    all_cabs_data = data_json['devices']
    cabs = []
    for cab_data in all_cabs_data:
        cab = create_cab_model(cab_data)
        cabs.append(cab)

    return cabs


def run():
    print 'Getting data'
    data = get_data()
    print 'Got data'
    print 'Analyzing data'
    cabs = analyze_data(data)
    print 'Analyzed data'
    print 'Putting in DB'
    DBHelper.update_all_cabs(cabs)
    print 'Completed'


if __name__ == '__main__':
    run()
