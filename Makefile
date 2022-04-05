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

############## MAKE COMMANDS ##############

PHONY: clean
clean:
	$(call clean)

PHONY: run
run: 
	$(call run)