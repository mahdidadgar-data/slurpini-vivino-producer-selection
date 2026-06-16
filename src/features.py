from __future__ import annotations

import re

import numpy as np
import pandas as pd


def add_value_metrics(df: pd.DataFrame, min_rating_count: int = 100) -> pd.DataFrame:
    """Add value-for-money metrics and apply a minimum rating-count filter.

    Returns a filtered copy of df with new columns.
    """

    # Work on a copy so callers don't get surprise in-place column additions.
    out = df.copy()

    # Enforce a minimum number of consumer ratings for robustness.
    # This reduces the chance that a high score is driven by a tiny sample.
    out = out[out["rating_count"] >= min_rating_count].copy()

    # Simple "value" heuristics: higher rating, lower price => higher score.
    out["rating_per_euro"] = out["rating"] / out["median_price"]
    out["weighted_value_score"] = (
        out["rating"] * np.log1p(out["rating_count"])
    ) / out["median_price"]

    return out


def min_max_scale(series: pd.Series) -> pd.Series:
    """
    Scale a numeric pandas Series to a 0-1 range.
    If all values are equal, return 0.5 for all rows to avoid division by zero.
    """
    # Compute bounds once; pandas will ignore NaNs by default.
    min_value = series.min()
    max_value = series.max()

    if max_value == min_value:
        # If everything is identical, all points are "in the middle" of the range.
        return pd.Series(0.5, index=series.index)

    return (series - min_value) / (max_value - min_value)


def classify_region(row: pd.Series, region_model: pd.DataFrame) -> str:
    """
    Assign a business-oriented strategic category based on rating, price, and value profile.
    """
    # Same business rules as the original notebook, but with `region_model`
    # passed explicitly to avoid relying on a hidden global variable.
    if row["avg_rating"] >= 4.2 and row["median_price"] >= 100:
        return "Premium quality opportunity"
    elif row["avg_weighted_value_score"] >= region_model["avg_weighted_value_score"].quantile(0.75):
        return "Value-for-money opportunity"
    elif row["median_rating_count"] >= region_model["median_rating_count"].quantile(0.75):
        return "High-visibility market opportunity"
    else:
        return "Secondary opportunity"


def extract_producer_from_name(name: str) -> str | None:
    """
    Heuristic producer extraction from Vivino-style wine names.

    Strategy (conservative):
    1) remove vintage year tokens (e.g., 2016)
    2) take the leading brand/producer chunk before common separators
    3) clean leftover punctuation and whitespace

    Returns None if the result is empty.
    """
    if name is None or (isinstance(name, float) and np.isnan(name)):
        return None
    s = str(name).strip()
    # Remove standalone 4-digit years (common vintage marker)
    s = re.sub(r"\b(19|20)\d{2}\b", "", s)
    # Split on separators that often separate producer from cuvée/appellation
    s = re.split(r"\s[-–|:]\s|\s\(|\s\[", s, maxsplit=1)[0]
    # If the name contains a comma, keep the part before comma
    s = s.split(',')[0]
    s = re.sub(r"\s+", " ", s).strip()
    # Strip surrounding double-quotes if they appear in the raw name
    s = s.strip('"')
    return s or None
