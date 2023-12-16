import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random

from PIL import Image
logo = Image.open('corona.jpeg')
#pip install pandas numpy matplotlib seaborn streamlit
#to run strealit :   streamlit run test2.py 

st.set_page_config(page_title="Corona  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
# Define the list of names
names = [ "k.reshi charan","U.N.V.Raviteja","Ganesh","p.Chandu"]
st.title("Exploratory Data Analysis on Covid-19 In India")
# Add the names to the sidebar
st.sidebar.title("Team Head:")
st.sidebar.write("M.Ankammarao")
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)
st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
# File upload
uploaded_file = st.file_uploader("Choose a  Covid-19 in India Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    pd.DataFrame(data)
    st.title("Covid-19 In India Data Analysis")
if st.checkbox("Get the head of the data"):
    st.write(data.head())
if st.checkbox("Check The Total Cases of Andhra Pradesh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Andhra Pradesh']['Total Cases'].values[0]
    st.write(f"Total Cases in Andhra Pradesh: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Andaman and Nicobar"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Andaman and Nicobar']['Total Cases'].values[0]
    st.write(f"Total Cases in Andaman and Nicobar: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Arunachal Pradesh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Arunachal Pradesh']['Total Cases'].values[0]
    st.write(f"Total Cases in Andhra Pradesh: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Assam"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Assam']['Total Cases'].values[0]
    st.write(f"Total Cases in Assam: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Bihar"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Bihar']['Total Cases'].values[0]
    st.write(f"Total Cases in Bihar: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of AChandigarh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Chandigarh']['Total Cases'].values[0]
    st.write(f"Total Cases in Chandigarh: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Chhattisgarh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Chhattisgarh']['Total Cases'].values[0]
    st.write(f"Total Cases in Chhattisgarh: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Dadra and Nagar Haveli and Daman and Diu"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Dadra and Nagar Haveli and Daman and Diu']['Total Cases'].values[0]
    st.write(f"Total Cases in Dadra and Nagar Haveli and Daman and Diu: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Delhi"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Delhi']['Total Cases'].values[0]
    st.write(f"Total Cases in Delhi: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Goa"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Goa']['Total Cases'].values[0]
    st.write(f"Total Cases in Goa: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Gujarat"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Gujarat']['Total Cases'].values[0]
    st.write(f"Total Cases in Gujarat: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Haryana"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Haryana']['Total Cases'].values[0]
    st.write(f"Total Cases in Haryana: {total_cases_andhra_pradesh}")
if st.checkbox("Check The Total Cases of Himachal Pradesh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Himachal Pradesh']['Total Cases'].values[0]
    st.write(f"Total Cases in Himachal Pradesh: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Jammu and Kashmir"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Jammu and Kashmir']['Total Cases'].values[0]
    st.write(f"Total Cases in Jammu and Kashmir: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Jharkhand"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Jharkhand']['Total Cases'].values[0]
    st.write(f"Total Cases in Jharkhand: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Karnataka"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Karnataka']['Total Cases'].values[0]
    st.write(f"Total Cases in Karnataka: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Kerala"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Kerala']['Total Cases'].values[0]
    st.write(f"Total Cases in Kerala: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Ladakh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Ladakh']['Total Cases'].values[0]
    st.write(f"Total Cases in Ladakh: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Lakshadweep"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Lakshadweep']['Total Cases'].values[0]
    st.write(f"Total Cases in Lakshadweep: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Madhya Pradesh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Madhya Pradesh']['Total Cases'].values[0]
    st.write(f"Total Cases in Madhya Pradesh: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Maharashtra"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Maharashtra']['Total Cases'].values[0]
    st.write(f"Total Cases in Maharashtra: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Manipur"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Manipur']['Total Cases'].values[0]
    st.write(f"Total Cases in Manipur: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Meghalaya"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Meghalaya']['Total Cases'].values[0]
    st.write(f"Total Cases in Meghalaya: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Mizoram"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Mizoram']['Total Cases'].values[0]
    st.write(f"Total Cases in Mizoram: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Nagaland"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Nagaland']['Total Cases'].values[0]
    st.write(f"Total Cases in Nagaland: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Odisha"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Odisha']['Total Cases'].values[0]
    st.write(f"Total Cases in Odisha: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Puducherry"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Puducherry']['Total Cases'].values[0]
    st.write(f"Total Cases in Puducherry: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Punjab"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Punjab']['Total Cases'].values[0]
    st.write(f"Total Cases in Punjab: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Rajasthan"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Rajasthan']['Total Cases'].values[0]
    st.write(f"Total Cases in Rajasthan: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Sikkim"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Sikkim']['Total Cases'].values[0]
    st.write(f"Total Cases in Sikkim: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Tamil Nadu"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Tamil Nadu']['Total Cases'].values[0]
    st.write(f"Total Cases in Tamil Nadu: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Telengana"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Telengana']['Total Cases'].values[0]
    st.write(f"Total Cases in Telengana: {total_cases_andhra_pradesh}")



if st.checkbox("Check The Total Cases of Tripura"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Tripura']['Total Cases'].values[0]
    st.write(f"Total Cases in Tripura: {total_cases_andhra_pradesh}")

if st.checkbox("Check The Total Cases of Uttar Pradesh"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'Uttar Pradesh']['Total Cases'].values[0]
    st.write(f"Total Cases in Uttar Pradesh: {total_cases_andhra_pradesh}")


if st.checkbox("Check The Total Cases of West Bengal"):
    total_cases_andhra_pradesh = data[data['State/UTs'] == 'West Bengal']['Total Cases'].values[0]
    st.write(f"Total Cases in West Bengal: {total_cases_andhra_pradesh}")
if st.checkbox("Get Data Visualization Of Corona In India State Wise"):
    selected_state = st.selectbox('Select a State/UT:', data.get('State/UTs', []))

    if st.button('Show Plots'):
        try:
            fig, axes = plt.subplots(1, 3, figsize=(15, 5))

            # Plot Death Ratio
            axes[0].bar(data['State/UTs'], data['Death Ratio'])
            axes[0].set_title('Death Ratio')
            axes[0].set_ylabel('Ratio')
            axes[0].set_xticklabels(data['State/UTs'], rotation=45)
            
            # Plot Discharge Ratio
            axes[1].bar(data['State/UTs'], data['Discharge Ratio'])
            axes[1].set_title('Discharge Ratio')
            axes[1].set_ylabel('Ratio')
            axes[1].set_xticklabels(data['State/UTs'], rotation=45)

            # Plot Population
            axes[2].bar(data['State/UTs'], data['Population'])
            axes[2].set_title('Population')
            axes[2].set_ylabel('Population')
            axes[2].set_xticklabels(data['State/UTs'], rotation=45)

            plt.tight_layout()
            st.pyplot(fig)
        except KeyError as e:
            st.error(f"KeyError: {e} - Data might be missing or in an unexpected format.")



st.title('Total COVID-19 Cases by State/UTs')

if st.button('Show Total Cases Plot'):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data['State/UTs'], data['Total Cases'], color='skyblue')
    ax.set_xlabel('State/UTs')
    ax.set_ylabel('Total Cases')
    ax.set_title('Total COVID-19 Cases by State/UTs')
    ax.set_xticklabels(data['State/UTs'], rotation=45)
    st.pyplot(fig)
st.title('COVID-19 Active Ratio by State')

if st.button('Show Active Ratio Plot'):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data['State/UTs'], data['Active Ratio'], color='salmon')
    ax.set_xlabel('State/UTs')
    ax.set_ylabel('Active Ratio (%)')
    ax.set_title('COVID-19 Active Ratio by State/UTs')
    ax.set_xticklabels(data['State/UTs'], rotation=45)
    st.pyplot(fig)
st.title('COVID-19 Discharge Ratio by State')

if st.button('Show Discharge Ratio Plot'):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data['State/UTs'], data['Discharge Ratio'], color='lightgreen')
    ax.set_xlabel('State/UTs')
    ax.set_ylabel('Discharge Ratio (%)')
    ax.set_title('COVID-19 Discharge Ratio by State/UTs')
    ax.set_xticklabels(data['State/UTs'], rotation=45)
    st.pyplot(fig)
st.title('COVID-19 Impact: Cases and Population')

if st.button('Show Impact Plot'):
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot Total Cases
    ax.bar(data['State/UTs'], data['Total Cases'], color='skyblue', label='Total Cases')

    # Plot Population (scaled for better visualization)
    scaled_population = [pop / 1000 for pop in data['Population']]  # scaling for better representation
    ax.plot(data['State/UTs'], scaled_population, marker='o', linestyle='-', color='orange', label='Population (scaled)')

    ax.set_xlabel('State/UTs')
    ax.set_ylabel('Count / Population (scaled)')
    ax.set_title('COVID-19 Impact: Cases and Population')
    ax.set_xticklabels(data['State/UTs'], rotation=45)
    ax.legend()

    st.pyplot(fig)



