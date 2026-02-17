# Data Terminology (Tidy Data Perspective)

## 1. Dataset

A **dataset** is a structured collection of values.

Values may include:

- **Numerical data** (e.g., age, salary, score)
- **Character/string data** (e.g., names, cities)

Data can be stored in various formats, such as:

- Spreadsheets
- Databases
- Data frames

Every value in a dataset must belong to:

- A **variable** (what is being measured)
- An **observation** (who or what is being measured)

---

## 2. Variables

**Variables** represent the different attributes or features collected in a dataset.

They define **what kind of information is recorded**.

Each variable corresponds to:

- **One column** in a tidy dataset

### Example Variables

- ID  
- LastName  
- FirstName  
- Sex  
- City  
- State  
- Occupation  

Variable names are typically placed in:

- The **first row** (in spreadsheets)
- The **column headers** (in data frames)

---

## 3. Observations

An **observation** represents a single recorded instance of data.

It contains:

- **One value for each variable**

In tidy data:

- Each observation occupies **one row**
- Each value is stored in its corresponding **variable column**

Conceptually:

> **One row = one entity**  
(e.g., one person, one transaction, one experiment trial)

---

## 4. Types (Data Types / Data Sources)

Data may be collected from multiple sources or measurement processes.

Different sources can produce **different types of data** for the same individuals.

### Example

- **Self-reported survey data** (filled by the patient)
- **Clinical measurements** (collected by a doctor)

These represent:

- Different **measurement contexts**
- Potentially different **data structures**

According to tidy data principles:

> Each type of observational unit should typically be stored in a **separate table**

---

## Summary Structure (Tidy Data Principles)

- Each **variable** → one column  
- Each **observation** → one row  
- Each **type of observational unit** → one table  
