import os
import sqlite3
import re

def FindPath():
        User_profile = os.environ.get("USERPROFILE")
        History_path = User_profile + r"\\AppData\Local\Google\Chrome\User Data\Default\History"
        return History_path

def SaveHistoryToTxt():
        User_profile = os.environ.get("USERPROFILE")
        with open(User_profile + r"\\Desktop\history.txt","w") as f:
                f.write(str(result))
        f.close()
        
def Main():
        #List from the History database of chrome
        data_base = FindPath()          
        con = sqlite3.connect(data_base) 
        c = con.cursor()
        c.execute("SELECT urls.url FROM urls ORDER BY id DESC LIMIT 20") #I get last 20 items of the History
        result=c.fetchall()
        #List from the History database of chrome
        
        print(*result, sep = "\n")

        #converting the result to a string
        for i in result:
                resultString=''.join(str(result))

        #regex = re.compile("www.*")
        #newList = list(filter(regex.match,resultString))

        #how many times the user visited facebook links 
        timesVisitedFacebook = re.findall('facebook', resultString)
        print("The user visited facebook "+str(len(timesVisitedFacebook))+" times")

        
if __name__ == '__main__':
    Main()
