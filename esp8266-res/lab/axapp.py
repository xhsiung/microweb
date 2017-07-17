import network
import ubinascii
import ujson as json

CONFIG ={
    "webserver":"192.168.5.1",
    "webport": 88,
    "netmask": "255.255.255.0",
    "gateway":"0.0.0.0",
    "dns":"8.8.8.8",
    "broker":"axsoho.com",
    "brkport": 1883,
    "topic":"/api/json/data",

    "apssid":"ESPAX",
    "appasswd":"12345678",
    "stassid":"AndroidAP557F",
    "stapasswd":"ayay2579",
    "ticktime": 500
}

class App(object):
    """docstring for App"""
    config = None
    apif = None
    staif = None

    def __init__(self):
        super(App, self).__init__()
        self.loadConfig()
        self.apif =  network.WLAN(network.AP_IF) 
        self.staif = network.WLAN(network.STA_IF)

    def loadConfig(self):
        try:
            with open("/config.json") as f:
                self.config = json.loads( f.read())
            print("loding config")
        except Exception as e:
            self.saveConfig( CONFIG )
            

    def saveConfig(self, conf ):
        try:
            with open("/config.json","w") as f:
                f.write(json.dumps(conf))
                self.config = conf
                f.close()

            print("saving config")
        except Exception as e: 
            print("can not save config")


    def apifConncet(self):
        print("apif connect")
        self.apif.active(True)
        self.apif.config(essid=self.config['apssid'])
        self.apif.config(password=self.config['appasswd']) 
        self.apif.ifconfig( ( self.config["webserver"], self.config["netmask"], self.config["gateway"], self.config["dns"] ) )


    def staifConnect(self):
        print("staif connect")
        if not self.staif.isconnected():
            self.staif.active(False)
            self.staif.active(True)
            self.staif.connect( self.config['stassid'], self.config['stapasswd'])
            while not self.staif.isconnected():pass
            

    def getMac(self):
        apifmac = None
        staifmac = None
        if self.apif != None:
            apifmac = ubinascii.hexlify( self.apif.config('mac'),':').decode()
        if self.staif != None:
            staifmac = ubinascii.hexlify( self.staif.config('mac'),':').decode()
        print( (apifmac,staifmac) )

    def getConf(self):
        return self.config
