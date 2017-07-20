from umqtt.robust import MQTTClient
#from umqtt.simple import MQTTClient
import ubinascii
import machine
import time

class MqttClient(object):
    """docstring for MqttClient"""
    t1 = None
    t2 = None
    config = None
    mqtt = None
    CLIENT_ID = ""
    
    def __init__(self, conf):
        super(MqttClient, self).__init__()
        self.config = conf 
        self.CLIENT_ID = conf["device"]
        self.t1 = time.time()

    def connect(self):
        self.mqtt = MQTTClient( self.CLIENT_ID , self.config["broker"] , port=self.config["brkport"] , user=self.config["brkuser"],password=self.config["brkpasswd"])
        self.mqtt.set_callback(self.callback)

    def subscribe(self, channel):
        if not self.mqtt.connect(clean_session=False):
            self.mqtt.subscribe( channel )

    def tick(self,t):
        self.mqtt.check_msg()

        self.t2 = time.time()
        timediff = self.t2 - self.t1
        if timediff > self.config["durationpub"] :
            self.subscribe( bytes(self.config["topic"], 'utf-8') )
            self.t1 = self.t2 


    def callback(self,topic,msg):
        print( (topic,msg) )
