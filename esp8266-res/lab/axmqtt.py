from umqtt.robust import MQTTClient
#from umqtt.simple import MQTTClient
import ubinascii
import machine

class MqttClient(object):
    """docstring for MqttClient"""
    config = None
    mqtt = None
    CLIENT_ID = ubinascii.hexlify(machine.unique_id())

    def __init__(self, conf):
        super(MqttClient, self).__init__()
        self.config = conf 

    def connect(self):
        self.mqtt = MQTTClient( self.CLIENT_ID , self.config["broker"] , port=self.config["brkport"])
        self.mqtt.set_callback(self.callback)

    def subscribe(self, channel):
        if not self.mqtt.connect(clean_session=False):
            self.mqtt.subscribe( channel )

    def tick(self,t):
        self.mqtt.check_msg()

    def callback(self,topic,msg):
        print( (topic,msg) )
