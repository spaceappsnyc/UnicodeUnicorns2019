beaufo<-read_csv2("~/Repo/Space Apps 2019/dataset/beaufort99-01.csv")
beaufo$site<-"beaufo"
cacana<-read_csv2("~/Repo/Space Apps 2019/dataset/cacana99-01.csv")
cacana$site<-"cacana"
cafram<-read_csv2("~/Repo/Space Apps 2019/dataset/cafram99-01.csv")
cafram$site<-"cafram"
esiber<-read_csv2("~/Repo/Space Apps 2019/dataset/esiber99-01.csv")
esiber$site<-"esiber"

data.weather<-rbind(beaufo,cacana,cafram,esiber)
colnames(data.weather)<-c("date","temp","wind","hum","rad","site")

data.weather$date<-as.Date(data.weather$date)
data.weather$temp<-as.numeric(data.weather$temp)
data.weather$wind<-as.numeric(data.weather$wind)
data.weather$rad<-as.numeric(data.weather$rad)
data.weather<-select(data.weather,c(site,date,temp,wind,hum,rad))

data.weather$agg_seven_temp<-NA
data.weather$agg_seven_rad<-NA
data.weather$agg_seven_hum<-NA
data.weather$agg_seven_rad<-NA
for (j in 0:3){
  for (i in (7+j*1089):(1089+j*1089)){
    data.weather$agg_seven_temp[i]<-mean(data.weather$temp[(i-6):i])
    data.weather$agg_seven_wind[i]<-mean(data.weather$wind[(i-6):i])
    data.weather$agg_seven_hum[i]<-mean(data.weather$hum[(i-6):i])
    data.weather$agg_seven_rad[i]<-sum(data.weather$rad[(i-6):i])
  }
}

data.weather$agg_thirty_temp<-NA
data.weather$agg_thirty_wind<-NA
data.weather$agg_thirty_hum<-NA
data.weather$agg_thirty_rad<-NA
for (j in 0:3){
  for (i in (30+j*1089):(1089+j*1089)){
    data.weather$agg_thirty_temp[i]<-mean(data.weather$temp[(i-29):i])
    data.weather$agg_thirty_wind[i]<-mean(data.weather$wind[(i-29):i])
    data.weather$agg_thirty_rad[i]<-sum(data.weather$rad[(i-29):i])
    data.weather$agg_thirty_hum[i]<-mean(data.weather$hum[(i-29):i])
  }
}


data.weather$match<-paste(data.weather$site,data.weather$date)

data.match.all<-select(merge(melt.good,data.weather,by = "match", all = TRUE),c("site.y","date.y","temp","wind","hum","rad","agg_seven_temp","agg_seven_wind","agg_seven_hum","agg_seven_rad","agg_thirty_temp","agg_thirty_wind","agg_thirty_hum","agg_thirty_rad","Ice","Pond","Open Water","All Water"))
colnames(data.match.all)[1]<-"site"
colnames(data.match.all)[2]<-"date"
data.match<-select(merge(melt.good,data.weather,by = "match", all.x = TRUE),c("site.y","date.y","temp","wind","hum","rad","agg_seven_temp","agg_seven_wind","agg_seven_hum","agg_seven_rad","agg_thirty_temp","agg_thirty_wind","agg_thirty_hum","agg_thirty_rad","Ice","Pond","Open Water","All Water"))
colnames(data.match)[1]<-"site"
colnames(data.match)[2]<-"date"

