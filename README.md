# VANGUARD A/B TEST

- [Presentation](https://docs.google.com/presentation/d/12Kd4BYSKqSL1LLOXoFSM1wFfO5M47FknlkYkO05ZMDE/edit?usp=sharing)
- [Tableau](https://public.tableau.com/views/VanguardAB/VanguardAB?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

## Introduction

This project involves analyzing an A/B test conducted by Vanguard to understand client behavior and preferences. The goal is to determine whether a new variation (Test group) of a digital process improves client engagement and success rates compared to the existing version (Control group).

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
