from http.server import BaseHTTPRequestHandler, HTTPServer
import math
from multiprocessing import Process
from klein import run, route
import sys
import time
from subprocess import PIPE, Popen
import os
import json
import requests
import logging
import threading
import warnings
import time
import smtplib

import urllib3,pymongo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Krypto"]
alert_col=mydb["alert"]


        
fromadd='krypto@gmail.com' 
toadd='nandhini@gmail.com' 
password='Krytpo@123'

warnings.filterwarnings("ignore")


def createalert(request):
    try:
        # Get default audio device using PyCAW
        trigger_price = requests.form['price']
        current_price=0
        while(trigger_price<= coin_price):  
            price_api="https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
            data=requests.get(price_api)
            json_data=data.json()
            Btc=json_data[0]
            coin_name=Btc["name"]
            coin_price=Btc["current_price"]
            time.sleep(5)
        krypto_server=smtplib.SMTP("krypto.gmail.com",8080)
        krypto_server.ehlo() 
        krypto_server.starttls() 
        krypto_server.ehlo() 
        krypto_server.login(fromadd,password) 
        msg_to_be_sent ="Current Price for " +coin_name+" is "+coin_price+" Please Hurry to Buy :)"
        krypto_server.sendmail(sender_add,receiver_add,msg_to_be_sent)
        krypto_server.quit()
        alert_data = {"coin_name":coin_name,"coin_price":coin_price}
        x = alert_col.insert_one(alert_data)
        
        return redirect(url_for('success',msg = "Aleat Created"))

    except Exception as e:
        print(e)

def getall():
    try:
        
        all_alert_data = alert_col.find()
        li = list(cursor)
        return li
        
        

    except Exception as e:
        print(e)
        


def delete_alert(request):
    try:
        delete_query = requests.form['deletequery']
        alert_col.delete_one(myquery)
        return redirect(url_for('success',msg = "Aleat Deleted"))

        
        

    except Exception as e:
        print(e)

class server_module(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    @route('/success/<msg>')
    def success(msg):
        return '%s' % msg
        
        
    @route('/alerts/create', methods=['POST'])
    def get_price_from_user(request):
        createalert(request)
        
    
    @route('/alerts/delete', methods=['POST'])
    def get_delete_from_user(request):
        delete_alert(request)
        
             
    @route('/getall', methods=['GET'])
    def getaudio(request):
        data=getall()
        return data



        


if __name__ == '__main__':
    run('', 80)
    





