# Makefile for AI Schema Filler Project

.PHONY: install run-backend run-frontend lint test clean

# Install dependencies
install:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Run the backend Flask server
run-backend:
	@echo "Running the Flask backend..."
	cd backend && python app.py

# Run the frontend interface
run-frontend:
	@echo "Running the frontend interface..."
	python run_gradio.py

# Lint the Python code
lint:
	@echo "Linting the code with flake8..."
	flake8 backend/ frontend/

# Run tests
test:
	@echo "Running tests..."
	pytest tests/

# Clean up .pyc files and __pycache__
clean:
	@echo "Cleaning up..."
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete