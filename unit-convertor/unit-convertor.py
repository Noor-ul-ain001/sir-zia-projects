import streamlit as st

def convert_units(value, unit_from, unit_to):
    
     conversion={
         "meter_kilometer":0.001,
         "kilometer_meter":1000,
         "gram_kilogram":0.001,
         "kilogram_gram":1000
     }
     
     key = f"{unit_from}_{unit_to}" # generate a unique key for conversion
     
     if key in conversion:
         conversions = conversion[key]
         return value * conversions
     else:
         return "conversion not supported"
     
st.title("Unit Convertor")

value = st.number_input("Enter the value to convert:")

unit_from = st.selectbox("Convert from ", ["meter", "kilometer", "gram", "kilogram"])

unit_to = st.selectbox("Convert to:", ["meter","kilometer", "gram", "kilogram"])   

if st.button("Convert"):
    result= convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")