# MicroPython Web Project

MicroWeb Project is tiny web control 

## Show
![image](https://)

## Installation
```install
$sudo pip install esptool
$sudo pip install adafruit-ampy
$wget https://github.com/xhsiung/microweb/blob/master/esp8266-custom-0.0.1.bin
$esptool.py --port /dev/ttyUSB0 erase_flash
$esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-custom-0.0.1.bin

```

CONFIG
```config
{
    "webserver":"192.168.5.1",
    "webport": 88,
    "netmask": "255.255.255.0",
    "gateway":"0.0.0.0",
    "dns":"8.8.8.8",
    "broker":"xxx.xxx.xxx.xxx",
    "brkport": 1883,
    "topic":"/api/json/data",
    "apssid":"ESPAX",
    "appasswd":"12345678",
    "stassid":"xxx",
    "stapasswd":xxx"",
    "ticktime": 500
}
```

## Usage

get config
```info
http://192.168.5.1/api/conf/get

```

set config 
```
http://192.168.5.1/api/conf/post?broker=x.x.x.x&brkport=1884&topic=xxxxx

```


reset
```
http://192.168.5.1/api/reset
```

Sample
```
test
```

## Current status

Done  work:
* test

## History

* **v1.0.0** : 2017-07-27
