import os
import machine

import uhttpd
import http_file_handler
import http_api_handler
import urequests as requests

import axapp
import axconfbox
import axgpio
import axmqtt

# import usocket as socket

class WebServer(object):
    """docstring for WebServer"""
    config = None
    server = None
    webroot = "/www"
    confbox = None 
    app = None
    gpio = None
    mqcli = None

    def __init__(self):
        super(WebServer, self).__init__()

        if not http_file_handler.exists( self.webroot):
            os.mkdir( self.webroot)
        
        self.initApp()
        self.initMqtt()

        self.confbox = axconfbox.Confbox(self.app, axapp.CONFIG )
        self.gpio = axgpio.Gpio()

        #www
        webhandler = http_file_handler.Handler( self.webroot )
        #api
        api_handler = http_api_handler.Handler([ (['gpio'], self.gpio) , 
                                                 (['conf'], self.confbox)
                                              ])
        self.server = uhttpd.Server([('/web', webhandler),('/api', api_handler)] , config={'port': self.config["webport"]}) 

    def initApp(self):
        self.app = axapp.App()
        self.config = self.app.getConf()
        self.app.apifConncet()
        self.app.staifConnect()


    def initMqtt(self):
        self.mqcli = axmqtt.MqttClient( self.config )
        self.mqcli.connect()
        self.mqcli.subscribe( bytes(self.config["topic"], 'utf-8') )

        try:
            tim = machine.Timer(-1)
            tim.init(period=200, mode=machine.Timer.PERIODIC, callback=self.mqcli.tick)

        except Exception as e:
            print("Connect Error")
            raise e
       

    def run(self):
        print("http start")
        self.server.run()


def main():
    web = WebServer() 
    web.run()

main()
