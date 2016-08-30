from geojson_scraper import scrape


stations_url = "http://ilocal.carmarthenshire.gov.uk/mapping/assets?service=WFS&version=1.1.1&request=GetFeature&typeNames=Polling_Stations&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'W06000010'


scrape(stations_url, council_id, 'utf-8', 'stations')
