# Common Problems with Messy Datasets

Messy datasets violate tidy data principles and make analysis, modeling, and visualization difficult. The following are common structural problems found in messy datasets.

---

## 1. Column Headers Are Values but Should Be Variable Names

Column headers sometimes contain **data values instead of variable names**.

This violates the tidy data principle that:

> Each variable must have its own column, and column headers must represent variable names.

### Problem Example

| ID | Jan | Feb | Mar |
|----|-----|-----|-----|
| 1  | 100 | 120 | 140 |

Here, `Jan`, `Feb`, and `Mar` are **values of a variable (Month)**, not variable names.

### Correct Tidy Structure

| ID | Month | Sales |
|----|-------|-------|
| 1  | Jan   | 100   |
| 1  | Feb   | 120   |
| 1  | Mar   | 140   |

---

## 2. A Single Column Contains Multiple Variables

Sometimes multiple variables are combined into a single column.

This violates the principle:

> Each variable must be stored in its own column.

### Problem Example

| ID | Name            |
|----|------------------|
| 1  | John Smith      |

Here, `Name` contains two variables:

- FirstName  
- LastName  

### Correct Tidy Structure

| ID | FirstName | LastName |
|----|------------|----------|
| 1  | John       | Smith    |

---

## 3. Variables Are Stored in Both Rows and Columns

Variables should be represented only as columns, not spread across both rows and columns.

This violates the principle:

> Each variable must be a column.

### Problem Example

| ID | Height | Weight |
|----|--------|--------|
| 1  | 170    | 65     |

But elsewhere in the dataset:

| Variable | Value |
|----------|--------|
| Height   | 170    |
| Weight   | 65     |

This creates structural inconsistency.

### Correct Tidy Structure

| ID | Height | Weight |
|----|--------|--------|
| 1  | 170    | 65     |

---

## 4. Multiple Types of Data Stored in the Same Spreadsheet

Different observational units are sometimes stored in the same table.

This violates the principle:

> Each type of observational unit must be stored in its own table.

### Problem Example

| PatientID | PatientName | VisitDate | TestResult |
|-----------|--------------|------------|-------------|

This mixes:

- Patient data
- Visit data
- Measurement data

### Correct Structure

Separate into multiple tables:

**patients table**

| patient_id | patient_name |
|------------|---------------|

**visits table**

| visit_id | patient_id | visit_date |
|----------|-------------|-------------|

**measurements table**

| measurement_id | patient_id | test_result |
|----------------|-------------|--------------|

---

## 5. A Single Observation Is Stored Across Multiple Spreadsheets

Sometimes information about one observation is fragmented across multiple files.

This violates the principle:

> Each observation should be stored as one row in one table.

### Problem Example

**File 1: Personal Information**

| ID | Name |
|----|------|

**File 2: Measurements**

| ID | Weight |

### Correct Structure

Either:

- Store in one table if same observational unit

| ID | Name | Weight |

Or:

- Store in separate relational tables connected by a key

---

## Summary of Messy Data Problems

| Problem | Violation |
|--------|------------|
| Column headers contain values | Variable-column mismatch |
| Single column contains multiple variables | Variable separation violation |
| Variables stored in both rows and columns | Structural inconsistency |
| Multiple observational units in one table | Table normalization violation |
| Single observation split across files | Observation fragmentation |

---

## Key Insight

Messy data violate tidy data principles, resulting in:

- Difficult preprocessing
- Increased risk of analytical errors
- Reduced reproducibility
- Poor compatibility with data analysis tools

Tidying data resolves these structural issues and enables efficient, reliable analysis.
