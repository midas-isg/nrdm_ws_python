import sys
import datetime
from zeep import Client
from zeep.wsse.username import UsernameToken


# NRDM WebService Python Client API
# Utilizes NRDM SOAP Webservice
# Jeremy Espino MD 2020/03/25
# juest4@pitt.edu


class NrdmWs:
    username = ""
    password = ""
    endpoint = "https://services.rods.pitt.edu/nrdm-ws-2.2-SNAPSHOT/NRDMService?wsdl"
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

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = None
        self.initClient()

    def initClient(self):
        self.client = Client(self.endpoint, wsse=UsernameToken(self.username, self.password))

    def isAlive(self):
        return self.client.service.isAlive()

    def getStateLevelCompletion(self, state):
        return self.client.service.getStateLevelCompletion(state)

    def getSpatialSeriesByRangeAndRegionType(self, start, end, category, region_type, region, region_return_type, normalize):
        return self.client.service.getSpatialSeriesByRangeAndRegionType(start,
                                                                        end,
                                                                        region_type,
                                                                        region,
                                                                        region_return_type,
                                                                        category,
                                                                        self.username,
                                                                        normalize)


def main():
    username = sys.argv[1]
    password = sys.argv[2]
    nrdmWs = NrdmWs(username, password)
    print(nrdmWs.isAlive())
    print(nrdmWs.getStateLevelCompletion("PA"))
    print(nrdmWs.getSpatialSeriesByRangeAndRegionType(datetime.date(2020,3,1),
                                                      datetime.date(2020,3,2),
                                                      nrdmWs.category['Cough/Cold'],
                                                      nrdmWs.region_type['state'],
                                                      "PA",
                                                      nrdmWs.region_type['county'],
                                                      False))


if __name__ == '__main__':
    main()
