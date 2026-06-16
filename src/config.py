from __future__ import annotations

from pathlib import Path


def project_root() -> Path:
    """
    Return the repository root.

    Assumes this file lives in:
    <repo>/src/config.py
    """
    return Path(__file__).resolve().parents[1]


def data_dir(root: Path | None = None) -> Path:
    """Return the main data directory."""
    root = root or project_root()
    return root / "data"


def raw_data_dir(root: Path | None = None) -> Path:
    """Return the raw data directory."""
    return data_dir(root) / "raw"


def processed_data_dir(root: Path | None = None) -> Path:
    """Return the processed data directory."""
    return data_dir(root) / "processed"


def raw_excel_path(root: Path | None = None) -> Path:
    """Return the path to the original Vivino Excel export."""
    return raw_data_dir(root) / "Vivino-export.xlsx"


def cleaned_italian_wines_path(root: Path | None = None) -> Path:
    """Return the path to the cleaned Italian wine dataset."""
    return processed_data_dir(root) / "cleaned_italian_wines.csv"


def region_opportunity_scores_path(root: Path | None = None) -> Path:
    """Return the path to the region opportunity scores dataset."""
    return processed_data_dir(root) / "region_opportunity_scores.csv"


def strategic_region_summary_path(root: Path | None = None) -> Path:
    """Return the path to the strategic region summary dataset."""
    return processed_data_dir(root) / "strategic_region_summary.csv"