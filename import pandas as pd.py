import pandas as pd
from scipy.stats import chi2_contingency

# Sample Data
data = {
    'department': ['Sales', 'Engineering', 'Engineering', 'Sales', 'HR', 'Engineering', 'Sales', 'HR'],
    'training_completed': ['Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']
}
df = pd.DataFrame(data)

# 1. Create a contingency table
contingency_table = pd.crosstab(df['department'], df['training_completed'])
print("--- Contingency Table ---")
print(contingency_table)

# 2. Perform the Chi-Square test
chi2, p_value, dof, expected = chi2_contingency(contingency_table)

print(f"\nChi-Square Statistic: {chi2:.4f}")
print(f"P-value: {p_value:.4f}")

# 3. Interpret the result
alpha = 0.05
if p_value < alpha:
    print("\nResult: Reject the null hypothesis. There is a significant association between department and training completion.")
else:
    print("\nResult: Fail to reject the null hypothesis. There is no significant association.")