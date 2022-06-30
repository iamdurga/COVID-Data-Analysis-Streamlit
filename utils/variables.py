"""
To set global variables.
"""

import streamlit as st
import pandas as pd

file_path = "F:/MDS-Private-Study-Materials/Second Semester/Python Programming/Assignment/data.csv"
cols = ["continent","location","date","total_cases","new_cases","total_deaths",
            "new_deaths","new_tests",
            "total_vaccinations","total_boosters","new_vaccinations"]

trend_levels=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"]
trend_kwds = {"Daily": "1D", "Weekly": "1W", "Monthly": "1M", "Quarterly": "1Q", "Yearly": "1Y"}
