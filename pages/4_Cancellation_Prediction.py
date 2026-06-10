import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
st.title("Cancellation Prediction")
st.image("https://static.vecteezy.com/system/resources/previews/072/958/101/non_2x/open-cardboard-box-with-red-cross-symbol-indicating-delivery-rejection-or-cancellation-vector.jpg")
df=pd.read_csv("Amazon Sale Report.csv", low_memory=False)
df['Cancelled']=np.where(df['Status'].str.contains("Cancelled", na=False), 1, 0)
features=['Category','Size','Qty','Fulfilment','Amount']
target="Cancelled"
df=df[features+[target]].dropna()

#label encoding
encoders={}
for col in ['Category','Size','Fulfilment']:
    le=LabelEncoder()
    df[col]=le.fit_transform(df[col].astype(str))
    encoders[col]=le

#features and target
X=df[features]
y=df[target]
#train test split
X_train, X_test, y_train, y_test=train_test_split(X,y, random_state=42, test_size=0.2)

#model training
model=RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
#accuracy
pred=model.predict(X_test)
accuracy=accuracy_score(y_test, pred)
st.success(f"Model Accuracy: {accuracy:.2f}")
st.markdown("### Predict Cancellation")
#user input
category=st.selectbox("Category", encoders['Category'].classes_)
size=st.selectbox("Size", encoders['Size'].classes_)
qty=st.number_input("Quantity", min_value=1, step=1)
fulfilment=st.selectbox("Fulfilment", encoders['Fulfilment'].classes_)
amount=st.number_input("Amount", min_value=0.0, step=0.01)
if st.button("Predict Status"):
    input_data=pd.DataFrame({
        'Category':[encoders['Category'].transform([category])[0]],
        'Size':[encoders['Size'].transform([size])[0]],
        'Qty':[qty],
        'Fulfilment':[encoders['Fulfilment'].transform([fulfilment])[0]],
        'Amount':[amount]
    })

    result=model.predict(input_data)[0]

    if result==1:
        st.error("High Cancellation Risk")
    else:
        st.success("Low Cancellation Risk")

