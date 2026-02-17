# Examples of Untidy Data

To understand messy datasets in practice, it is useful to examine real-world examples where tidy data principles are violated. These examples illustrate common structural and formatting issues that prevent effective data analysis.

---

## Examples from *Data Organization in Spreadsheets*

Several examples presented in the paper *Data Organization in Spreadsheets* demonstrate violations of tidy data principles.

Common problems observed in these datasets include:

- Variables are not stored in unique columns.
- Column headers do not consistently represent variable names.
- Empty cells are present throughout the dataset.
- The dataset does not form a clean rectangular structure.
- Structural alignment across rows and columns is inconsistent.

Datasets formatted in these messy ways create significant obstacles during analysis, including:

- Difficulty in data import and parsing
- Ambiguity in variable interpretation
- Increased preprocessing overhead
- Higher risk of analytical errors

**Figure:** Examples from *Data Organization in Spreadsheets*

---

## Case Study 1: Miles McBain — Australian Marriage Survey Data

Miles McBain, a data scientist from Brisbane, Australia, attempted to analyze Australian postal survey data on marriage.

Before analysis could begin, extensive data tidying was required.

He identified several structural and formatting issues, including:

- Commas used in numerical values (e.g., `1,000`)
- Blank cells representing missing or implicit values
- Junk metadata rows at the top of the spreadsheet
- Merged cells violating rectangular structure
- Inconsistent formatting across rows and columns

These issues would have prevented reliable analysis if left unresolved.

To address these problems, Miles systematically cleaned and transformed the dataset into a tidy format.

He documented the entire cleaning process in a Medium article, explaining:

- Identification of structural violations
- Data normalization procedures
- Conversion into analysis-ready format

**Figure:** Miles McBain’s tidying of Australian Same-Sex Marriage Postal Survey Data

---

## Case Study 2: Sharla Gelfand — Toronto Open Data

Inspired by Miles McBain’s work, Sharla Gelfand undertook a similar effort to clean a messy dataset from Toronto’s open data portal.

She identified multiple tidy data violations, including:

- Names and addresses split across multiple cells
- Merged column headings
- Numerous blank cells
- Structural inconsistencies across rows
- Poorly defined variable boundaries

These issues prevented immediate analytical use of the dataset.

Sharla documented her data cleaning workflow in a blog post, including:

- Identification of messy structural patterns
- Data restructuring procedures
- Conversion into tidy format suitable for analysis

Although the programming details may initially appear complex, they become clearer with familiarity with data manipulation tools such as R and tidyverse.

**Figure:** Sharla Gelfand’s tidying of Toronto’s open data

---

## Key Insight

These real-world examples demonstrate that messy data commonly violate tidy data principles, including:

- One variable per column
- One observation per row
- One value per cell
- Rectangular structure
- Explicit and consistent variable definitions

Data tidying is a critical preprocessing step that transforms structurally inconsistent datasets into reliable, analysis-ready formats.

Without tidying, statistical modeling, visualization, and computational analysis become unreliable or impossible.

Data cleaning is therefore not optional—it is a foundational stage of the data science pipeline.
