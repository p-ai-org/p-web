import pandas as pd

#read in data from csv file
df = pd.read_csv("majestic_million.csv")

#just get domain for now
domains = df["Domain"]

#write domains to text file
domains.to_csv("majestic_million.txt",sep = " ", index = False, header = False)

#shorter version with 10000 domains
domains_10000 = domains[0:10000]

#write to text as well
domains_10000.to_csv("10000websites.txt", sep = " ", index = False, header = False)