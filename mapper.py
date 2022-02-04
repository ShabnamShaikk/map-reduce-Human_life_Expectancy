from re import A
import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 12) : 
    unit_id,golden,unit_state,trusted_judgments,last_judgment_at,choose_one,choose_one_confidence,choose_one_gold,keyword,location,text,tweetid,userid = datalist
    # print intermediate key-value pairs to standard output
  print(golden,"\t",1)