# StyleLoop HK Backend

This backend module provides weather-based clothing suggestions for the StyleLoop HK app.

## Files

- `main.py`: Entry point script that fetches weather data and prints clothing suggestions.
- `weather.py`: Module for fetching current weather data from Hong Kong Observatory API.
- `suggestions.py`: Module for generating clothing category suggestions based on temperature and humidity.
- `requirements.txt`: Python dependencies.

## Development Environment Setup

To set up the development environment for the Python backend:

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps
1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/Yanny1026/StyleLoop-HK.git
   cd StyleLoop-HK/backend
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Verify installation**:
   ```bash
   python main.py
   ```
   This should fetch weather data and display clothing suggestions.

### Development Tips
- Use a code editor like VS Code with Python extensions for better development experience.
- For testing, you can modify the weather data or suggestions logic in the respective modules.
- Ensure you have internet access for the weather API calls.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the script: `python main.py`

The script will fetch current weather data and suggest appropriate clothing categories.

## API

The weather data is sourced from the Hong Kong Observatory's open data API: https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en