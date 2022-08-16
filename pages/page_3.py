import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
 
 #データ関連
df = pd.read_csv('./data/data.csv', index_col='月')
#st.dataframe(df)
#st.table(df)
st.line_chart(df)
st.bar_chart(df['2021年'])
#matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['2021年']) 
ax.set_title('matplot graph')
st.pyplot(fig)