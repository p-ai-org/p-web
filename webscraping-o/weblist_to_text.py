import pandas as pd

#read in data from csv file
df = pd.read_csv("majestic_million.csv")

#just get domain for now
domains = df["Domain"]

#write domains to text file
domains.to_csv("majestic_million.txt",sep = " ", index = False, header = False)