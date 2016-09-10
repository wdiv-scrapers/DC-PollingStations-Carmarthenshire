from gml_scraper import scrape


stations_url = "http://ilocal.carmarthenshire.gov.uk/mapping/assets?service=WFS&version=1.1.1&request=GetFeature&typeNames=Polling_Stations&srsName=EPSG%3A4326"
stations_fields = {
    '{http://www.carmarthenshire.gov.uk/}register': 'register',
    '{http://www.carmarthenshire.gov.uk/}address': 'address',
    '{http://www.carmarthenshire.gov.uk/}postcode': 'postcode',
}

council_id = 'W06000010'


scrape(stations_url, council_id, 'stations', stations_fields, 'register', xml_format='wfs/2.0')
