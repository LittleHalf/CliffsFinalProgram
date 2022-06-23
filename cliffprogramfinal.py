from os import name
import yahoo_fin.stock_info as si
from yahoo_fin import options

p = [152.84, 4796.56, 36585.06, 401.68, 225.32, 162.89, 89.43, 78.22, 57.22, 39.53, 175.52, 77.10, 78.22, 139.44, 210.31, 57.10, 373.67, 142.34, 47.50, 49.20, 34.79, 29.11, 41.00, 78.74, 120.67, 18.95] 

k = ["gme", "^gspc", "^dji", "qqq", "iwm", "rsp", "xlb", "xlc", "xle", "xlf", "xlk", "xlp", "xlu", "xlv", "xly", "ipo", "xlg", "iwc", "eqal", "eem", "prnt", "izrl", "arkf", "arkq", "arkw", "arkx"]

j = (p[0] - si.get_live_price(k[0]))/p[0]
lol = -j*100
dickt = si.get_quote_data(k[0]) 
extract = dickt.get("regularMarketChangePercent")
file1 = open("hi.txt","w")
file1.write(k[0])
file1.write("\n")
file1.write(str(round(lol, 2)))
file1.write(" %  YTD")
file1.write("\n")
file1.write(str(extract))
file1.write("% Daily")
file1.write("\n\n")
for i in range(1, 26):
    j = (p[i] - si.get_live_price(k[i]))/p[i]
    lol = -j*100
    dickt = si.get_quote_data(k[i]) 
    extract = dickt.get("regularMarketChangePercent")
    file1 = open("hi.txt","a")
    file1.write(k[i])
    file1.write("\n")
    file1.write(str(round(lol, 2)))
    file1.write(" %  YTD")
    file1.write("\n")
    file1.write(str(extract))
    file1.write("% Daily")
    file1.write("\n\n")
'''
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yahoo_fin.stock_info as si
from yahoo_fin import options

#hi cliff i hope u enjoy this crackhead code

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("apidemo3578-b74297b2f622.json", scope)

googleSheet = gspread.authorize(credentials)

index = 0 
ws = googleSheet.open("APITestSheet").get_worksheet(index)


p = [0, 152.84, 4796.56, 36585.06, 401.68, 225.32, 162.89, 89.43, 78.22, 57.22, 39.53, 175.52, 77.10, 78.22, 139.44, 210.31, 57.10, 373.67, 142.34, 47.50, 49.20, 34.79, 29.11, 41.00, 78.74, 120.67, 18.95] 

k = ["nothing", "gme", "^gspc", "^dji", "qqq", "iwm", "rsp", "xlb", "xlc", "xle", "xlf", "xlk", "xlp", "xlu", "xlv", "xly", "ipo", "xlg", "iwc", "eqal", "eem", "prnt", "izrl", "arkf", "arkq", "arkw", "arkx"]


for name in range(2, 27):
  ws.update_cell(name, 1, k[name])
  j = (p[name] - si.get_live_price(k[name]))/p[name]
  perytd = -j*100
  dickt = si.get_quote_data(k[name]) 
  perdai = dickt.get("regularMarketChangePercent")
  perdain = str(round(perdai, 2)) + "%"
  perytdn = str(round(perytd, 2)) + "%"
  ws.update_cell(name, 2, perytdn)
  ws.update_cell(name, 3, perdain)

print("look on the sheets (it updates in real time)")
'''