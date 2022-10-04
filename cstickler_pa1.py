#Caleb Stickler
#Date

import os
import sys

if(sys.argv[1] != NULL):
  sqlFile = sys.argv[1]

def main():
  filePath = os.getcwd() + sqlFile
  sqlCmd = open(filePath, 'r')
  
  os.system("cd /")
  os.system("mkdir CS457_As1")
  
  for line in sqlCmd:
    cmd = sqlCmd.readline(line)
    parsedCmd = cmd.split(" ")
    
    if(parsedCmd[0].upper() == ".EXIT"): 
       print("All done")
    elif(parsedCmd[0].upper() == "CREATE"):
       if(parsedCmd[1].upper() == "DATABASE"):
          dbName = parsedCmd[2]
          dbName = dbName[:-1]
          os.system("cd ~")
          try:
            os.system("mkdir " + dbName)
          except FileExistsError:
            print("!Failed to create database " + dbName + " because it already exists.")
            break
          finally:
            print("Database " + dbName + " created.")
       elif(parsedCmd[1].upper() == "TABLE"):
          tbName = parsedCmd[2]
          tbMetadata = ""
          for i in parsedCmd:
            if (i < 3):
              pass
            else:
              tbMetadata += parsedCmd[i]
          
          tbMetadata = tbMetadata[:-1]
          tbMetadata = tbMetadata[:-1]
          tbMetadata = tbMetadata[1:]
          tbMetadata.replace(",", " |")
          
          try:
            os.system("echo " + tbMetadata + " > " + tbName + ".txt")
          except FileExistsError:
            print("!Failed to create table " + tbName + " because it already exists.")
          else:
            print("Table " + tbName + " created.") 
    elif(parsedCmd[0].upper() == "DROP"):
       if(parsedCmd[1].upper() == "DATABASE"):
          os.system("cd ~")
          dbName = parsedCmd[2]
          try:
            os.system("rm -r " + dbName) #delete non-empty directory
          except FileExistsError:
            print("!Failed to delete " + dbName + " because it does not exist.")
            break
          except:
            os.system("rm -d " + dbName) #delete empty directory
            break
          else:
            print("Database " + dbName + "deleted.")
       elif(parsedCmd[1].upper() == "TABLE"):
          tbName = parsedCmd[2]
          try:
            tbFilePath = os.system("readlink -f " + tbName + ".txt")
          except FileExistsError:
            print("!Failed to delete " + tbName + " because it does not exist.")
          else:
            parentFilePath = tbFilePath.rstrip("/" + tbName + ".txt")
            os.system("cd " + parentFilePath)
            os.system("rm " + tbName + ".txt")
    elif(parsedCmd[0].upper() == "USE"):
       dbName = parsedCmd[1]
       dbName = dbName[:-1]
      
       try:
          dbFilePath = os.system("readlink -f " + dbName)
       except FileExistsError:
          print("!Failed to use " + dbName + "because it does not exist.")
       else:
          os.system("cd " + dbFilePath)
          print("Using database " + dbName)
    elif(parsedCmd[0].upper() == "SELECT"):
       if(parsedCmd[1] == "*":
          tbName = parsedCmd[3]
          
          try:
             selectedTbl = open(tbName + ".txt", "r")
          except FileExistsError:
             print("!Failed to query table " + tbName + " because it does not exist.")
          else:
             selectedTbl.readlines()
    elif(parsedCmd[0].upper() == "ALTER"):
       #TABLE
          #tbName
            #ADD
    elif (parsedCmd[0][0] == "-"): #SQL comment
       pass
       
  
  
  sqlCmd.close()
       
if __name__=="__main__":
  main()
