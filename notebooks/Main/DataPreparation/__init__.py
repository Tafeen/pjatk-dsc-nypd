import sys
import pandas as pd
import requests
from requests.auth import HTTPBasicAuth


def getJson(URL, APIKey, APISecret):
    response = requests.get(URL, auth=HTTPBasicAuth(APIKey, APISecret))
    if response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
        sys.exit(1)
    return response.json()


def getDataFrame(Json):
    df = pd.DataFrame(Json)
    columnsToRemove = ['cmplnt_num', 'addr_pct_cd', 'ky_cd', 'crm_atpt_cptd_cd', 'loc_of_occur_desc',
                       'juris_desc', 'jurisdiction_code', 'hadevelopt', 'housing_psa', 'x_coord_cd', 'y_coord_cd',
                       'lat_lon', 'patrol_boro', 'station_name', 'vic_age_group', 'vic_race', 'vic_sex',
                       ':@computed_region_efsh_h5xi', ':@computed_region_f5dn_yrer',
                       ':@computed_region_yeji_bk3q', ':@computed_region_92fq_4b7q',
                       ':@computed_region_sbqj_enih', 'transit_district']

    df.drop(columns=columnsToRemove, inplace=True, errors='ignore')
    return df


def countUniqueRecords(dataFrame, column):
    uniques = dataFrame[column].nunique()
    print(f"There are {uniques} unique records in the column '{column}'")


def getUniqueRecordsWithCount(dataFrame, column):
    pd.set_option('display.max_rows', None)  # None means unlimited
    pd.set_option('display.max_columns', None)  # None means unlimited
    uniques = dataFrame[column].value_counts()
    print("Unique records in column '{}', with counts:".format(column))
    print(uniques)


def getDataFrameWithSelectedColumns(dataFrame, columns: list):
    return dataFrame[columns]


def saveToCSV(dataFrame):
    dataFrame.to_csv('data.csv', index=False)


def loadFromCSV(pathName):
    dataFrame = pd.read_csv(pathName)
    return dataFrame


def printInfo(dataFrame):
    print(dataFrame.shape)
