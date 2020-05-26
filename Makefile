.PHONY: help run test install

default: help

help: ## Show this help
	@echo "RPG Content Generator"
	@echo "======================"
	@echo
	@echo "By Robin Rainwalker circa 2020"
	@echo
	@fgrep -h " ## " $(MAKEFILE_LIST) | fgrep -v fgrep | sed -Ee 's/([a-z.]*):[^#]*##(.*)/\1##\2/' | column -t -s "##"

install: ## Install the app's dependencies
				pip3 install -r requirements.txt

run: ## Run app locally
				python3 main.py

test: ## Run app's tests
				pytest