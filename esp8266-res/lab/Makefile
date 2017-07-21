AMPY=ampy
SERIAL=/dev/ttyUSB0

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
	    $(AMPY) -p $(SERIAL) put $$f ;\
	done;


clean: $(MPYFILES)
	$(AMPY) -p $(SERIAL) rm config.json
	for f in $^ ; \
	do \
	    echo delete $$f ;\
	    $(AMPY) -p $(SERIAL) rm $$f ;\
	done;


ls:
	$(AMPY) -p $(SERIAL) ls

login:
	picocom -b 115200 $(SERIAL)