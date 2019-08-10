import urllib
import re


SECONDS_MINUTES_RE = re.compile('seconds="(\d+)" minutes="(\d+)"')
URLS = (
    ('10', 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&r=10&s=6966'),  # noqa E501
    ('48', 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a=sf-muni&r=48&s=3513'),  # noqa E501
)


def format_prediction(seconds, minutes):
    return '{}:{:0>2}'.format(
        minutes,
        int(seconds) % 60,
    )


def request_predictions():
    predictions = {}
    for stop, url in URLS:
        connection = urllib.urlopen(url)
        xml = connection.read()
        connection.close()
        predictions[stop] = [
            format_prediction(*seconds_minutes)
            for seconds_minutes
            in SECONDS_MINUTES_RE.findall(xml)[:2]
        ]
    return predictions
