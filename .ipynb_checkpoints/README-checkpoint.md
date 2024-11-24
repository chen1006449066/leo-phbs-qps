# leo-phbs-qps
qps course
# Get CPI Data and Calculate Inflation

This project includes a script and notebook that fetch US Consumer Price Index (CPI) data from FRED (Federal Reserve Economic Data), save it to a CSV file, and calculate the last 4 quarters' inflation rates.

---

## Repository Structure

- `src/`: Contains helper modules for saving and reading data.
  - `storage.py`: Handles saving and loading data to/from CSV files.
- `scripts/`: Contains the Jupyter Notebook for the project
  - `get_CPI.ipynb`: Fetches CPI data, saves it, and calculates inflation rates.

---

## Requirements

To run this project, you need Python 3.7 or higher and the following packages:

- `pandas`
- `pandas-datareader`

---

## Setup Instructions

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/chen1006449066/leo-phbs-qps.git
```
### Step 2: Run the 'get_CPI.ipynb'
Open 'get_CPI.ipynb' it will fetch CPI data and save it to a CSV file, and calculate the last 4 quarters' inflation rates.