import datetime
import sys

from zeep import Client
from requests import Session
from requests.auth import HTTPBasicAuth  # or HTTPDigestAuth, or OAuth1, etc.
from zeep.transports import Transport

# NRDM WebService Python Client API
# Utilizes NRDM SOAP Webservice
# Jeremy Espino MD 2020/03/25
# juest4@pitt.edu

class NrdmWs:
    username = ""
    password = ""
    endpoint = "http://localhost:8888/nrdm-jax-ws?wsdl"
    category = {'Antifever adult': 1,
                'Antifever pediatric': 2,
                'Bronchial remedies': 3,
                'Chest rubs': 4,
                'Cold relief adult liquid': 5,
                'Cold relief adult tablet': 6,
                'Cold relief pediatric liquid': 7,
                'Cold relief pediatric tablet': 8,
                'Cough syrup adult liquid': 9,
                'Cough adult tablet': 10,
                'Cough syrup pediatric liquid': 11,
                'Diarrhea remedies': 12,
                'Electrolytes pediatric': 13,
                'Hydrocortisones': 14,
                'Nasal product internal': 15,
                'Thermometer adult': 16,
                'Thermometer pediatric': 17,
                'Throat Lozenges': 18,
                'Baby/Child Electrolytes': 19,
                'Cough/Cold': 20,
                'Internal Analgesics': 21,
                'Stomach Remedies': 22,
                'Thermometers': 23}
    region_type = {'state': 1, 'county': 2, 'zipcode': 3}

    def __init__(self, username, password, endpoint):
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.client = None
        self.initClient()

    def initClient(self):
        session = Session()
        session.auth = HTTPBasicAuth(self.username, self.password)
        self.client = Client(self.endpoint, transport=Transport(session=session))

    def isAlive(self):
        return self.client.service.isAlive()

    def getZipLevelCompletion(self, zipcode):
        return self.client.service.getZipLevelCompletion(zipcode)

    def getCountyLevelCompletion(self, county_fips):
        return self.client.service.getCountyLevelCompletion(county_fips)

    def getStateLevelCompletion(self, state_abbrev):
        return self.client.service.getStateLevelCompletion(state_abbrev)

    def getZipLevelCount(self, startDate, endDate, zipcode, category, normalize):
        return self.client.service.getZipLevelCount(startDate, endDate, zipcode, category,normalize, self.username)

    def getCountyLevelCount(self, startDate, endDate, county_fips, category, normalize):
        return self.client.service.getCountyLevelCount(startDate, endDate, county_fips, category,
                                                       normalize,self.username)

    def getJurisdictionLevelCount(self, startDate, endDate, jurisdiction, category, normalize):
        return self.client.service.getJurisdictionLevelCount(startDate, endDate, jurisdiction, category,
                                                             normalize, self.username)

    def getStateLevelCount(self, startDate, endDate, state_abbrev, category, normalize):
        return self.client.service.getStateLevelCount(startDate, endDate, state_abbrev, category, normalize, self.username)


    def getCountMultiRegions(self, startDate, endDate, regions, regionType, categories, normalize):
        return self.client.service.getCountMultiRegions(startDate, endDate, regions,regionType, categories,
                                                         normalize, self.username)

    def getZipcodeSeries(self, date, regionType, regionID, category, promotionOption):
        return self.client.service.getZipcodeSeries(date, regionType, regionID, category, promotionOption,
                                                     self.username)


    def getAlgorithmOutput(self, startDate, endDate, regions, regionType, categoryIDs ):
        return self.client.service.getAlgorithmOutput(startDate, endDate, regions, regionType, categoryIDs,self.username)





def main():
    if len(sys.argv) != 4:
        print("Usage: NrdmWs.py <username> <password> <endpoint>")
        exit()
    username = sys.argv[1]
    password = sys.argv[2]
    endpoint = sys.argv[3]
    nrdmWs = NrdmWs(username, password, endpoint)
    
    state_abbrev_to_test = "PA"
    county_fips_to_test = "42001"
    zipcode_to_test = "15228"
    counties_fips_to_test = "42001,42003"
    zipcodes_to_test = "15228,15206"
    states_to_test = "PA,OH"
    


    print("nrdmWs.isAlive()")
    print(nrdmWs.isAlive())

    print("nrdmWs.getStateLevelCompletion(state_abbrev_to_test)")
    print(nrdmWs.getStateLevelCompletion(state_abbrev_to_test))

    print("nrdmWs.getCountyLevelCompletion(county_fips_to_test)")
    print(nrdmWs.getCountyLevelCompletion(county_fips_to_test))

    print("nrdmWs.getZipLevelCompletion(zipcode_to_test)")
    print(nrdmWs.getZipLevelCompletion(zipcode_to_test))


    print("nrdmWs.getStateLevelCount(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), state_abbrev_to_test, nrdmWs.category['Cough/Cold'], False)")
    print(nrdmWs.getStateLevelCount(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), state_abbrev_to_test, nrdmWs.category['Cough/Cold'], False))

    print("nrdmWs.getCountyLevelCount(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.category['Cough/Cold'], False)")
    print(nrdmWs.getCountyLevelCount(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.category['Cough/Cold'], False))

    print("nrdmWs.getZipLevelCount(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), zipcode_to_test, nrdmWs.category['Cough/Cold'], False)")
    print(nrdmWs.getZipLevelCount(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), zipcode_to_test, nrdmWs.category['Cough/Cold'], False))


    print("nrdmWs.getCountMultiRegions(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), zipcodes_to_test, nrdmWs.region_type['zipcode'], nrdmWs.category['Cough/Cold'], False)")
    print(nrdmWs.getCountMultiRegions(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), zipcodes_to_test, nrdmWs.region_type['zipcode'], nrdmWs.category['Cough/Cold'], False))

    print("nrdmWs.getCountMultiRegions(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), counties_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold'], False)")
    print(nrdmWs.getCountMultiRegions(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), counties_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold'], False))

    print("nrdmWs.getCountMultiRegions(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), states_to_test, nrdmWs.region_type['state'], str(nrdmWs.category['Cough/Cold']) + ',' + str(nrdmWs.category['Thermometer adult']), False)")
    print(nrdmWs.getCountMultiRegions(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), states_to_test, nrdmWs.region_type['state'], str(nrdmWs.category['Cough/Cold']) + ',' + str(nrdmWs.category['Thermometer adult']), False))


    print("nrdmWs.getZipcodeSeries(datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold'], 'N')")
    print(nrdmWs.getZipcodeSeries(datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold'], 'N'))

    print("nrdmWs.getZipcodeSeries(datetime.date(2020, 3, 1), state_abbrev_to_test, nrdmWs.region_type['state'], nrdmWs.category['Cough/Cold'], 'N')")
    print(nrdmWs.getZipcodeSeries(datetime.date(2020, 3, 1), state_abbrev_to_test, nrdmWs.region_type['state'], nrdmWs.category['Cough/Cold'], 'N'))



    print("nrdmWs.getAlgorithmOutput(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold'])")
    print(nrdmWs.getAlgorithmOutput(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold']))

    print("nrdmWs.getAlgorithmOutput(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), county_fips_to_test, nrdmWs.region_type['county'], nrdmWs.category['Cough/Cold'])")
    print(nrdmWs.getAlgorithmOutput(datetime.date(2020, 3, 1), datetime.date(2020, 3, 1), zipcode_to_test, nrdmWs.region_type['zipcode'], nrdmWs.category['Cough/Cold']))



if __name__ == '__main__':
    main()
