
import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("best_rf_model.pkl")  # Ensure the model file is in the same directory

# Function to make predictions
def predict(input_data):
    prediction = model.predict([input_data])
    return prediction[0]  # Return the single prediction value

# Streamlit app code
st.title("NefroAi: Kidney Disease Prediction")

st.markdown("""
This app predicts ckd disease. 
Fill in the fields below and click **Predict**.
""")

# Input fields for user data
home = st.number_input("Home", min_value=-3.715828242, max_value=1.7989894586228334, step=0.011029635400778294, value=-3.715828242)
pcv = st.number_input("PCV", min_value=-3.95699001, max_value=1.7527489142768187, value=-3.95699001, step=0.011419477847590169)
rc = st.number_input("Rc", min_value=-3.354615389, max_value=3.9102015151235343, value=-3.354615389, step=0.014529633808600693)
sc = st.number_input("Sc", min_value=-0.440194033, max_value=14.401746112931715, step=0.029683880292612562, value=-0.440194033)
sg = st.number_input("Sg", min_value=-2.532423687, max_value=1.2364234115245358, step=0.007537694197558072, value=-2.532423687)
bgr = st.number_input("Bgr", min_value=-1.727735107, max_value=5.08015862133763, step=0.013615787457457534, value=-1.727735107)
al = st.number_input("Al", min_value=-0.672554267, max_value=2.4107830163289914, step=0.006166674566801247, value=-0.672554267)
sod = st.number_input("Sod", min_value=-15.66244722, max_value=2.8997009511666754, step=0.037124296345604615, value=-15.66244722)
pot = st.number_input("Pot", min_value=-0.819481504, max_value=16.78340056665894, step=0.035205764140927374, value=-0.819481504)
bu = st.number_input("Bu", min_value=-1.128119215, max_value=7.468757655114903, step=0.01719375374019046, value=-1.128119215)


# Collect all inputs in a list
input_data = [
    home, pcv, rc, sc, sg, bgr, al, sod, pot, bu ]

# Prediction button
if st.button("Predict"):
    prediction = predict(input_data)
    
    # Display the prediction result
    if prediction == 1:
        st.error("Machine predict CKD , Please meet doctor soon")
    else:
        st.success("Machine predict, you are safe")
