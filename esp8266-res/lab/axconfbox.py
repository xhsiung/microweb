
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
        
class Confbox:
    CONFIG = None
    app = None

    def __init__(self, app , config):
        self.app = app 
        self.CONFIG = config
    
    def get(self, req):
        if req["context"][0] == "get":
            return self.gget( req )

        elif req["context"][0] == "post":
            return self.post( req )

        elif req["context"][0] == "put":
            return self.put( req )

        elif req["context"][0] == "delete":
            return self.delete( req )


    def gget(self, req):
        return {"action":"get","conf": self.app.getConf() }

    def post(self, req):
        params = req["query_params"]
        conf = self.app.getConf()
        if params != None:
            for key in params:
                if self.CONFIG.get( key ) == None:
                    continue  
                if key in ["webport","brkport","ticktime"]:
                    conf[ key ] = int(params[key])
                    continue
                conf[ key ] = params[key]
        
        self.app.saveConfig( conf )
        return {"action":"post", "conf": self.app.getConf() }

    def put(self, req):
        return {"action":"put", "data": req}

    def delete(self, req):
        return {"action":"delete"}

    def apply(self, req):
        self.app.apifConncet()
        self.app.staifConnect()
        return {"action":"apply" , "succes": True}

    def reset(self, req):
        self.app.saveConfig(CONFIG)
        machine.reset()
        return {"action":"reset" , "succes": True}