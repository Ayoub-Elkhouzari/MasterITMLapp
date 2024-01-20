import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('model.pkl', 'rb'))
st.title('Bank marketing classifier')
# Declaring the teams

jobs = ['blue_collar','services','student','management','admin','technician'
        'self-employed','entrepreneur','retired','unemployed','housemaid'
        ,'unknown']
job_mapping = {'admin': 0,'blue_collar': 1,'entrepreneur': 2,'housemaid': 3,'management': 4,'retired': 5,
               'self_employed': 6,'services': 7,'student': 8,'technician': 9,'unemployed': 10,'unknown': 11,}

maritals = ['married','single','divorced']
marital_mapping = {'divorced':  0,'married':  1,'single':  2,}

housings = ['0','1']
housing_mapping = {'0': 0,'1': 1}

contacts = ['unknown','cellular','telephone']
contact_mapping = {'cellular':  0,'telephone':  1,'unknown':  2,}

col1, col2= st.columns(2)
with col1:
    age = st.text_input('Age')

with col2:
    balancePerYear = st.text_input('BalancePerYear')
    
col3, col4= st.columns(2)

with col3:
    duration = st.text_input('Duration')

with col4:
    pdays = st.text_input('Pdays')


col5, col6= st.columns(2)

with col5:
    jobc = st.selectbox('Select Job', sorted(jobs))
job = job_mapping.get(jobc, None)

with col6:
    maritalc = st.selectbox('Select Marital', sorted(maritals))
marital = marital_mapping.get(maritalc, None)


col7, col8= st.columns(2)
with col7:
    housingc = st.selectbox('Select Housing', sorted(housings))
housing = housing_mapping.get(housingc, None)


with col8:
    contactc = st.selectbox('Select Contact', sorted(contacts))
contact = contact_mapping.get(contactc, None)



new_user_features = pd.DataFrame({'age': [age], 'balancePerYear': [balancePerYear], 'duration': [duration] ,'pdays': [pdays],
                                      'job': [job] , 'marital': [marital], 'housing': [housing], 'contact': [contact]})
if st.button('Predict'):
    result = model.predict(new_user_features)
    prob = result[0]
    if prob==2:
        st.header("The client will * deposit a term *")
    else:
        st.header("The client will * not deposit a term *")
