# Motorcycle Sales Analysis

**Description:**  
This project focuses on analyzing motorcycle sales data to understand various factors influencing selling prices, ownership trends, and usage characteristics. The analysis aims to provide insights into how variables such as age, kilometers driven, seller type, and manufacturer affect the motorcycle market. An interactive dashboard built with **Streamlit** allows users to visualize these insights and engage dynamically with the data.

## Project Structure

- **/data/**:  
  Directory for storing data files used in the project.
  - **/data/raw/**: Contains original datasets that have not been processed.
  - **/data/processed/**: Holds cleaned and processed datasets ready for analysis.

- **/notebooks/**:  
  Jupyter notebooks containing exploratory data analysis (EDA) and model development.
  - Example notebook organization: `01_exploratory_analysis.ipynb`, `02_data_cleaning.ipynb`, etc.

- **/outputs/**:  
  Folder for saving results generated from analyses, including graphs and tables.

- **/scripts/**:  
  Optional directory for reusable Python scripts, such as functions for data cleaning and transformation.

- **/streamlit/**:  
  Contains the Streamlit application files for interactive data visualization.
  - **/streamlit/app.py**: Main file for the Streamlit application.
  - **/streamlit/components/**: Subdirectory for reusable components like charts or sidebars.
  - **/streamlit/pages/**: (Optional) If the application has multiple pages, they can be organized in this directory.

- **requirements.txt**:  
  A file listing the necessary dependencies for the project (Python libraries). This ensures that anyone can install the required libraries to run the project.

- **README.md**:  
  Documentation providing an overview of the project and instructions for use.

## Requirements

- **Python 3.x**
- Required libraries, listed in `requirements.txt`, include:
  - pandas
  - plotly
  - streamlit
  - openpyxl
  - XlsxWriter

### Installing Dependencies

To install the necessary dependencies, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Usage

1. **Place Your Data in the Correct Directory:**  
   Insert the raw data files into the `/data/raw/` folder. If you have any processed data, you can create a `/data/processed/` folder to organize them.

2. **Open Jupyter Notebooks for Exploration:**  
   Start JupyterLab with the command:
   ```bash
   jupyter lab
   ```
   Navigate to the `/notebooks/` folder and open the notebooks to perform analyses. Example notebooks include:
   - `01_exploratory_analysis.ipynb`: Initial exploration of the dataset, visualizations, and findings.
   - `02_data_cleaning.ipynb`: Data cleaning and preparation processes.
   - `03_modeling.ipynb`: (if applicable) Building and evaluating predictive models.

3. **Start the Streamlit Application:**  
   To launch the interactive Streamlit application and explore results through a web interface, execute:
   ```bash
   streamlit run streamlit/app.py
   ```
   If your application has multiple pages, you can navigate through them based on the organization in the `/streamlit/pages/` directory.

4. **Generate and View Results:**  
   As you run the notebooks or the Streamlit application, generated outputs such as charts and tables will be stored in the `/outputs/` folder for easy access later.

## Notebook Workflow

1. **Data Exploration:**  
   The exploratory analysis notebook inspects the data, performs basic cleaning, and provides initial insights into sales trends and factors affecting motorcycle prices.

2. **Modeling (if applicable):**  
   The modeling notebook trains and evaluates predictive models to analyze pricing based on various attributes.

3. **Streamlit Application:**  
   The **Streamlit** application allows users to visualize insights and interact with the analyses dynamically. You can access the application at the following link: [Motorcycle Sales Analysis Streamlit App](https://cds-motorcycle-sales-analysis.streamlit.app/).


## Contact

For questions or feedback, feel free to reach out at [rennanreis@me.com].