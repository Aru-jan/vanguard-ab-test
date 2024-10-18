# VANGUARD A/B TEST

## Introduction

This project involves analyzing an A/B test conducted by Vanguard to understand client behavior and preferences. The goal is to determine whether a new variation (Test group) of a digital process improves client engagement and success rates compared to the existing version (Control group).

## Table of Contents

- Metadata
- Project Structure
- Installation
- Usage
- Data Description
- Data Cleaning
- Data Exploration
- Statistical Analysis
- Results
- Conclusion
- License

## Metadata

This comprehensive set of fields will guide your analysis, helping you unravel the intricacies of client behavior and preferences.

- `client_id`: Every client’s unique ID.
- `variation`: Indicates if a client was part of the experiment (Test or Control).
- `visitor_id`: A unique ID for each client-device combination.
- `visit_id`: A unique ID for each web visit/session.
- `process_step`: Marks each step in the digital process.
- `date_time`: Timestamp of each web activity.
- `clnt_tenure_yr`: Represents how long the client has been with Vanguard, measured in years.
- `clnt_tenure_mnth`: Further breaks down the client’s tenure with Vanguard in months.
- `clnt_age`: Indicates the age of the client.
- `gendr`: Specifies the client’s gender.
- `num_accts`: Denotes the number of accounts the client holds with Vanguard.
- `bal`: Gives the total balance spread across all accounts for a particular client.
- `calls_6_mnth`: Records the number of times the client reached out over a call in the past six months.
- `logons_6_mnth`: Reflects the frequency with which the client logged onto Vanguard’s platform over the last six months.

## Project Structure

- `data`: Contains the raw and cleaned data files.
- `notebooks`: Jupyter notebooks used for analysis.
- `scripts`: Python scripts for data cleaning, mining, database handling, and analysis.
- `README.md`: Project documentation.

## Installation

To run this project, you’ll need to have Python 3.x installed along with the necessary packages listed in the `requirements.txt` file.

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/vanguard-ab-test.git
    cd vanguard-ab-test
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables by creating a `.env` file:

    ```bash
    touch .env
    ```

    Add your environment variables in the `.env` file:

    ```
    SQL_PASSWORD=your_sql_password
    ```

## Usage

1. Run the data cleaning and analysis scripts:

    ```bash
    python scripts/cleaning.py
    python scripts/mining.py
    python scripts/analysis.py
    ```

2. Alternatively, you can open and run the Jupyter notebook:

    ```bash
    jupyter notebook notebooks/vanguard_ab_test.ipynb
    ```

## Data Description

The data is split into three main datasets:

- `Clients`: Contains demographic and account information for each client.
- `Experiment`: Indicates which variation (Test or Control) each client was assigned to.
- `Visits`: Logs of web activities for each client during their visits.

## Data Cleaning

Data cleaning steps include:

- **Removing Null Values**: Null values in critical columns are removed to ensure data integrity.
- **Type Conversion**: Data types are appropriately converted for analysis.
- **Categorical Data Cleaning**: Categories are standardized and cleaned.
- **Outlier Removal**: Outliers in `total_time_taken` are removed using Tukey’s method.

## Data Exploration

- **Merging Datasets**: The clients, experiment, and visits datasets are merged for comprehensive analysis.
- **Sorting and Filtering**: Visits are sorted by time, and non-relevant or duplicate visits are removed.
- **Feature Engineering**: New features like `time_taken` and `total_time_taken` are calculated.
- **Outlier Analysis**: Histograms and boxplots are used to visualize and remove outliers.

## Statistical Analysis

- **Happy Paths**: Analysis of clients who followed the ideal process steps.
- **Confused Paths**: Clients who reached the final step but did not follow the happy path.
- **Dropped Paths**: Clients who did not complete the process.
- **Correlation Analysis**: Examining correlations between numerical variables.
- **Proportion Z-Test**: Testing the difference in proportions between Test and Control groups.
- **T-Test**: Comparing average `total_time_taken` between groups.

## Results

- **Success Rate**: The Test group showed a higher success rate in following the happy path compared to the Control group.
- **Time Efficiency**: Clients in the Test group took less time to complete the process steps.
- **Confused Paths**: The proportion of clients taking confused paths was analyzed, indicating areas for improvement.
- **Statistical Significance**: Statistical tests confirmed that the differences observed were significant.

## Conclusion

The A/B test results suggest that the new variation (Test group) is more effective in guiding clients through the process efficiently. The Test group not only had a higher success rate but also completed the process faster than the Control group. These findings support implementing the new variation to enhance client experience.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## Additional Information

For more detailed insights, please refer to the notebook which includes all the code and visualizations used in this analysis.

**Contact**: If you have any questions or suggestions, feel free to contact `your.email@example.com`.

*Note: Replace placeholders like `yourusername`, `your_sql_password`, and contact information with actual details relevant to your project.*