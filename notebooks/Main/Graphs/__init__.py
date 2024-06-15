import matplotlib.pyplot as plt
import pandas as pd


def createAndShowGraphMonthlyIncidents(dataFrame):
    plt.style.use('cyberpunk')
    plt.figure(figsize=(10, 6))
    dataFrame['cmplnt_fr_dt'] = pd.to_datetime(dataFrame['cmplnt_fr_dt'])
    monthly_activity = dataFrame['cmplnt_fr_dt'].dt.month.value_counts().sort_index()
    monthly_activity.plot(kind='bar')
    plt.xlabel('Month')
    plt.ylabel('Number of Incidents')
    plt.title('Monthly Activity')
    plt.show()


def createAndShowGraphHourlyIncidents(dataFrame):
    plt.style.use('cyberpunk')
    plt.figure(figsize=(10, 6))
    dataFrame['cmplnt_fr_tm'] = pd.to_datetime(dataFrame['cmplnt_fr_tm'])
    hourly_activity = dataFrame['cmplnt_fr_tm'].dt.hour.value_counts().sort_index()
    hourly_activity.plot(kind='bar')
    plt.xlabel('Hour')
    plt.ylabel('Number of Incidents')
    plt.title('Hourly Activity')
    plt.show()


def createAndShowGraphRacialIncidents(dataFrame):
    plt.style.use('cyberpunk')
    plt.figure(figsize=(10, 6))
    race_activity = dataFrame['susp_race'].value_counts()
    race_activity.plot(kind='bar')
    plt.xlabel('Race')
    plt.ylabel('Number of Incidents')
    plt.title('Activity by Race')
    plt.show()


def firstHistory(dataFrame):
    pass


def secondHistory(dataFrame):
    pass
