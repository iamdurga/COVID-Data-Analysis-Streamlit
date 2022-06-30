"""
A main file to create an app.
"""

import streamlit as st
import pandas as pd
import cufflinks # used in backend by pandas
from utils.variables import *

sidebar = st.sidebar

@st.cache
def get_data(root,cols):
    df = pd.read_csv(root)
    df["date"] = pd.to_datetime(df.date).dt.date
    df['date'] = pd.DatetimeIndex(df.date)
    return df[cols]


data = get_data(file_path,cols)


locations = data.location.unique().tolist()

location_selector = sidebar.selectbox(
    "Select a Location",
    locations
)
st.markdown(f"# Currently Selected Location: {location_selector}")


show_data = sidebar.checkbox("Show Data")
if show_data:    
    st.dataframe(data)
    

trend_level = sidebar.selectbox("Trend Level", trend_levels)
st.markdown(f"### Currently Selected Trend Level {trend_level}")



trend_data = data.query(f"location=='{location_selector}'").\
    groupby(pd.Grouper(key="date", 
    freq=trend_kwds[trend_level])).aggregate(new_cases=("new_cases", "sum"),
    new_deaths = ("new_deaths", "sum"),
    new_vaccinations = ("new_vaccinations", "sum"),
    new_tests = ("new_tests", "sum")).reset_index()

trend_data["date"] = trend_data.date.dt.date

tcols = [c for c in trend_data.columns if c !="date"]
trends = sidebar.multiselect("Please select trends: ", options=tcols)

subplots=sidebar.checkbox("Show Subplots", True)
if len(trends)>0:
    fig=trend_data.iplot(kind="line", asFigure=True, xTitle="Date", yTitle="Values",
                         x="date", y=trends, title=f"{trend_level} Trend of {', '.join(trends)}.", subplots=subplots)
    st.plotly_chart(fig, use_container_width=False)

