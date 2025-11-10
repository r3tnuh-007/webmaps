all:
	@clear
	@echo "Executing map.py..."
	@sleep 1.5s
	@clear
	@python3 map.py
	@echo "map.py execution complete."

dependencies:
	@echo "Installing dependencies..."
	@sleep 1s
	@pip install -r requirements.txt
	@clear
	@echo "Success: Dependencies installed."
	@sleep 2s
	@clear

clean:
	@echo "Cleaning up..."
	@sleep 1s
	@rm -rf map1.html
	@clear
	@echo "Cleanup complete."
	@sleep 1s
	@clear

re: clean all

.PHONY: all dependencies clean
