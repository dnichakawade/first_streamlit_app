import streamlit
import pandas

streamlit.title('This is my first Streamlit python program.')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smothie')
streamlit.text('Hard Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index("Fruit")

# Lets insert pick list here so that parents can pick the fruits they want to include in Smoothie

# streamlit.multiselect("Pick Fruits from the list for Smoothie", list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick Fruits from the list for Smoothie", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]

#Display in the table on the page
#streamlit.dataframe(my_fruit_list)

#Display fruits to show
streamlit.dataframe(fruits_to_show)

