from re import A
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 12) : 
    Country,Region,Happiness_Rank,Happiness_Score,Standard_Error,Economy,Family,Health,Freedom,Trust,Generosity,Dystopia_Residual = datalist
    # print intermediate key-value pairs to standard output
  print(Country,"\t",1)