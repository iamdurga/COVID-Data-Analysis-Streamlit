"""
To set global variables.
"""

file_path = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
cols = ["continent","location","date","total_cases","new_cases","total_deaths",
            "new_deaths","new_tests",
            "total_vaccinations","total_boosters","new_vaccinations"]

trend_levels=["Daily", "Weekly", "Monthly", "Quarterly", "Yearly"]
trend_kwds = {"Daily": "1D", "Weekly": "1W", "Monthly": "1M", "Quarterly": "1Q", "Yearly": "1Y"}
