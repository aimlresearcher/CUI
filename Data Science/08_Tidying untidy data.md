# Tidying Untidy Data

Tidying untidy data is the process of transforming structurally inconsistent datasets into a standardized format that satisfies tidy data principles. The specific actions required depend on the nature and severity of the structural violations present in the dataset.

Common data tidying operations include:

- Filtering data  
- Transforming values  
- Modifying variables  
- Aggregating data  
- Sorting observations  

Statistical programming environments such as R provide functions to perform each of these operations efficiently. However, before applying these transformations programmatically, it is essential to develop the ability to:

- Identify untidy data structures  
- Diagnose structural violations  
- Determine the necessary transformations required to achieve tidy structure  

---

## Case Study: Dataset D from *Data Organization in Spreadsheets*

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/17.png)

Consider Dataset D from the *Data Organization in Spreadsheets* examples.

This dataset contains several tidy data violations, including:

- Blank cells representing missing values  
- Non-rectangular structure  
- Multiple observational units stored in a single spreadsheet  
- Structural ambiguity between sample metadata and measurement data  

These issues prevent direct analysis and must be resolved through data restructuring.

**Figure:** Messy dataset

---

## Tidying Strategy: Splitting into Multiple Spreadsheets

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/18.png)

To resolve these structural violations, the dataset can be split into two separate spreadsheets, each representing a distinct observational unit.

### Spreadsheet A: Sample Metadata

This spreadsheet contains descriptive information about each sample.

This table represents the **sample-level observational unit**, where each row corresponds to one sample.

---

### Spreadsheet B: Sample Measurements Over Time

This spreadsheet contains measurement values collected over time for each sample.


This table represents the **measurement-level observational unit**, where each row corresponds to one measurement at a specific time point.

---

## Relational Link Between Spreadsheets

Both spreadsheets include a common key column: **id**

This key enables relational operations that allow the datasets to be combined when needed during analysis.

This supports relational joins such as:

- left_join  
- inner_join  
- right_join  
- full_join  

This ensures relational integrity while maintaining proper tidy structure.

---

## Handling Missing Values

The **note** column contains missing values.

These blank cells must be replaced with **NA**.

This ensures:

- Explicit representation of missing data  
- Compliance with tidy data principles  
- Elimination of structural ambiguity  

Blank cells should never be used because they introduce uncertainty and complicate analysis.

---

## Structural Insight: Splitting a Single Spreadsheet into Multiple Tables

During the tidying process, it is sometimes necessary to split a single spreadsheet into multiple spreadsheets.

This is acceptable and correct when:

- Multiple observational units exist in the original dataset  
- Each observational unit requires its own table  

The critical requirement is the presence of a consistent linking variable such as **id**

This ensures the datasets can be merged during analysis when necessary.

---

## Final Outcome: Tidy Version of the Dataset

After tidying, the dataset satisfies tidy data principles:

- Each variable is stored in its own column  
- Each observation occupies its own row  
- Each observational unit is stored in its own table  
- Each cell contains a single value  
- Missing values are explicitly represented using **NA**  
- Tables are relationally connected using a common key such as **id**

**Figure:** Tidy version of the messy dataset

---

## Conceptual Summary

Tidying untidy data may involve:

- Splitting datasets into multiple relational tables  
- Replacing blank cells with explicit missing value indicators  
- Enforcing rectangular structure  
- Ensuring one variable per column  
- Ensuring one observation per row  
- Maintaining relational integrity via key variables such as **id**

Tidying transforms structurally inconsistent datasets into analysis-ready, machine-readable, and computationally reliable data.

This process is a foundational step in the data science pipeline and is essential for ensuring accurate statistical modeling, reliable analysis, and reproducible research.
