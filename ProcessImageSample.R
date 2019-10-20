library(dplyr)
library(plyr)

i<-0

#load all file names in "datasets"
for (file in list.files("datasets")){
  
  #load each as a dataframe
  df_new<-data.frame(read.table(paste("datasets/",file,sep=""), skip = 4, sep = " "))
  
  #Remove empty columns (most are double-space separated, but sep only takes 1-byte separators) and cells labels
  if (ncol(df_new)==5) {
    df_new<-select(df_new,c(V2,V3,V4,V5))
  } else {  
    df_new<-select(df_new,c(V3,V5,V7,V9))
  }
  
  #Rename
  colnames(df_new) <- c("ice","pond","owtr","water")
  
  #Add Date
  df_new$date<-as.Date(substr(file,regexpr("_",b)[1]+1,regexpr("_",b)[1]+9),format = "%Y%b%d")
  
  #Add Location
  df_new$site<-substr(file,1,regexpr("_",b)[1]-1)
  df_new<-select(df_new,c("site","date","ice","pond","owtr","water"))
  
  #Start dataset or append to existing
  if (i==0) {
    df<-df_new
  } else {
    df<-rbind(df,df_new)
  }
  i<-i+1
  print(paste(df_new$site[1],i))
}

#Remove missing values
df[df==9.99]<-NA
df$match<-paste(df$site,df$date)

#Create summary file
df.summary<-ddply(df, c("site","date"), summarise,
      "Ice" = mean(ice, na.rm=TRUE),
      "Pond" = mean(pond, na.rm=TRUE),
      "Open Water" = mean(owtr, na.rm=TRUE),
      "All Water" = mean(water, na.rm=TRUE)
      )
df.summary