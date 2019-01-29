import os
import sqlite3

def FindPath():
        User_profile = os.environ.get("USERPROFILE")
        History_path = User_profile + r"\\AppData\Local\Google\Chrome\User Data\Default\History"
        return History_path

def Main():
        data_base = FindPath()          
        con = sqlite3.connect(data_base) 
        c = con.cursor()
        result=c.execute("SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;") 
        User_profile = os.environ.get("USERPROFILE")
        result=c.fetchall()
        with open(User_profile + r"\\Desktop\history.txt","w") as f:
                f.write(str(result))
        f.close()
        
if __name__ == '__main__':
    Main()
