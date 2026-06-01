# 📊 Women Financial Inclusion & Alternative Credit Scoring Dashboard

An interactive **Business Analytics Dashboard** built with Python and Streamlit to explore digital lending access, barriers, and financial inclusion metrics for women.

---

## 🌟 Project Overview
This project analyzes survey data to identify key trends in how women interact with digital banking and mobile loan applications. It highlights demographics, usage patterns, and the biggest barriers women face in the financial ecosystem.

## 🚀 Key Features
* **Live Metrics:** Real-time calculation of bank account ownership and mobile loan app usage.
* **Interactive Filters:** Filter data by **Area of Residence** (Urban, Semi-urban, Rural) to see localized insights.
* **Visual Data Exploration:**
    * **Bar Charts:** Visualize Age Demographics.
    * **Donut Charts:** Identify the biggest perceived barriers to credit.
* **Raw Data Access:** Toggle view to inspect the underlying survey responses directly.

---

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Framework:** [Streamlit](https://streamlit.io/)
* **Data Analysis:** Pandas
* **Visualization:** Plotly Express
* **Environment:** Python `venv` (Virtual Environment)

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
2. Set Up Virtual Environment (Recommended)
Bash
# Create venv
python -m venv venv

# Activate venv (Windows)
.\venv\Scripts\Activate.ps1

# Activate venv (Mac/Linux)
source venv/bin/activate
3. Install Dependencies
Bash
pip install -r requirements.txt
4. Data Preparation
Make sure your Excel file is in the root directory, then run the conversion script to generate data.csv:

Bash
python convert.py
5. Run the Dashboard
Bash
streamlit run app.py
📂 Project Structure
app.py: The main Streamlit dashboard application.

convert.py: Script to convert Excel survey data to CSV format.

requirements.txt: List of Python libraries needed.

data.csv: The cleaned data used by the app.

README.md: Documentation and project guide.

📊 Sample Insights
Demographics: Analyzes which age groups are most active in digital lending.

Barriers: Identifies lack of credit history and high interest rates as major hurdles.

Inclusion: Measures the gap between traditional banking and mobile wallet adoption.

🤝 Contributing
Contributions are welcome! If you have suggestions to improve the dashboard or additional data to add, feel free to Fork the repo and create a Pull Request.

📄 License
This project is open-source and available under the MIT License.
