from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd


_ROW_PATTERN = re.compile(
    r'^(?P<name>.*),"(?P<country>\(.*?\))","(?P<region>\(.*?\))",'
    r'(?P<rating>[-+]?\d*\.?\d+),'
    r'(?P<rating_count>\d+),'
    r'(?P<price>[-+]?\d*\.?\d+)$'
)


def parse_vivino_export(excel_path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Parse the Vivino-export.xlsx workbook into a structured dataframe.

    The raw workbook sheets contain one text column where each row is a CSV-like
    string. This function parses all sheets into one dataframe.
    """

    excel_path = Path(excel_path)
    excel_file = pd.ExcelFile(excel_path)

    parsed_rows: list[dict] = []
    problem_rows: list[dict] = []

    for sheet in excel_file.sheet_names:
        raw_sheet = pd.read_excel(excel_path, sheet_name=sheet, header=None)
        raw_rows = raw_sheet.iloc[1:, 0].dropna().astype(str)

        for row_number, raw_row in raw_rows.items():
            match = _ROW_PATTERN.match(raw_row)
            if match:
                row_data = match.groupdict()
                row_data["source_sheet"] = sheet
                parsed_rows.append(row_data)
            else:
                problem_rows.append(
                    {
                        "source_sheet": sheet,
                        "row_number": int(row_number),
                        "raw_row": raw_row,
                    }
                )

    wine_raw = pd.DataFrame(parsed_rows)
    wine_raw["rating"] = pd.to_numeric(wine_raw["rating"], errors="coerce")
    wine_raw["rating_count"] = pd.to_numeric(wine_raw["rating_count"], errors="coerce")
    wine_raw["price"] = pd.to_numeric(wine_raw["price"], errors="coerce")

    problems = pd.DataFrame(problem_rows)
    return wine_raw, problems


# ---------------------------------------------------------------------------
# Notebook-to-module helpers
#
# These functions are intentionally kept very close to the original notebook
# definitions so students can see the direct "cut/paste into src/" workflow.
# ---------------------------------------------------------------------------


def clean_tuple_text(value):
    """
    Clean tuple-like strings such as ('Frankrijk',) into plain text.
    """
    if pd.isna(value):
        return np.nan

    value = str(value)
    # Vivino exports sometimes store values like ("Italy",) as literal strings.
    # We remove punctuation so we can treat them as plain categorical text.
    value = value.replace("(", "")
    value = value.replace(")", "")
    value = value.replace("'", "")
    value = value.replace('"', "")
    value = value.replace(",", "")
    value = value.strip()

    return value


def fix_encoding_issues(value):
    """
    Fix common encoding issues found in country, region, and wine name text.
    The replacements are intentionally limited to visible recurring patterns.
    """
    if pd.isna(value):
        return np.nan

    value = str(value)

    replacements = {
        "√´": "ë",
        "√©": "é",
        "√®": "è",
        "√™": "ê",
        "√¢": "â",
        "√†": "à",
        "√¥": "ô",
        "√∂": "ö",
        "√º": "ü",
        "√±": "ñ",
        "√ß": "ß",
        "¬¥": "'",
        "¬∞": "°",
        "¬Æ": "®",
        "¬©": "©",
        "√": "",
    }

    for wrong, correct in replacements.items():
        # Simple, transparent replacement pass (no regex) to keep it teachable.
        value = value.replace(wrong, correct)

    return value.strip()


def fix_remaining_text_artifacts(value):
    """
    Fix remaining visible text artifacts after the first encoding cleanup.
    """
    if pd.isna(value):
        return np.nan

    value = str(value)

    replacements = {
        "‚Äô": "'",
        "‚Äò": "'",
        "‚Äú": '"',
        "‚Äù": '"',
        "‚Äì": "-",
        "‚Äî": "-",
        "‚Ä°": "I",
        "¬¥": "'",
        "Â": "",
        "Ã©": "é",
        "Ã¨": "è",
        "Ã«": "ë",
        "Ã´": "ô",
        "Ã¢": "â",
        "Ã¼": "ü",
        "Ã¶": "ö",
        "Ã±": "ñ"
    }

    for wrong, correct in replacements.items():
        value = value.replace(wrong, correct)

    return value.strip()


def build_wine_level_dataset(wine_raw: pd.DataFrame) -> pd.DataFrame:
    """Deduplicate, clean, and aggregate parsed rows to *wine-level*.

    This mirrors the notebook pipeline:
    1) drop duplicate raw rows
    2) clean tuple-like country/region strings
    3) aggregate to one row per (name, country, region)
    4) fix the most common encoding artifacts in the resulting text columns
    """

    # 1) Remove exact duplicate rows produced by the workbook export.
    wine_df = wine_raw.drop_duplicates().copy()

    # 2) Normalize tuple-like values stored as strings, e.g. "('Italië',)".
    wine_df["country_clean"] = wine_df["country"].apply(clean_tuple_text)
    wine_df["region_clean"] = wine_df["region"].apply(clean_tuple_text)

    wine_level = (
        wine_df.groupby(["name", "country_clean", "region_clean"], as_index=False)
        .agg(
            # Ratings: use a robust central tendency (median) across price observations.
            rating=("rating", "median"),
            # Rating count: take the maximum count observed for that wine.
            rating_count=("rating_count", "max"),
            min_price=("price", "min"),
            median_price=("price", "median"),
            max_price=("price", "max"),
            price_observations=("price", "count"),
            source_sheet_count=("source_sheet", "nunique"),
        )
    )

    for col in ["name", "country_clean", "region_clean"]:
        # Only run the first-pass encoder fix here.
        # The notebook performs an optional second-pass cleanup on the Italian subset.
        wine_level[col] = wine_level[col].apply(fix_encoding_issues)

    return wine_level


def filter_italian_wines(wine_level: pd.DataFrame, country_label: str = "Italië") -> pd.DataFrame:
    italian = wine_level[wine_level["country_clean"] == country_label].copy()
    italian = italian.reset_index(drop=True)
    return italian
