#Caleb Stickler
#Date

import os
import sys

sqlFile = sys.argv[1]

def main():
  filePath = os.getcwd() + sqlFile
  sqlCmd = open(filePath, 'r')
  
  for line in sqlCmd:
    cmd = sqlCmd.readline(line)
    parsedCmd = cmd.split(" ")
    
    if(parsedCmd[0][0] == "-"): #SQL comment
       break
    if(parsedCmd[0].upper() == ".EXIT): 
       print("All done")
    if(parsedCmd[0].upper() == "CREATE"):
       #DATABASE
       #TABLE
    if(parsedCmd[0].upper() == "DROP"):
       #DATABASE
       #TABLE
    if(parsedCmd[0].upper() == "USE"):
       #open database dir
    if(parsedCmd[0].upper() == "SELECT"):
       #*
    if(parsedCmd[0].upper() == "ALTER"):
       
  
  
  sqlCmd.close()
       
if __name__=="__main__":
  main()
