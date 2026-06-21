import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("income.csv", names=["name", "income"])

print("Original Dataset:")
print(df)


# Statistical summary
print("\nStatistical Summary:")
print(df.income.describe())


# Percentile analysis
print("\nMinimum Income:")
print(df.income.quantile(0))

print("\n25th Percentile:")
print(df.income.quantile(0.25, interpolation="higher"))


# Detecting outliers using 99th percentile
percentile_99 = df.income.quantile(0.99)

print("\n99th Percentile:")
print(percentile_99)


# Dataset with outliers
df_outlier = df[df.income > percentile_99]

print("\nOutliers:")
print(df_outlier)


# Dataset without outliers
df_no_outlier = df[df.income <= percentile_99]

print("\nDataset after removing outliers:")
print(df_no_outlier)


# Handling missing values
# Creating a missing value for demonstration
df.loc[3, "income"] = np.nan

print("\nDataset with missing value:")
print(df)


# Filling missing values using median
median_income = df.income.median()

df_new = df.fillna(median_income)

print("\nDataset after filling missing values:")
print(df_new)


# Comparing mean and median
print("\nMean Income:")
print(df.income.mean())

print("\nMedian Income:")
print(df.income.median())