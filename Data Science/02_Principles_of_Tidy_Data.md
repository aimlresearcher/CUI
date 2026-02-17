# Principles of Tidy Data (Hadley Wickham, 2014)

According to Hadley Wickham (2014) in the paper *“Tidy Data”*:

Tidy datasets are easy to:

- Manipulate  
- Model  
- Visualize  

They follow a specific structure:

- Each variable → a column  
- Each observation → a row  
- Each type of observational unit → a table  

These form the core tidy data principles.

---

## Principle 1: Each Variable → One Column

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/4.png)

Every measured attribute must have its own dedicated column.

- No multiple variables should be stored in a single column.
- Column names represent variable names.
- Each cell contains a single atomic value (no concatenated fields).

### Implication in tidyverse:

- Enables vectorized operations.
- Supports clean `mutate()`, `filter()`, `select()`, and `summarise()` operations.

---

## Principle 2: Each Observation → One Row

Each row represents a single observational unit instance.

- Each observation contains one value per variable.
- No stacking of multiple observations within the same row.

### Example interpretation:

- One person → one row  
- One transaction → one row  
- One time point measurement → one row  

### Analytical benefit:

- Facilitates row-wise operations.
- Supports grouping (`group_by()`) and modeling pipelines.

---

## Principle 3: One Table per Type of Observational Unit

Different types of entities should be stored in separate tables.

- Each table represents one kind of observational unit.

### Example:

- patients table → patient-level data  
- visits table → visit-level data  
- measurements table → lab test results  

### Design rationale:

- Avoids structural redundancy.
- Preserves relational integrity.
- Aligns with database normalization principles.

---

## Principle 4: Tables Must Be Joinable

If multiple tables exist:

- Each must contain a common key column.
- The key must have the same name and meaning.
- This enables relational operations.

### Example key:


### Tidyverse implication:

- Enables `left_join()`, `inner_join()`, `right_join()`, etc.
- Supports modular data modeling.

---

## Conceptual Summary

| Principle | Structural Rule | Analytical Benefit |
|----------|-----------------|--------------------|
| 1 | One variable per column | Clean vectorized transformations |
| 2 | One observation per row | Reliable aggregation & modeling |
| 3 | One type of unit per table | Relational clarity |
| 4 | Common keys across tables | Safe joins & merging |

---

## Why Tidy Data Matters (From a Data Science Perspective)

- Reduces preprocessing complexity.
- Minimizes ambiguity in statistical modeling.
- Enhances reproducibility.
- Aligns with relational database theory.
- Enables scalable pipelines in tidyverse.
