import machine
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
                if key in ["webport","brkport","ticktime","noapport"]:
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