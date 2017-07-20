import network
import ubinascii
import ujson as json

CONFIG ={
    "webserver":"192.168.4.2",
    "webport": 88,
    "netmask": "255.255.255.0",
    "gateway":"",
    "dns":"",

    "broker":"axsoho.com",
    "brkport": 1883,
    "brkuser":"",
    "brkpasswd":"",
    "noapport": 1880,
    "topic":"",
    "device":"",
    "durationpub": 600,

    "apssid":"ESPAX",
    "appasswd":"12345678",
    "stassid":"BAIS-16F",
    "stapasswd":"hjkl848484",
    "ticktime": 500
}

class App(object):
    """docstring for App"""
    config = None
    apif = None
    staif = None
    apifmac = None
    staifmac = None

    def __init__(self):
        super(App, self).__init__()
        self.apif =  network.WLAN(network.AP_IF) 
        self.staif = network.WLAN(network.STA_IF)
        self.loadConfig()

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
                if conf.get("brkuser") == "":
                    conf["brkuser"] = "xhsiung"
                if conf.get("brkpasswd") == "":
                    conf["brkpasswd"] = "@gmail.com"
                if conf.get("device") == "":
                    conf["device"] = self.getApifmac()
                if conf.get("topic") == "":
                    conf["topic"] = "/mqtt/"+self.getApifmac()

                f.write(json.dumps(conf))
                self.config = conf
                f.close()

            print("saving config")
        except Exception as e: 
            print("can not save config")


    def apifConncet(self):
        print("apif connect")
        self.apif.active(True)
        print( self.config['apssid']  )
        self.apif.config(essid=self.config['apssid'])
        self.apif.config(password=self.config['appasswd']) 
        self.apif.ifconfig( ( self.config["webserver"], self.config["netmask"], self.config["gateway"], self.config["dns"] ) )


    def staifConnect(self):
        print("staif connect")
        if not self.staif.isconnected():
            self.staif.active(True)
            self.staif.connect( self.config['stassid'], self.config['stapasswd'])
            while not self.staif.isconnected():pass
            

    def getApifmac(self):
        if self.apif != None:
            self.apifmac = ubinascii.hexlify( self.apif.config('mac'),':').decode()
        return self.apifmac.replace(":","")
        #if self.staif != None:
        #    staifmac = ubinascii.hexlify( self.staif.config('mac'),':').decode()
        #return (apifmac,staifmac)

    def getConf(self):
        return self.config
