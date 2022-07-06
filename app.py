import streamlit as st 
#header
st.set_page_config(page_title="Wabepage", page_icon=":tada:", layout="wide") 
st.title("Main Page 🎈")
st.sidebar.title("Side Page 🎈")
st.sidebar.markdown("<h1 style='text-align: left; color: orange;'> Well Come🎈</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: orange;'>Engineering Properties of Ethiopian Grains Crops</h1>", unsafe_allow_html=True)
st.write("Five major cereals (Teff, Wheat, Maize, Sorghum and Barley)")
st.write("-----------")
st.markdown("<h1 style='text-align: left; color: blue;'>Available Data</h1>", unsafe_allow_html=True)
#subheader
st.markdown("<h1 style='text-align: left; color: orange;'>A.Physical Properties</h1>", unsafe_allow_html=True)
st.write("(Size, Shape, Roundness,  Sphercity, Volume, Bulk Density, Solid Density, Porosity, Shrinkage, Color and Appearance and Moisture Content)")
import pandas as pd
df =pd.DataFrame({
  'Grains': ["Teff", "Wheat","Maize", "Sorghum","Barly"],
  'Bulk Desinty': [20, 20, 30, 40,50],
  'Angle of Repose':[10, 20, 40, 50,60],
  'Porocity': [10, 20, 40, 50,70],
  'Roundness': [10, 20, 40, 50,60],
  'Coeffincient of Resistuttion': [1, 2, 3, 4,5],
  'Coeffincient of Friction': [0.1, 0.2, 0.3, 0.4,0.7]
})
st.table(df)
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
st.markdown("<h1 style='text-align: left; color: orange;'>B.Flow Properties</h1>", unsafe_allow_html=True) 
import streamlit as st
import pandas as pd
df =pd.DataFrame({
  'Grains': ["Teff", "Wheat","Maize", "Sorghum","Barly"],
  'Segregation': [20, 20, 30, 40,50],
  'Velocity':[10, 20, 40, 50,60],
  'Impact Force': [10, 20, 40, 50,70],
  'Funel Flow': [10, 20, 40, 50,60],
  'Silo Dicharge': [1, 2, 3, 4,5]
}) 
st.table(df)  
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )
st.markdown("<h1 style='text-align: left; color: orange;'>C.Segregation Properties </h1>", unsafe_allow_html=True) 
import streamlit as st
import pandas as pd
df =pd.DataFrame({
  'Grains': ["Teff", "Wheat","Maize", "Sorghum","Barly"],
  'Segregation': [245, 2098, 300, 450,550],
  'Velocity':[10, 210, 420, 540,620],
  'Impact Force': [130, 240, 460, 560,720],
  'Funel Flow': [180, 280, 420, 510,630],
  'Silo Dicharge': [122, 233, 356, 456,511]
}) 
st.table(df) 
@st.cache
def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
     label="Download",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )


#chart representation
import pandas as pd
import numpy as np
import altair as alt
df = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.altair_chart(c, use_container_width=True)

import pandas as pd
import numpy as np
import altair as alt
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])
import pandas as pd
import numpy as np

st.bar_chart(chart_data)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

#sidebar   
date = st.sidebar.date_input("Date")
text=st.sidebar.text_area("Write Comment Here")
st.write(text)
button1=st.sidebar.button("Submit Text")
uploaded_files=st.sidebar.file_uploader("Chose a csv file",accept_multiple_files=True)
for uploaded_file in uploaded_files:
      bytes_data=uploaded_file.read()
      st.write("filename:",uploaded_file.name)
      st.write(bytes_data)
#sidebar
st.sidebar.checkbox("How Many Grain Crops Do You Know?")
Grain = st.sidebar.slider('Slide Slider?',0, 15, 5)
st.sidebar.write("I know ", Grain, 'Grain Crops')
st.sidebar.checkbox("Which is of This You Know More?", key=button1)
st.sidebar.radio(
       "How many Grains?",
        ["1 Wheat", "2 Teff", "3 Maize","4 Sorghum","5 Barley"],
        key=button1,
    )
#add file
st.write("##")
st.write("---") 
st.sidebar.markdown("<h1 style='text-align: left; color: green;'>Contact Info</h1>", unsafe_allow_html=True)
st.sidebar.text_input('Full Name')
st.sidebar.text_input('Email address')
st.sidebar.text_input('Phone No')
st.balloons()
color = st.sidebar.color_picker('Pick Your Favorable Color', '#00f900')
st.sidebar.write('The current color is', color)
st.write('Developer Lemi Demissie PhD student at Adama Science and Technology University')
st.markdown("<h1 style='text-align: center; color: gray;'>Streamlit Is a Faster Way To Build And Deploy Data Apps</h1>", unsafe_allow_html=True)














