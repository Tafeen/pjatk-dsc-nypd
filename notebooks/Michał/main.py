from DataPreparation import *


def LoadDataFromAPI():
    APIKey = 'b6g8ahp9cur6ukfvc9ebax0tn'
    APISecret = '4r06v9zy295iz4fujr2hfprjfotyx113uye1i55x8yddjgkin2'
    URL = 'https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=200000'

    Json = getJson(URL=URL, APIKey=APIKey, APISecret=APISecret)
    dataFrame = getDataFrame(Json=Json)
    saveToCSV(dataFrame=dataFrame)


if __name__ == '__main__':
    # LoadDataFromAPI()
    dataFrame = loadFromCSV('data.csv')
    print(dataFrame.shape)
    countUniqueRecords(dataFrame=dataFrame, column='ofns_desc')
    getUniqueRecordsWithCount(dataFrame=dataFrame, column='ofns_desc')
