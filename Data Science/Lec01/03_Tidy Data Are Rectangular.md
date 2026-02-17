## Rectangular Structure of Tidy Data

Tidy data are **rectangular in structure**.

A tidy dataset must form a **rectangle (tabular format)**.

![Variables](https://github.com/aimlresearcher/CUI/blob/main/Data%20Science/images/8.png)

### Structural Requirements

- Each variable must be stored in a separate column.
- Each observation (entry) must occupy a separate row.
- Each cell must contain a single value.
  - No merged cells
  - No multiple values in a single cell

### Visual and Structural Consistency

The dataset should visually and structurally resemble a complete rectangle, meaning:

- Consistent alignment across rows and columns
- No irregular gaps or structural inconsistencies
- Uniform column definitions across all rows

### Diagnostic Criterion

If the dataset does not form a clean rectangle after processing, it is likely not yet fully tidy.

### Final Checkpoint in Data Tidying

When tidying data, the final validation question is:

> Does the dataset satisfy the rectangular constraint?

- If **yes** → The dataset is structurally tidy.  
- If **no** → Additional transformation is required.
