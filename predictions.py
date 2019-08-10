import urllib
import re
URLS = (
    ('10', 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&r=10&s=6966'),  # noqa E501
    ('48', 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&r=48&s=3513'),  # noqa E501
)
SECONDS_MINUTES_RE = re.compile('seconds="(\d+)" minutes="(\d+)"')
def format_prediction(seconds, minutes):
    return '{}:{:0>2}'.format(
        minutes,
        int(seconds) % 60,
    )
    # return '{minutes}:{seconds}'.format(
    #     minutes=minutes,
    #     seconds=int(seconds) % 60,
    # )

def request_predictions():
    predictions = {}
    for stop, url in URLS:
        connection = urllib.urlopen(url)
        xml = connection.read()
        connection.close()
        predictions[stop] = [
            format_prediction(*tuple)
            for tuple
            in SECONDS_MINUTES_RE.findall(xml)[:2]
        ]
    return predictions
