PROJECTNAME = project-guest-list
PYTHON := python3

############## FUNCTION DEFINES ##############
define run
	$(PYTHON) guestListApp.py
endef

define clean
	rm -rf __pycache__
	rm -rf ./recordings/*
endef

define depends
	sudo apt install libportaudio2 libportaudiocpp0 portaudio19-dev
	pip3 install PyAudio
	pip3 install pydub
endef

############## MAKE COMMANDS ##############

PHONY: clean
clean:
	$(call clean)

PHONY: run
run: 
	$(call run)

PHONY: depends
depends:
	$(call depends)