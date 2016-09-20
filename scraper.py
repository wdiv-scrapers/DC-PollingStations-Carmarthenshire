from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://ilocal.carmarthenshire.gov.uk/mapping/assets?service=WFS&version=1.1.1&request=GetFeature&typeNames=Polling_Stations&outputFormat=json&srsName=EPSG%3A4326&sortBy=register"
council_id = 'W06000010'


scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
scraper.scrape()
