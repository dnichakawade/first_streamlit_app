# streamlit_app.py

import streamlit as st
import snowflake.connector

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return snowflake.connector.connect(
        **st.secrets["snowflake"], client_session_keep_alive=True
    )

conn = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("use WAREHOUSE COMPUTE_WH; SELECT * from  fruityvice;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")

#import streamlit

#import snowflake.connector

#try:
#  my_cnx = snowflake.connector.connect(**streamlit.secrets[snowflake])
#except Exception as e:
#  return [[e, e]]

# my_cnx = snowflake.connector.connect(**streamlit.secrets[snowflake])

#my_cur = my_cnx.cursor()
#my_cur.execute("select CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()

#streamlit.text("Hello from Snowflake Database:")
#streamlit.text(my_data_row)



# 1 import streamlit
# 1 import pandas

# 1 streamlit.title('This is my first Streamlit python program.')
# 1 streamlit.header('Breakfast Menu')
# 1 streamlit.text('Omega 3 & Blueberry Oatmeal')
# 1 streamlit.text('Kale, Spinach & Rocket Smothie')
# 1 streamlit.text('Hard Boiled Free-Range Egg')

# 1 my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# 1 my_fruit_list = my_fruit_list.set_index("Fruit")

# 1 #Lets insert pick list here so that parents can pick the fruits they want to include in Smoothie

# 1 #streamlit.multiselect("Pick Fruits from the list for Smoothie", list(my_fruit_list.index))
# 1 fruits_selected=streamlit.multiselect("Pick Fruits from the list for Smoothie", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
# 1 fruits_to_show=my_fruit_list.loc[fruits_selected]

# 1 #Display in the table on the page
# 1 #streamlit.dataframe(my_fruit_list)

# 1 #Display fruits to show
# 1 streamlit.dataframe(fruits_to_show)
