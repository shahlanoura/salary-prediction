import streamlit as st
import pandas as pd 

st.title("Salary prediction")
nav=st.sidebar.radio(["Home","Prediction","Contribute"])

if nav=="Home":
    st.write("Home")
if nav=="Prediction":
    st.write("Predictio")
if nav=="Contribute":
    st.write("Contribute")
    