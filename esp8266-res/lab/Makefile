AMPY=ampy

MPYFILES := \
	boot.py \
	axadc.py \
	axapp.py \
	axconfbox.py \
	axgpio.py \
	axmqtt.py \
	axpwm.py \
	main.py \


install: $(MPYFILES) 
	for f in $^ ; \
	do \
	    echo installing $$f ;\
	    $(AMPY) -p /dev/ttyUSB0 put $$f ;\
	done;


clean: $(MPYFILES)
	$(AMPY) -p /dev/ttyUSB0 rm config.json
	for f in $^ ; \
	do \
	    echo delete $$f ;\
	    $(AMPY) -p /dev/ttyUSB0 rm $$f ;\
	done;


ls:
	$(AMPY) -p /dev/ttyUSB0 ls

login:
	picocom -b 115200 /dev/ttyUSB0