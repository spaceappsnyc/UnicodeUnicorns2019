#The analyzer
import pandas as pd
import numpy
import datetime

from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


beau_df_meteo = pd.read_csv("dataset/beaufort99-01.csv", ';')
cacana_df_meteo = pd.read_csv("dataset/cacana99-01.csv",";")
cafram_df_meteo = pd.read_csv("dataset/cafram99-01.csv",";")
esiber_df_meteo = pd.read_csv("dataset/esiber99-01.csv",";")


beau_df_meteo.validdate = beau_df_meteo.validdate.str.slice(stop=10)

cacana_df_meteo.validdate = cacana_df_meteo.validdate.str.slice(stop=10)


cafram_df_meteo.validdate = cafram_df_meteo.validdate.str.slice(stop=10)
esiber_df_meteo.validdate = esiber_df_meteo.validdate.str.slice(stop=10)




df2 = pd.read_csv("dataset/ImageSummariesOriginal.csv")

beaufoDFocean = df2[df2.site == 'beaufo']
cacanaDFocean = df2[df2.site == 'cacana']
caframDFocean = df2[df2.site == 'cafram']
esiberDFocean = df2[df2.site == 'esiber']

dfBeaufortFinal = beau_df_meteo.set_index('validdate').join(beaufoDFocean.set_index('date'))
dfCacanaFinal = cacana_df_meteo.set_index('validdate').join(cacanaDFocean.set_index('date'))
dfCaframFinal = cafram_df_meteo.set_index('validdate').join(caframDFocean.set_index('date'))
dfEsiberFinal = esiber_df_meteo.set_index('validdate').join(esiberDFocean.set_index('date'))

dfUltimate = dfBeaufortFinal.append(dfCacanaFinal.append(dfCaframFinal.append(dfEsiberFinal)))

dfUltimate = dfUltimate.drop(columns=["All Water","Open Water","Ice","site","Unnamed: 0"])
dfUltimate = dfUltimate.dropna()
print(dfUltimate)

abetterdf = pd.read_csv("dataset/Matched Data.csv")
abetterdf = abetterdf.drop(columns=["Unnamed: 0", "site", "date","Ice", "Pond", "wind","temp","hum","rad","agg_thirty_hum","agg_thirty_rad","agg_thirty_wind","agg_thirty_temp"])
print(abetterdf.head(20))

values = abetterdf.values
X = values[:, [0,1,2,3,5]]
y = values[:,4]



print("Linear reg:")
reg = LinearRegression().fit(X, y)
print(reg.score(X, y))
print(reg.coef_)
print(reg.intercept_)

