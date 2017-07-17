import machine
class Pwm:
    def __init__(self):
        pass
    
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
        return {"action":"get" , "data": req }

    def post(self, req):
        xpin = int( req["context"][1] )
        xfreq = int( req["context"][2] )
        xduty = int( req["context"][3] )
        pwm = machine.PWM(machine.Pin(2), freq=xfreq, duty=xduty)

        return {"action":"post", "data": req}

    def put(self, req):
        return {"action":"put", "data": req}

    def delete(self, req):
        return {"action":"delete", "data": req}
