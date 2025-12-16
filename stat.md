# Statistical Tests: Chi-Square vs. ANOVA

This document explains when to use the Chi-Square test and ANOVA, two common statistical methods for hypothesis testing.

---

## 1. Chi-Square (χ²) Test of Independence

Use the Chi-Square test when you want to determine if there is a statistically significant **association between two categorical variables**.

-   **Question it Answers:** "Are these two categorical variables independent, or is there a relationship between them?"
-   **Variable Types:**
    -   Independent Variable: Categorical
    -   Dependent Variable: Categorical

### Hypotheses

-   **Null Hypothesis (H₀):** The two variables are independent. There is no association between them.
-   **Alternative Hypothesis (H₁):** The two variables are dependent. There is an association between them.

### Example

Imagine a company wants to know if the `Department` an employee works in is associated with their `Job Satisfaction` level.

-   **Variable 1 (Categorical):** `Department` (e.g., 'Sales', 'Engineering', 'HR')
-   **Variable 2 (Categorical):** `Job Satisfaction` (e.g., 'Low', 'Medium', 'High')

You would collect data and create a contingency table:

| Department  | Low | Medium | High |
| :---------- | --: | -----: | ---: |
| Sales       |  10 |     30 |   40 |
| Engineering |  25 |     25 |   10 |
| HR          |   5 |     10 |    5 |

The Chi-Square test compares this observed data to what you would *expect* if there were no relationship.

### Interpreting the Results

-   **Low p-value (e.g., < 0.05):** You **reject the null hypothesis**. This means there is a statistically significant association. For example, you might conclude that employees in the Sales department have a significantly different pattern of job satisfaction compared to those in Engineering.
-   **High p-value (e.g., > 0.05):** You **fail to reject the null hypothesis**. This means you do not have enough evidence to say there is an association. The observed differences are likely due to random chance.

---

## 2. ANOVA (Analysis of Variance)

Use ANOVA when you want to compare the **means of a continuous variable** across **three or more groups** of a categorical variable.

-   **Question it Answers:** "Is there a statistically significant difference between the average values of my groups?"
-   **Variable Types:**
    -   Independent Variable (Groups): Categorical (with 3+ levels)
    -   Dependent Variable (Measured): Continuous (Numerical)

*(Note: If you are comparing the means of only **two** groups, you would use a **t-test** instead of ANOVA.)*

### Hypotheses

-   **Null Hypothesis (H₀):** The means of all groups are equal (e.g., μ_group1 = μ_group2 = μ_group3).
-   **Alternative Hypothesis (H₁):** At least one group mean is different from the others.

### Example

A company wants to know if there is a significant difference in the average `Salary` across different `Education Levels`.

-   **Variable 1 (Categorical Groups):** `Education Level` ('Bachelors', 'Masters', 'PhD')
-   **Variable 2 (Continuous):** `Salary` (e.g., $70,000, $95,000, $120,000)

ANOVA will analyze the variance *within* each education group and the variance *between* the education groups.

### Interpreting the Results

-   **Low p-value (e.g., < 0.05):** You **reject the null hypothesis**. This tells you that there is a statistically significant difference in the mean salary between at least two of the education levels.
-   **High p-value (e.g., > 0.05):** You **fail to reject the null hypothesis**. You do not have enough evidence to conclude that a difference in mean salaries exists between the education groups.

**Important:** ANOVA tells you *if* there is a difference somewhere among the groups, but it doesn't tell you *which specific groups* are different from each other. To find that out, you would need to perform a "post-hoc" test (like Tukey's HSD) after getting a significant ANOVA result.