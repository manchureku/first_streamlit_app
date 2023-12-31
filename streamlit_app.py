import streamlit
streamlit.title ('My Parents New Healthy Diner')
streamlit.header (' Breakfast Favourites')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-bolied Free Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
#Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
 #Display the table on the page.
streamlit.dataframe(my_fruit_list)
#my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display on the page
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values 'jackfruit','papaya','kiwi','guava'")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("the fruit_load_list contains:")
streamlit.dataframe(my_data_rows)

############################

fruit_choice2 = streamlit.text_input('What fruit would you like to add?','')
streamlit.write('Thanks for adding ', fruit_choice2)
add_my_fruit = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice2)

# write your own comment -what does the next line do? 
fruityvice2_normalized = pandas.json_normalize(add_my_fruit.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice2_normalized)
#my_cur.execute("insert into fruit_load_list_values('from Streamlit')")
#def insert_row_snowflake(new_fruit):
# with my_cnx.cursor() as my_cur:
 # my_cur.execute("insert into fruit_load_list_values('jackfruit'+'papaya'+'guava'+'kiwi')")
 # return "Thanks for adding" + new_fruit
