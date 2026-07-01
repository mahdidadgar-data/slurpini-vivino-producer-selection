# Data Folder

This folder contains the data structure used for the Slurpini Vivino wine analysis project.

## Raw Data

The original raw Excel workbook is expected at:

```text
data/raw/Vivino-export.xlsx
```

The raw Vivino export is **not included in this public repository** because dataset sharing rights may be restricted.

## Processed Outputs

The notebook exports cleaned and summary outputs to:

```text
data/processed/
```

The detailed cleaned wine-level dataset is not included publicly:

```text
data/processed/cleaned_italian_wines.csv
```

This file is excluded because it still contains detailed wine-level derived data from the original Vivino export.

The producer-candidate shortlist CSV is also not redistributed publicly. It is kept only as a screenshot/table inside the report or README visuals for storytelling purposes.

The repository may include smaller aggregated summary outputs that support the project documentation, such as:

* `data_quality_log.csv`
* `price_outlier_impact_summary.csv`
* `region_opportunity_scores.csv`
* `region_scoring_sensitivity_summary.csv`
* `strategic_region_summary.csv`
* `value_metric_sensitivity_summary.csv`

## Reproducibility

To reproduce the full analysis:

1. Place the raw Excel file in `data/raw/`.
2. Run the notebook in `notebooks/`.
3. The processed outputs will be generated automatically in `data/processed/`.

## Responsible Data Use

This project uses Vivino consumer review data for educational and portfolio purposes. The analysis is intended as a decision-support workflow and should not be interpreted as a final commercial producer selection system without additional validation.

The original raw data, detailed wine-level dataset, and producer-candidate shortlist CSV are not redistributed in this public repository.
