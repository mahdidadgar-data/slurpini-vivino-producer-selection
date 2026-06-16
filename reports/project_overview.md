# Project Overview

# Slurpini Wine Producer Selection Using Vivino Consumer Data

**Author:** Mahdi Dadgar
**Project Type:** Business Analytics / Data Science — Data Cleaning, Exploratory Data Analysis, Robust Scoring Model
**Domain:** Wine Import / Consumer Review Analytics / Market Selection
**Business Use Case:** Data-driven pre-selection of promising Italian wine regions and producer candidates for potential collaboration

---

## 1. Project Summary

Slurpini is an importer of high-quality Italian wines with a strong focus on sustainability. The company receives collaboration requests from wine producers across Italy and needs a more objective way to decide which regions or producers are worth further investigation.

The goal of this project was to use Vivino consumer review data from the Dutch market to support Slurpini’s producer pre-selection process. Instead of relying only on intuition, producer requests, or costly exploratory visits, the project builds a structured analytical framework based on market evidence.

The final portfolio-ready version includes data cleaning, exploratory analysis, value-for-money evaluation, price outlier review, sensitivity analysis, region opportunity scoring, producer-candidate extraction, and business recommendations.

---

## 2. Business Problem

Slurpini regularly receives collaboration requests from wine producers across Italy. However, visiting and evaluating producers in person requires time, budget, and operational effort.

The company needs a structured way to prioritize which producer opportunities deserve further investigation. A purely intuition-based selection process can lead to inefficient use of resources and may overlook regions with strong consumer potential.

The main business question was:

**Which Italian wine regions and producer candidates show the strongest potential based on consumer ratings, popularity, price, value for money, and commercial relevance in the Dutch market?**

---

## 3. Dataset Overview

The project used a Vivino dataset containing wines rated by consumers in the Netherlands.

The original dataset contained wine information such as:

| Field          | Description                       |
| -------------- | --------------------------------- |
| `name`         | Wine name and vintage information |
| `country`      | Country of origin                 |
| `region`       | Wine region                       |
| `rating`       | Average Vivino consumer rating    |
| `rating_count` | Number of consumer ratings        |
| `price`        | Listed wine price                 |

The raw workbook was not immediately analysis-ready. Each sheet contained CSV-like text stored in one column, which required parsing before the data could be used in a proper tabular format.

---

## 4. Data Cleaning and Preparation

The dataset required significant preparation before analysis.

Key cleaning and preparation steps included:

* parsing raw workbook sheets into structured columns;
* combining multiple sheets into one dataframe;
* removing exact duplicate rows;
* cleaning tuple-like country and region values;
* correcting visible text encoding issues;
* aggregating repeated observations into wine-level records;
* filtering the project scope to Italian wines;
* exporting cleaned analytical datasets.

Key preparation results:

| Metric                                  |   Value |
| --------------------------------------- | ------: |
| Parsed raw rows                         | 409,777 |
| Exact duplicate rows                    | 222,522 |
| Rows after duplicate removal            | 187,255 |
| Unique wine-level records               |  14,088 |
| Final Italian wine records              |   2,986 |
| Italian regions                         |     179 |
| Missing values in final Italian dataset |       0 |
| Remaining visible encoding artifacts    |       0 |

---

## 5. Portfolio-Ready Improvements

After the original bootcamp submission, the project was improved to make it more suitable for a professional portfolio.

Main improvements included:

* formal data quality control log;
* explicit price outlier policy;
* before/after outlier impact check;
* value metric sensitivity analysis;
* scoring-weight robustness check;
* deeper analytical layer using correlation and price-band analysis;
* producer-candidate extraction from wine names;
* final producer-candidate shortlist;
* stronger limitations and responsible-use discussion;
* reproducible project folder structure using `src/` helper modules.

These additions make the project more robust, reproducible, and defensible.

---

## 6. Analytical Approach

The project followed a business-oriented analytical workflow:

1. Workbook inspection
2. Raw data parsing
3. Data quality assessment
4. Data cleaning and aggregation
5. Italian wine subset creation
6. Exploratory data analysis
7. Price outlier review
8. Value-for-money analysis
9. Sensitivity analysis
10. Region opportunity scoring
11. Producer-candidate extraction
12. Final shortlist and recommendations

---

## 7. Region Opportunity Scoring Model

A transparent region opportunity scoring model was created to compare Italian wine regions.

The model combined five business-relevant components:

| Component                 | Business Meaning                        |
| ------------------------- | --------------------------------------- |
| Quality score             | Average consumer rating                 |
| Popularity score          | Median rating count                     |
| Value-for-money score     | Rating and popularity relative to price |
| Reliability score         | Number of wines in the region           |
| Price accessibility score | More commercially accessible pricing    |

The model was designed as a decision-support tool, not as an automatic decision system.

---

## 8. Producer-Candidate Shortlist

Because the dataset did not contain a clean separate producer column, producer candidates were extracted from wine names using a conservative heuristic.

The shortlist includes:

* producer candidate;
* region;
* representative wine;
* rating;
* rating count;
* median price;
* price band;
* shortlist justification.

This output directly supports the business goal of producer pre-selection.

---

## 9. Key Insights

Several important insights were identified:

1. **Rating alone is not enough.**
   Italian wine ratings are relatively compressed around 4.0, so small differences should not be overinterpreted.

2. **Popularity improves reliability.**
   Rating count helps identify wines and regions with stronger consumer validation.

3. **Premium and value opportunities are different.**
   Premium regions often show strong quality signals, while value-oriented regions may offer stronger commercial accessibility.

4. **A portfolio strategy is more useful than selecting one region.**
   Slurpini can benefit from combining premium quality, value-for-money, and high-visibility opportunities.

5. **Vivino data supports pre-selection, not final partnership decisions.**
   Final producer selection should include sustainability checks, tastings, supplier conversations, logistics, margins, and brand fit.

---

## 10. Business Recommendations

The main recommendation is that Slurpini should use a portfolio-based selection strategy instead of choosing one single “best” region.

Recommended opportunity groups:

### Premium quality opportunities

These regions are suitable for premium restaurants, wine bars, and high-end customers.

### Value-for-money opportunities

These regions may support direct-to-consumer offers and hospitality clients looking for attractive quality at manageable prices.

### High-visibility opportunities

These regions can support market recognition, consumer awareness, and stable portfolio coverage.

### Producer-candidate shortlist

The producer-candidate shortlist should be used as a first-stage screening tool. Before any final collaboration decision, Slurpini should validate:

* sustainability certification;
* organic or biodynamic production;
* supplier reliability;
* production capacity;
* logistics feasibility;
* margin potential;
* brand fit.

---

## 11. Limitations

This project has several important limitations:

* Vivino users may not represent the full Dutch wine market.
* Rating count is a proxy for popularity, not actual sales.
* Listed prices may not reflect wholesale prices, import costs, or margins.
* Sustainability and organic certification data were not available.
* Producer candidates were extracted heuristically and require manual validation.
* Scoring weights are business assumptions and should be reviewed with stakeholders.
* The model should support human judgment, not replace it.

---

## 12. Tools and Skills Demonstrated

This project demonstrates practical skills in:

* Python;
* Pandas and NumPy;
* data parsing;
* data cleaning;
* exploratory data analysis;
* value-for-money analysis;
* robustness and sensitivity analysis;
* transparent scoring model design;
* producer-candidate extraction;
* business recommendation development;
* responsible data use;
* reproducible project structure.

---

## 13. Final Conclusion

This project shows how messy real-world consumer review data can be transformed into a structured decision-support framework.

The final solution helps Slurpini move from intuition-based producer exploration toward a more transparent, evidence-based pre-selection process.

The main business value is not only the final ranking, but the creation of a repeatable analytical workflow that Slurpini can reuse and improve over time.
