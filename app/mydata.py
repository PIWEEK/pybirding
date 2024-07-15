import streamlit as st
import pandas as pd
import numpy as np

st.title('Test with my data')

DATA_FILE = '../data/mydata/MyEBirdData.csv'

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_FILE)
    lowercase = lambda x: str(x).lower()
    df.rename(lowercase, axis='columns', inplace=True)
    replace_dunder = lambda x: x.replace(' ', '_')
    df.rename(replace_dunder, axis='columns', inplace=True)
    df['date'] = pd.to_datetime(df['date'])
    return df


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load allrows of data into the dataframe.
data = load_data()
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of birds')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
hist_values = data.groupby(['scientific_name'])['count'].sum().reset_index(name='count').sort_values(by='count', ascending=False)
st.bar_chart(hist_values, x="scientific_name", y="count", x_label='pajaricus')

# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all places')
st.map(data)
