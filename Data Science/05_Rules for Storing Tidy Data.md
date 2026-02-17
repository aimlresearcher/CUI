# Rules for Storing Tidy Data

Beyond the four tidy data principles, additional data-entry guidelines improve analysis and visualization. These guidelines were formalized in the paper **Data Organization in Spreadsheets** by Karl Broman and Kara Woo. The goal is to ensure that data are not only tidy, but also **analysis-ready** and **machine-readable**.

---

## Core Guidelines

### 1. Be Consistent

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/9.png)

Maintain consistency in data entry, variable naming, and file naming.

Code categorical variables uniformly. For example, use only `"female"` and `"male"`, not `"F"` and `"female"`.

Keep variable names identical across datasets. For example, always use `ID`, not `id` or `identifier`.

Use consistent:

- Date formats  
- Capitalization  
- Spacing  
- File naming conventions  

Consistency reduces ambiguity and downstream preprocessing effort.

---

### 2. Choose Good Names for Things

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/10.png)


Avoid spaces in file and variable names.

Prefer underscores `_` over spaces. Example: `doctor_visit_v1`.

Use names that are:

- Short  
- Meaningful  
- Self-descriptive  

Avoid vague labels such as `F1`.

Use explicit versioning. Example: `doctor_visit_v1`, `doctor_visit_v2`.

Examples:

- Good: `FirstName`, `weight_lbs`  
- Poor: `First Name`, `Doctor Visit 1`  

---

### 3. Write Dates as YYYY-MM-DD

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/11.png)


Follow the international ISO 8601 format: **YYYY-MM-DD**.

Example: **2018-02-27**

Benefits:

- Eliminates cross-country ambiguity  
- Prevents spreadsheet software from misinterpreting dates  
- Ensures lexicographic sorting aligns with chronological order  

---

### 4. No Empty Cells

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/12.png)


Every cell must contain a value.

If data are unknown, use `NA`.

Avoid blank cells that create ambiguity about whether data are missing or inherited from previous rows.

Empty cells violate tidy principles and complicate analysis.

---

### 5. Put Just One Thing in a Cell

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/13.png)


Each cell must contain a single atomic value.

Do not combine numbers and units. Avoid entries like `165 lbs`.

Instead, store the value as `165`, and encode the unit in the variable name (e.g., `weight_lbs`) or a separate column.

Avoid mixed data types within a column.

This ensures numeric columns remain numeric, which is essential for statistical modeling.

---

### 6. Don’t Use Font Color or Highlighting as Data

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/14.png)


Do not encode meaning using formatting such as font color or highlighting.

Instead, create an explicit variable. Example: `outlier = TRUE`.

Formatting is not machine-readable and may be lost during data import or export. Metadata must be explicit, not visual.

---

### 7. Save Data as Plain Text Files

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/15.png)


Prefer open, non-proprietary formats such as `.csv` and `.txt`.

Advantages:

- Software-independent  
- Platform-independent  
- Easily parsed programmatically  
- Suitable for long-term archival  

---

## Conceptual Summary

A well-structured tidy dataset should satisfy the following conditions:

- Rectangular structure  
- One variable per column  
- One observation per row  
- One value per cell  
- No empty cells  
- Consistent naming and encoding  
- ISO-compliant date formatting (YYYY-MM-DD)  
- No visual formatting as metadata  
- Stored in plain text format  

---

## Analytical and Computational Benefits

These principles ensure:

- Lower preprocessing overhead  
- Higher reproducibility  
- Easier integration across tools  
- Reduced cognitive and computational friction  

These practices are foundational requirements for scalable, reproducible, and machine-readable data science workflows.
